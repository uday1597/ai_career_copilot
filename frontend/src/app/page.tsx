"use client";

import AppLayout from "../components/layout/AppLayout";

export default function Home() {
    return (
        <AppLayout>
            <div className="space-y-6">

                <h1 className="text-3xl font-bold">
                    Career Copilot
                </h1>

                <p className="text-slate-600">
                    Welcome to Career Copilot.
                </p>

            </div>
        </AppLayout>
    );
}