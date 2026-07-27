import { LatestMatch } from "@/src/types/dashboard";

interface Props {

    match: LatestMatch;

}

export default function MatchCard({

    match,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">

                Latest Match

            </h2>

            <p className="mt-4">

                {match.job_title}

            </p>

            <p className="text-slate-500">

                {match.company}

            </p>

            <div className="mt-6 text-4xl font-bold text-indigo-600">

                {match.match_score}%

            </div>

        </div>

    );

}