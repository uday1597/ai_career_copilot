"use client";

interface Props {
    explanation: {
        summary: string;
        strengths: string[];
        missing_skills: string[];
        recommendations: string[];
    };
}

export default function AIMatchExplanation({
    explanation,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-8 shadow-sm">

            <h2 className="text-2xl font-bold">
                🤖 AI Match Analysis
            </h2>

            <p className="mt-5 leading-8 text-slate-700">
                {explanation.summary}
            </p>

            <div className="mt-8 grid gap-8 md:grid-cols-3">

                {/* Strengths */}

                <div>

                    <h3 className="font-semibold text-green-700">
                        ✅ Strengths
                    </h3>

                    <ul className="mt-3 space-y-3 list-disc pl-5">

                        {explanation.strengths.map((item) => (

                            <li key={item}>
                                {item}
                            </li>

                        ))}

                    </ul>

                </div>

                {/* Missing */}

                <div>

                    <h3 className="font-semibold text-red-700">
                        ❌ Missing Skills
                    </h3>

                    <ul className="mt-3 space-y-3 list-disc pl-5">

                        {explanation.missing_skills.map((item) => (

                            <li key={item}>
                                {item}
                            </li>

                        ))}

                    </ul>

                </div>

                {/* Recommendation */}

                <div>

                    <h3 className="font-semibold text-blue-700">
                        💡 Recommendations
                    </h3>

                    <ul className="mt-3 space-y-3 list-disc pl-5">

                        {explanation.recommendations.map((item) => (

                            <li key={item}>
                                {item}
                            </li>

                        ))}

                    </ul>

                </div>

            </div>

        </div>

    );

}