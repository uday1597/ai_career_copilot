"use client";

import { Week } from "../../types/roadMap";
import MiniProjectCard from "./MiniProjectCard";
import ResourceCard from "./ResourceCard";
import Link from "next/link";
import {
    AssessmentHistory,
} from "@/src/types/assessmentHistory";

interface Props{

    week: Week;

    matchId:string;

    assessment?:
        AssessmentHistory;

}

export default function TopicCard({
    week,
    matchId,
    assessment,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <div className="flex items-center justify-between">

                <div>

                    <p className="text-sm font-semibold text-indigo-600">
                        Week {week.week}
                    </p>

                    <h2 className="mt-1 text-2xl font-bold">
                        {week.focus}
                    </h2>

                </div>

            </div>

            <div className="mt-6">

                <h3 className="font-semibold text-slate-800">
                    Topics
                </h3>

                <div className="mt-3 flex flex-wrap gap-2">

                    {week.topics.map((topic) => (

                        <span
                            key={topic}
                            className="rounded-full bg-indigo-100 px-3 py-1 text-sm text-indigo-700"
                        >
                            {topic}
                        </span>

                    ))}

                </div>

            </div>

            <div className="mt-6 grid gap-4 lg:grid-cols-2">

                <MiniProjectCard
                    project={week.mini_project}
                />

                <ResourceCard
                    resources={week.resources}
                />

            </div>

            <div className="mt-8 flex items-center justify-between">

                <div>

                    {!assessment && (

                        <span
                            className="rounded-full bg-gray-100 px-4 py-2 text-sm"
                        >

                            Not Started

                        </span>

                    )}

                    {assessment?.status==="IN_PROGRESS" && (

                        <span
                            className="rounded-full bg-yellow-100 px-4 py-2 text-sm text-yellow-700"
                        >

                            In Progress

                        </span>

                    )}

                    {assessment?.status==="COMPLETED" && (

                        <div>

                            <span
                                className="rounded-full bg-green-100 px-4 py-2 text-sm text-green-700"
                            >

                                Completed

                            </span>

                            <p
                                className="mt-3 text-sm font-semibold"
                            >

                                Score

                                {" "}

                                {assessment.overall_score}%

                            </p>

                        </div>

                    )}

                </div>

                <Link

                    href={`/assessment?matchId=${matchId}&week=${week.week}`}

                    className="rounded-lg bg-indigo-600 px-5 py-2 text-white"

                >

                    {

                        assessment?.status==="COMPLETED"

                        ?

                        "Review"

                        :

                        assessment?.status==="IN_PROGRESS"

                        ?

                        "Continue"

                        :

                        "Take Assessment"

                    }

                </Link>

            </div>

        </div>

    );

}