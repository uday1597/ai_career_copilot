import { CrawledJob } from "../../types/job";

interface Props {
    job: CrawledJob;
}

export default function JobCard({ job }: Props) {
    return (
        <div className="rounded-xl bg-white p-5 shadow transition hover:shadow-lg">
            <h2 className="text-xl font-bold text-slate-900">
                {job.title}
            </h2>

            <p className="mt-2 text-slate-700">
                <span className="font-medium">Company:</span> {job.company}
            </p>

            <p className="text-slate-700">
                <span className="font-medium">Location:</span> {job.location}
            </p>

            {job.department && (
                <p className="text-slate-700">
                    <span className="font-medium">Department:</span> {job.department}
                </p>
            )}

            <div className="mt-4">
                <a
                    href={job.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center rounded-lg bg-indigo-600 px-4 py-2 text-sm font-medium text-white transition hover:bg-indigo-700"
                >
                    View Job ↗
                </a>
            </div>
        </div>
    );
}