import { ScenarioQuestion } from "@/src/types/assessment";

interface Props {
    question: ScenarioQuestion;
    answer: string;
    onChange: (value: string) => void;
}

export default function ScenarioCard({
    question,
    answer,
    onChange,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6">

            <h2 className="text-xl font-semibold">
                Scenario
            </h2>

            <p className="mt-4">
                {question.question}
            </p>

            <textarea
                value={answer}
                onChange={(e) =>
                    onChange(
                        e.target.value
                    )
                }
                rows={10}
                className="mt-6 w-full rounded border p-4"
            />

        </div>

    );

}