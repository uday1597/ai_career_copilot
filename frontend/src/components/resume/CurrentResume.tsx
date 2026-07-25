"use client";

import { useResume } from "../../hooks/useResume";

export default function CurrentResume() {

    const {
        resume,
        hydrated,
        clearResume,
    } = useResume();
    
    if (!hydrated) {
        return null;
    }
    if (!resume) {
        return null;
    }

    return (

        <div className="rounded-xl border bg-white p-5">

            <h2 className="text-lg font-semibold">
                Current Resume
            </h2>

            <p className="mt-2">
                {resume.filename}
            </p>

            <button
                onClick={clearResume}
                className="mt-4 rounded bg-red-600 px-4 py-2 text-white"
            >
                Remove Resume
            </button>

        </div>

    );

}