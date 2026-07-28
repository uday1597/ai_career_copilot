import { RoadmapSummary } from "@/src/types/dashboard";

interface Props {

    roadmap: RoadmapSummary;

}

export default function RoadmapProgressCard({

    roadmap,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">

                Roadmap Progress

            </h2>
            {roadmap?(
            <>
                <div className="mt-6">

                    <div className="h-4 rounded-full bg-slate-200">

                        <div
                            className="h-4 rounded-full bg-green-600"
                            style={{
                                width:
                                    `${roadmap.completion_percentage}%`,
                            }}
                        />

                    </div>

                </div>

                <div className="mt-6 space-y-2">

                    <p>

                        Completed: {roadmap.completed_weeks}

                    </p>

                    <p>

                        In Progress: {roadmap.in_progress_weeks}

                    </p>

                    <p>

                        Remaining: {roadmap.not_started_weeks}

                    </p>

                </div>
            </>
            ):(<div>No roadmap available yet.</div>)}

        </div>

    );

}