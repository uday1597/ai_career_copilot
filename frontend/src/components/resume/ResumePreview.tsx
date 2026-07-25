"use client";

import { useState } from "react";
import { getResumePreviewUrl } from "../../services/resume";
import { Resume } from "../../types/resume";

interface ResumePreviewProps {
    resume: Resume;
}

export default function ResumePreview({
    resume
}: ResumePreviewProps) {

    const [showPreview, setShowPreview] = useState(false);

    return (
        <div className="rounded-lg bg-green-100 p-4 space-y-4">

            <div className="flex items-center justify-between">

                <p>
                    Current Resume:
                    <strong className="ml-2">
                        {resume.filename}
                    </strong>
                </p>

                <button
                    onClick={() => setShowPreview(!showPreview)}
                    className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                >
                    {showPreview 
                        ? "Hide Preview" 
                        : "Preview Resume"
                    }
                </button>

            </div>


            {showPreview && (
                <div className="border rounded-lg overflow-hidden">

                    <iframe
                        src={getResumePreviewUrl(resume.id)}
                        className="w-full h-[700px]"
                        title="Resume Preview"
                    />

                </div>
            )}

        </div>
    );
}