export interface AssistantEvent {
    type:
        | "plan"
        | "tools"
        | "token"
        | "complete"
        | "error";

    content?: string;

    answer?: string;

    steps?: unknown[];

    results?: Record<string, unknown>;

    message?: string;
}


export async function chatWithAssistant(
    message: string,
    onToken: (token: string) => void,
): Promise<void> {

    const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/assistant/chat`,
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json",
                "Accept": "text/event-stream",
            },

            body: JSON.stringify({
                message,
            }),
        }
    );


    if (!response.ok) {

        throw new Error(
            `Assistant request failed: ${response.status}`
        );

    }


    if (!response.body) {

        throw new Error(
            "Assistant response does not support streaming."
        );

    }


    const reader =
        response.body.getReader();

    const decoder =
        new TextDecoder();

    let buffer = "";


    while (true) {

        const {
            value,
            done,
        } = await reader.read();


        if (done) {
            break;
        }


        buffer += decoder.decode(
            value,
            {
                stream: true,
            }
        );


        const events =
            buffer.split("\n\n");


        // Keep incomplete event
        buffer =
            events.pop() ?? "";


        for (const event of events) {

            const lines =
                event.split("\n");


            for (const line of lines) {

                if (
                    !line.startsWith("data:")
                ) {
                    continue;
                }


                const raw =
                    line
                        .slice(5)
                        .trim();


                if (!raw) {
                    continue;
                }


                let data: AssistantEvent;

                try {

                    data =
                        JSON.parse(raw);

                } catch (error) {

                    console.error(
                        "Invalid SSE data:",
                        raw,
                        error
                    );

                    continue;
                }


                // --------------------------------
                // ONLY tokens go to the chat UI
                // --------------------------------

                if (
                    data.type === "token" &&
                    data.content
                ) {

                    onToken(
                        data.content
                    );

                }


                // --------------------------------
                // Complete event
                //
                // We DON'T append it because
                // tokens already created the
                // complete answer.
                // --------------------------------

                if (
                    data.type === "complete"
                ) {

                    console.log(
                        "Assistant completed"
                    );

                }


                // --------------------------------
                // Plan / tool events
                //
                // Keep these internal for now.
                // --------------------------------

                if (
                    data.type === "plan"
                ) {

                    console.log(
                        "Agent plan:",
                        data.steps
                    );

                }


                if (
                    data.type === "tools"
                ) {

                    console.log(
                        "Tool results:",
                        data.results
                    );

                }


                if (
                    data.type === "error"
                ) {

                    throw new Error(
                        data.message ||
                        "Assistant error"
                    );

                }

            }

        }

    }

}
