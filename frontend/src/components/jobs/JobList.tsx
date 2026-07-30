import JobCard from "./JobCard";
import { CrawledJob } from "../../types/job";

interface Props {
    jobs: CrawledJob[];
}

export default function JobList({ jobs }: Props) {
    if (jobs.length === 0) {
        return (
            <div className="rounded-xl border border-dashed border-slate-300 bg-white p-8 text-center text-slate-500">
                No jobs found. Click <strong>Discover Jobs</strong> to load opportunities.
            </div>
        );
    }

    return (
        <div className="space-y-4">
            {jobs.map((job) => (
                <JobCard
                    key={job.job_id}
                    job={job}
                />
            ))}
        </div>
    );
}