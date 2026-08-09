"use client";

import { useState } from "react";

interface Message {
    id: string;
    role: "user" | "assistant";
    content: string;
}
import {
    chatWithAssistant
} from "@/src/services/assistant";

export default function ChatPage() {

    const [messages, setMessages] = useState<Message[]>([]);    

    const [input, setInput] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleSubmit() {

        const message = input.trim();
    
        if (!message || loading) {
            return;
        }
    
        const userMessage: Message = {
            id: crypto.randomUUID(),
            role: "user",
            content: message,
        };
    
        setMessages(previous => [
            ...previous,
            userMessage,
        ]);
    
        setInput("");
    
        const assistantId =
            crypto.randomUUID();
    
        setMessages(previous => [
            ...previous,
            {
                id: assistantId,
                role: "assistant",
                content: "",
            },
        ]);
    
        setLoading(true);
    
        try {
    
            await chatWithAssistant(
                message,
                (chunk) => {
    
                    setMessages(previous =>
                        previous.map(item =>
                            item.id === assistantId
                                ? {
                                    ...item,
                                    content:
                                        item.content +
                                        chunk,
                                }
                                : item
                        )
                    );
    
                }
            );
    
        } catch (error) {
    
            console.error(
                "Assistant error:",
                error
            );
    
            setMessages(previous =>
                previous.map(item =>
                    item.id === assistantId
                        ? {
                            ...item,
                            content:
                                "Sorry, I couldn't process your request. Please try again.",
                        }
                        : item
                )
            );
    
        } finally {
    
            setLoading(false);
    
        }
    }

    return (

        <div className="flex h-full min-h-[calc(100vh-64px)] flex-col">

            {/* Messages */}

            <div className="flex-1 overflow-y-auto">

                {messages.length === 0 ? (

                    <div className="flex h-full items-center justify-center px-6">

                        <div className="w-full max-w-3xl text-center">

                            <h2
                                className="
                                    text-4xl
                                    font-bold
                                    text-slate-900
                                    dark:text-slate-100
                                "
                            >                   
                                     What can I help you with?
                            </h2>

                            <p className="mt-4 text-slate-500 dark:text-slate-400">
                                Analyze your resume, discover jobs,
                                build learning roadmaps, prepare for
                                interviews, and more.
                            </p>

                            <div className="mt-8 grid gap-3 sm:grid-cols-2">

                                <Suggestion
                                    text="Analyze my resume"
                                    onClick={() =>
                                        setInput("Analyze my resume")
                                    }
                                />

                                <Suggestion
                                    text="Find jobs matching my skills"
                                    onClick={() =>
                                        setInput(
                                            "Find jobs matching my skills"
                                        )
                                    }
                                />

                                <Suggestion
                                    text="Create a learning roadmap"
                                    onClick={() =>
                                        setInput(
                                            "Create a learning roadmap for me"
                                        )
                                    }
                                />

                                <Suggestion
                                    text="Prepare me for an interview"
                                    onClick={() =>
                                        setInput(
                                            "Prepare me for an interview"
                                        )
                                    }
                                />

                            </div>

                        </div>

                    </div>

                ) : (

                    <div className="mx-auto w-full max-w-3xl space-y-6 px-6 py-8">

                        <div className="space-y-6">

                        {messages.map((message) => (

                            <div
                                key={message.id}
                                className={
                                    message.role === "user"
                                        ? "flex justify-end"
                                        : "flex justify-start"
                                }
                            >

                                {message.role === "user" ? (

                                    <div className="max-w-[80%] rounded-2xl bg-indigo-600 px-5 py-3 text-white shadow-sm">

                                        <p className="whitespace-pre-wrap leading-7">
                                            {message.content}
                                        </p>

                                    </div>

                                ) : (

                                    <div className="max-w-[85%] px-2 py-1">
                                        <p
                                            className="
                                                whitespace-pre-wrap
                                                leading-7
                                                text-slate-800
                                                dark:text-slate-200
                                            "
                                        >
                                            {message.content}
                                        </p>

                                    </div>

                                )}

                            </div>

                        ))}


                        {loading && (

                            <div className="flex justify-start">

                                <div className="px-2 py-1">

                                    <div className="flex items-center gap-1">

                                        <span className="h-2 w-2 animate-bounce rounded-full bg-slate-400" />

                                        <span
                                            className="h-2 w-2 animate-bounce rounded-full bg-slate-400"
                                            style={{
                                                animationDelay: "150ms",
                                            }}
                                        />

                                        <span
                                            className="h-2 w-2 animate-bounce rounded-full bg-slate-400"
                                            style={{
                                                animationDelay: "300ms",
                                            }}
                                        />

                                    </div>

                                </div>

                            </div>

                        )}

                        </div>

                    </div>

                )}

            </div>

            {/* Input */}

            <div
                className="
                    border-t
                    border-[var(--border)]
                    bg-[var(--background)]
                    p-5
                "
            >

                <form
                    onSubmit={event => {
                        event.preventDefault();
                        handleSubmit();
                    }}
                    className="mx-auto flex max-w-3xl items-end gap-3"
                >

                    <textarea
                        value={input}
                        onChange={event =>
                            setInput(event.target.value)
                        }
                        onKeyDown={event => {

                            if (
                                event.key === "Enter" &&
                                !event.shiftKey
                            ) {
                                event.preventDefault();
                                handleSubmit();
                            }

                        }}
                        placeholder="Ask Career Copilot anything..."
                        rows={1}
                        className="
                            max-h-40
                            min-h-[52px]
                            flex-1
                            resize-none
                            rounded-2xl
                            border
                            border-slate-300
                            bg-white
                            px-5
                            py-3
                            text-slate-900
                            outline-none

                            placeholder:text-slate-400

                            focus:border-indigo-500
                            focus:ring-2
                            focus:ring-indigo-100

                            dark:border-slate-700
                            dark:bg-slate-900
                            dark:text-slate-100
                            dark:placeholder:text-slate-500
                            dark:focus:border-indigo-500
                            dark:focus:ring-indigo-950
                        "
                    />

                    <button
                        type="submit"
                        disabled={!input.trim() || loading}
                        className="
                            h-[52px]
                            rounded-2xl
                            bg-indigo-600
                            px-6
                            font-medium
                            text-white
                            transition
                            hover:bg-indigo-700
                            disabled:cursor-not-allowed
                            disabled:opacity-50
                        "
                    >
                        Send
                    </button>

                </form>

                <p className="mx-auto mt-2 max-w-3xl text-center text-xs text-slate-400">
                    Career Copilot can help with resumes, jobs,
                    learning, assessments and interviews.
                </p>

            </div>

        </div>
    );
}


function Suggestion({
    text,
    onClick,
}: {
    text: string;
    onClick: () => void;
}) {

    return (

        <button
            type="button"
            onClick={onClick}
            className="
                rounded-xl
                border
                border-[var(--border)]
                bg-[var(--surface)]
                p-4
                text-left
                text-sm
                text-slate-700
                shadow-sm
                transition

                hover:border-indigo-300
                hover:bg-indigo-50

                dark:text-slate-200
                dark:hover:border-indigo-700
                dark:hover:bg-slate-800
            "
        >
            {text}
        </button>

    );
}