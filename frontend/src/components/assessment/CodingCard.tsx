import { CodingQuestion } from "@/src/types/assessment";

interface Props {
    question: CodingQuestion;
    answer: string;
    onChange: (value: string) => void;
}

export default function CodingCard({
    question,
    answer,
    onChange,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6">

            <h2 className="text-xl font-semibold">
                {question.title}
            </h2>

            <p className="mt-3">
                {question.question}
            </p>

            <textarea
                value={answer}
                onChange={(e) =>
                    onChange(
                        e.target.value
                    )
                }
                rows={14}
                className="mt-6 w-full rounded border p-4 font-mono"
            />

        </div>

    );

}