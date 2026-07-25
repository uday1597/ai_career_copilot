"use client";

interface MatchScoreCardProps {
    score: number;
}

export default function MatchScoreCard({
    score,
}: MatchScoreCardProps) {

    function getStatus() {

        if (score >= 90) return "Excellent";
        if (score >= 75) return "Very Good";
        if (score >= 60) return "Good";
        if (score >= 40) return "Fair";

        return "Needs Improvement";
    }

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-semibold">
                Match Score
            </h2>

            <div className="mt-6 flex items-center gap-6">

                <div className="text-5xl font-bold text-blue-600">
                    {score}%
                </div>

                <div className="flex-1">

                    <div className="h-4 overflow-hidden rounded-full bg-slate-200">

                        <div
                            className="h-full bg-blue-600 transition-all"
                            style={{
                                width: `${score}%`,
                            }}
                        />

                    </div>

                    <p className="mt-3 text-slate-600">
                        {getStatus()}
                    </p>

                </div>

            </div>

        </div>

    );

}