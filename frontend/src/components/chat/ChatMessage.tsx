"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface ChatMessageProps {
    role: "user" | "assistant";
    content: string;
}

export default function ChatMessage({
    role,
    content,
}: ChatMessageProps) {

    const isUser = role === "user";

    return (
        <div
            className={`flex ${
                isUser
                    ? "justify-end"
                    : "justify-start"
            }`}
        >

            <div
                className={`max-w-[85%] rounded-2xl px-4 py-3 text-sm leading-6 ${
                    isUser
                        ? "bg-slate-900 text-white"
                        : "bg-[var(--surface)] text-slate-900 shadow-sm border"
                }`}
            >

                {isUser ? (

                    <div className="whitespace-pre-wrap">
                        {content}
                    </div>

                ) : (

                    <div className="prose prose-sm max-w-none prose-slate">

                        <ReactMarkdown
                            remarkPlugins={[
                                remarkGfm,
                            ]}
                        >
                            {content}
                        </ReactMarkdown>

                    </div>

                )}

            </div>

        </div>
    );
}