import { RoadmapSummary } from "../../types/profile";

interface Props {
    roadmap: RoadmapSummary | null;
}

export default function RoadmapCard({ roadmap }: Props) {

    if (!roadmap) {

        return (

            <div className="rounded-xl bg-white p-6 shadow">

                <h2 className="text-xl font-semibold">
                    Learning Roadmap
                </h2>

                <p className="mt-4 text-gray-500">
                    No roadmap generated.
                </p>

            </div>

        );

    }

    return (

        <div className="rounded-xl bg-white p-6 shadow">

            <h2 className="text-xl font-semibold">
                Learning Progress
            </h2>

            <div className="mt-6">

                <div className="flex justify-between">

                    <span>
                        Progress
                    </span>

                    <div className="mt-3 h-4 rounded-full overflow-hidden bg-slate-200">

                        <div

                            className="h-full rounded-full bg-gradient-to-r from-blue-500 to-violet-600 transition-all duration-1000"

                            style={{
                                width: `${roadmap.progress}%`
                            }}

                        />

                    </div>

                </div>

                <div className="mt-2 h-3 rounded-full bg-gray-200 overflow-hidden">

                    <div
                        className="h-full bg-blue-600"
                        style={{
                            width: `${roadmap.progress}%`
                        }}
                    />

                </div>

            </div>

            <div className="grid grid-cols-3 gap-4 mt-8 text-center">

                <div>

                    <h3 className="text-2xl font-bold">
                        {roadmap.current_week}
                    </h3>

                    <p className="text-sm text-gray-500">
                        Current Week
                    </p>

                </div>

                <div>

                    <h3 className="text-2xl font-bold">
                        {roadmap.completed_weeks}
                    </h3>

                    <p className="text-sm text-gray-500">
                        Completed
                    </p>

                </div>

                <div>

                    <h3 className="text-2xl font-bold">
                        {roadmap.total_weeks}
                    </h3>

                    <p className="text-sm text-gray-500">
                        Total
                    </p>

                </div>

            </div>

        </div>

    );

}