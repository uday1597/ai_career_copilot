interface Props {
    assessment: {
        overall_score: number;
        mcq_score: number;
        coding_score: number;
        scenario_score: number;
    };
}

export default function ScoreCard({
    assessment,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-8 shadow-sm">

            <h2 className="text-2xl font-bold">
                Assessment Result
            </h2>

            <div className="mt-8 grid gap-6 lg:grid-cols-4">

                <div className="rounded-lg bg-indigo-50 p-6 text-center">

                    <p className="text-sm text-slate-500">
                        Overall
                    </p>

                    <h1 className="mt-2 text-5xl font-bold text-indigo-700">
                        {assessment.overall_score}%
                    </h1>

                </div>

                <div className="rounded-lg border p-6 text-center">

                    <p className="text-slate-500">
                        MCQ
                    </p>

                    <p className="mt-2 text-3xl font-bold">
                        {assessment.mcq_score}%
                    </p>

                </div>

                <div className="rounded-lg border p-6 text-center">

                    <p className="text-slate-500">
                        Coding
                    </p>

                    <p className="mt-2 text-3xl font-bold">
                        {assessment.coding_score}%
                    </p>

                </div>

                <div className="rounded-lg border p-6 text-center">

                    <p className="text-slate-500">
                        Scenario
                    </p>

                    <p className="mt-2 text-3xl font-bold">
                        {assessment.scenario_score}%
                    </p>

                </div>

            </div>

        </div>

    );

}