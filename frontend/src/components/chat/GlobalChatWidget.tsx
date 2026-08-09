"use client";

import {
    FormEvent,
    useState,
} from "react";

import ChatMessage from "@/src/components/chat/ChatMessage";

import {
    chatWithAssistant,
} from "@/src/services/assistant";

interface Message {
    role: "user" | "assistant";
    content: string;
}

export default function GlobalChatWidget() {

    const [open, setOpen] =
        useState(false);

    const [input, setInput] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [messages, setMessages] =
        useState<Message[]>([
            {
                role: "assistant",
                content:
                    "Hi! I'm your Career Copilot. How can I help you?",
            },
        ]);

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
        setMessages(
            previous => [
                ...previous,
                {
                    role: "user",
                    content: message,
                },
            ]
        );

        // Add empty assistant message
        setMessages(
            previous => [
                ...previous,
                {
                    role: "assistant",
                    content: "",
                },
            ]
        );

        setLoading(true);

        try {

            await chatWithAssistant(
                message,
                (chunk) => {

                    setMessages(
                        previous => {

                            const updated = [
                                ...previous,
                            ];

                            const lastIndex =
                                updated.length - 1;

                            updated[lastIndex] = {
                                ...updated[lastIndex],
                                content:
                                    updated[lastIndex]
                                        .content + chunk,
                            };

                            return updated;

                        }
                    );

                }
            );

        } catch (error) {

            console.error(
                "Assistant error:",
                error
            );

            setMessages(
                previous => {

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

                }
            );

        } finally {

            setLoading(false);

        }
    }
    return (

        <>

            {/* Floating Button */}

            {!open && (

                <button
                    onClick={() =>
                        setOpen(true)
                    }
                    className="fixed bottom-6 right-6 z-50 flex h-14 w-14 items-center justify-center rounded-full bg-slate-900 text-2xl text-white shadow-lg transition hover:scale-105 hover:bg-slate-800"
                    aria-label="Open Career Copilot"
                >
                    💬
                </button>

            )}


            {/* Chat Window */}

            {open && (

                <div className="fixed bottom-6 right-6 z-50 flex h-[520px] w-[380px] flex-col overflow-hidden rounded-2xl border bg-[var(--surface)] shadow-2xl">

                    {/* Header */}

                    <div className="flex items-center justify-between bg-slate-900 px-4 py-3 text-white">

                        <div>

                            <h2 className="font-semibold">
                                Career Copilot
                            </h2>

                            <p className="text-xs text-slate-300">
                                AI Career Assistant
                            </p>

                        </div>

                        <button
                            onClick={() =>
                                setOpen(false)
                            }
                            className="text-xl text-slate-300 hover:text-white"
                            aria-label="Close chat"
                        >
                            ×
                        </button>

                    </div>


                    {/* Messages */}

                    <div className="flex-1 space-y-3 overflow-y-auto bg-[var(--background)] p-4">

                        {messages.map(
                            (message, index) => (

                                <ChatMessage
                                    key={index}
                                    role={message.role}
                                    content={message.content}
                                />

                            )
                        )}

                        {loading && (

                            <div className="flex justify-start">

                                <div className="rounded-2xl border bg-[var(--surface)] px-3 py-2 text-sm text-slate-500 shadow-sm">

                                    Thinking...

                                </div>

                            </div>

                        )}

                    </div>


                    {/* Input */}

                    <form
                        onSubmit={sendMessage}
                        className="border-t bg-[var(--surface)] p-3"
                    >

                        <div className="flex gap-2">

                            <input
                                value={input}
                                onChange={
                                    event =>
                                        setInput(
                                            event.target.value
                                        )
                                }
                                placeholder="Ask anything..."
                                disabled={loading}
                                className="min-w-0 flex-1 rounded-xl border px-3 py-2 text-sm outline-none focus:ring-2 focus:ring-slate-300"
                            />

                            <button
                                type="submit"
                                disabled={
                                    loading ||
                                    !input.trim()
                                }
                                className="rounded-xl bg-slate-900 px-4 py-2 text-sm text-white disabled:opacity-50"
                            >
                                Send
                            </button>

                        </div>

                    </form>

                </div>

            )}

        </>

    );
}