import { AssessmentSummary } from "../../types/profile";

interface Props {
    assessment: AssessmentSummary;
}

export default function AssessmentCard({ assessment }: Props) {

    return (

        <div className="rounded-xl bg-white p-6 shadow">

            <h2 className="text-xl font-semibold">
                Assessment Performance
            </h2>

            <div className="grid grid-cols-3 gap-5 mt-8 text-center">

                <div>

                    <h3 className="text-3xl font-bold">
                        {assessment.completed}
                    </h3>

                    <p className="text-blue-600 text-sm">
                        Completed
                    </p>

                </div>

                <div>

                    <h3 className="text-3xl font-bold text-blue-600">
                        {assessment.average_score}%
                    </h3>

                    <p className="text-gray-500 text-sm">
                        Average
                    </p>

                </div>

                <div>

                    <h3 className="text-3xl font-bold text-green-600">
                        {assessment.highest_score}%
                    </h3>

                    <p className="text-green-600 text-sm">
                        Highest
                    </p>

                </div>

            </div>

        </div>

    );

}