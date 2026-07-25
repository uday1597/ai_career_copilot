"use client";

interface Props {
    score: number;
}

export default function MatchRecommendation({
    score,
}: Props) {

    let message = "";

    if (score >= 90) {

        message =
            "Excellent match! Your resume strongly aligns with the job requirements.";

    } else if (score >= 75) {

        message =
            "Very good match. Improving a few missing skills could make your profile even stronger.";

    } else if (score >= 60) {

        message =
            "Good match. Consider strengthening the missing skills before applying.";

    } else if (score >= 40) {

        message =
            "Fair match. Learning the missing technologies will significantly improve your chances.";

    } else {

        message =
            "Your resume currently has limited overlap with this job. Focus on learning the missing skills before applying.";

    }

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-semibold">
                Recommendation
            </h2>

            <p className="mt-4 leading-7 text-slate-700">
                {message}
            </p>

        </div>

    );

}