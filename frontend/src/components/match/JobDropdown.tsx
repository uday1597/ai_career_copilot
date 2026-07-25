"use client";

import { Job } from "../../types/job";

interface JobDropdownProps {
    jobs: Job[];
    selectedJobId: string;
    onChange: (jobId: string) => void;
}

export default function JobDropdown({
    jobs,
    selectedJobId,
    onChange,
}: JobDropdownProps) {
    return (
        <div className="space-y-2">
            <label className="text-sm font-medium text-slate-700">
                Select Job
            </label>

            <select
                value={selectedJobId}
                onChange={(e) => onChange(e.target.value)}
                className="w-full rounded-lg border border-slate-300 bg-white p-3 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
            >
                <option value="">
                    -- Select a Job --
                </option>

                {jobs.map((job) => (
                    <option
                        key={`${job.id}`}
                        value={job.id}
                    >
                        {job.title}
                    </option>
                ))}
            </select>
        </div>
    );
}