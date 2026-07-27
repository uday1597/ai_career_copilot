import { AssessmentSummary } from "@/src/types/dashboard";

interface Props {

    assessment: AssessmentSummary;

}

export default function AssessmentSummaryCard({

    assessment,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">

                Assessment Summary

            </h2>

            <div className="mt-6 space-y-3">

                <p>

                    Attempted: {assessment.attempted}

                </p>

                <p>

                    Average Score: {assessment.average_score}%

                </p>

                <p>

                    Best Score: {assessment.best_score}%

                </p>

            </div>

        </div>

    );

}