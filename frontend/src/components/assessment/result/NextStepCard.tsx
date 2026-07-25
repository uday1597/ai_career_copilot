"use client";

import { useRouter } from "next/navigation";

interface Props {
    nextAction: string;
}

export default function NextStepCard({
    nextAction,
}: Props) {

    const router = useRouter();

    return (

        <div className="rounded-xl border bg-indigo-50 p-8">

            <h2 className="text-2xl font-bold">

                🚀 Next Step

            </h2>

            <p className="mt-4 text-slate-700">

                {nextAction}

            </p>

            <button
                onClick={() => router.push("/roadmap")}
                className="mt-6 rounded-lg bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700"
            >

                Continue Learning →

            </button>

        </div>

    );

}