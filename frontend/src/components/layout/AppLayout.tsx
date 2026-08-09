"use client";

import Sidebar from "./Sidebar";

export default function AppLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <div className="flex h-screen overflow-hidden bg-[var(--background)]">
            <Sidebar />

            <main className="
                min-w-0
                flex-1
                overflow-y-auto
                bg-[var(--background)]
                text-[var(--foreground)]
            ">
                {children}
            </main>
        </div>
    );
}