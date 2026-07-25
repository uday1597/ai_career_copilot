import { Job } from "../../types/job";

interface Props {

    job: Job;

}

export default function JobCard({

    job

}: Props) {

    return (

        <div className="rounded-xl bg-white p-5 shadow">

            <h2 className="text-xl font-bold">

                {job.title}

            </h2>

            <p>{job.company}</p>

            <p>{job.location}</p>

        </div>

    );

}