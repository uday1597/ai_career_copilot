"use client";

import { Resume } from "../../types/resume";

interface ResumeDropdownProps {
    resumes: Resume[];
    selectedResumeId: string;
    onChange: (resumeId: string) => void;
}

export default function ResumeDropdown({
    resumes,
    selectedResumeId,
    onChange,
}: ResumeDropdownProps) {
    return (
        <div className="space-y-2">
            <label className="text-sm font-medium text-slate-700">
                Select Resume
            </label>

            <select
                value={selectedResumeId}
                onChange={(e) => onChange(e.target.value)}
                className="w-full rounded-lg border border-slate-300 bg-white p-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
            >
                <option value="">
                    -- Select a Resume --
                </option>

                {resumes.map((resume) => (
                    <option
                        key={`${resume.id}`}
                        value={resume.id}
                    >
                        {resume.filename}
                    </option>
                ))}
            </select>
        </div>
    );
}