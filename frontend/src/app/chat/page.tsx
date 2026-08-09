"use client";

import {
    FormEvent,
    useState,
} from "react";

import {
    chatWithAssistant,
} from "@/src/services/assistant";

interface Message {
    role: "user" | "assistant";
    content: string;
}

export default function ChatPage() {

    const [messages, setMessages] =
        useState<Message[]>([
            {
                role: "assistant",
                content:
                    "Hi! I'm your Career Copilot. Ask me about your resume, job match, learning roadmap, assessments, or career goals.",
            },
        ]);

    const [input, setInput] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    async function sendMessage(
        event: FormEvent
    ) {

        event.preventDefault();

        const message =
            input.trim();

        if (!message || loading) {
            return;
        }

        setInput("");

        // Add user message
        setMessages(previous => [
            ...previous,
            {
                role: "user",
                content: message,
            },
            {
                role: "assistant",
                content: "",
            },
        ]);

        setLoading(true);

        try {

            await chatWithAssistant(
                message,
                (chunk) => {

                    setMessages(previous => {

                        const updated = [
                            ...previous,
                        ];

                        const lastIndex =
                            updated.length - 1;

                        updated[lastIndex] = {
                            ...updated[lastIndex],
                            content:
                                updated[lastIndex].content +
                                chunk,
                        };

                        return updated;

                    });

                }
            );

        } catch (error) {

            console.error(
                "Assistant error:",
                error
            );

            setMessages(previous => {

                const updated = [
                    ...previous,
                ];

                const lastIndex =
                    updated.length - 1;

                updated[lastIndex] = {
                    role: "assistant",
                    content:
                        "Sorry, something went wrong. Please try again.",
                };

                return updated;

            });

        } finally {

            setLoading(false);

        }
    }

    return (

        <div
            className="
                flex
                h-full
                min-h-0
                flex-col
                bg-[var(--background)]
                text-[var(--foreground)]
            "
        >

            {/* Messages */}

            <div
                className="
                    flex-1
                    overflow-y-auto
                    px-4
                    py-8
                    sm:px-8
                "
            >

                <div
                    className="
                        mx-auto
                        flex
                        max-w-4xl
                        flex-col
                        gap-5
                    "
                >

                    {messages.map(
                        (message, index) => (

                            <div
                                key={index}
                                className={`flex ${
                                    message.role === "user"
                                        ? "justify-end"
                                        : "justify-start"
                                }`}
                            >

                                <div
                                    className={`
                                        max-w-[80%]
                                        rounded-2xl
                                        px-5
                                        py-3
                                        text-sm
                                        leading-6

                                        ${
                                            message.role === "user"
                                                ? `
                                                    bg-blue-600
                                                    text-white
                                                `
                                                : `
                                                    border
                                                    border-[var(--border)]
                                                    bg-[var(--surface)]
                                                    text-[var(--foreground)]
                                                `
                                        }
                                    `}
                                >

                                    {message.content}

                                </div>

                            </div>

                        )
                    )}

                    {loading && (

                        <div className="flex justify-start">

                            <div
                                className="
                                    rounded-2xl
                                    border
                                    border-[var(--border)]
                                    bg-[var(--surface)]
                                    px-5
                                    py-3
                                    text-sm
                                    text-slate-500
                                    dark:text-slate-400
                                "
                            >

                                <span className="flex items-center gap-2">

                                    <span className="h-2 w-2 animate-pulse rounded-full bg-slate-400" />

                                    Career Copilot is thinking...

                                </span>

                            </div>

                        </div>

                    )}

                </div>

            </div>


            {/* Input */}

            <div
                className="
                    border-t
                    border-[var(--border)]
                    bg-[var(--background)]
                    px-4
                    py-4
                    sm:px-8
                "
            >

                <form
                    onSubmit={sendMessage}
                    className="
                        mx-auto
                        max-w-4xl
                    "
                >

                    <div
                        className="
                            flex
                            items-center
                            gap-3
                            rounded-2xl
                            border
                            border-[var(--border)]
                            bg-[var(--surface)]
                            p-2
                            shadow-sm
                            dark:shadow-none
                        "
                    >

                        <input
                            value={input}
                            onChange={
                                event =>
                                    setInput(
                                        event.target.value
                                    )
                            }
                            placeholder="Ask your Career Copilot..."
                            disabled={loading}
                            className="
                                min-w-0
                                flex-1
                                bg-transparent
                                px-3
                                py-2
                                text-sm
                                text-[var(--foreground)]
                                outline-none
                                placeholder:text-slate-400
                                dark:placeholder:text-slate-500
                                disabled:opacity-50
                            "
                        />

                        <button
                            type="submit"
                            disabled={
                                loading ||
                                !input.trim()
                            }
                            className="
                                shrink-0
                                rounded-xl
                                bg-blue-600
                                px-5
                                py-2.5
                                text-sm
                                font-medium
                                text-white
                                transition
                                hover:bg-blue-700
                                disabled:cursor-not-allowed
                                disabled:opacity-40
                            "
                        >
                            Send
                        </button>

                    </div>

                    <p
                        className="
                            mt-2
                            text-center
                            text-xs
                            text-slate-400
                            dark:text-slate-500
                        "
                    >
                        Career Copilot can use your resume,
                        roadmap, assessments, and knowledge
                        base to answer questions.
                    </p>

                </form>

            </div>

        </div>
    );
}