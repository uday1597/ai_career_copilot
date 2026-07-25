import { MCQ } from "@/src/types/assessment";

interface Props {
    question: MCQ;
    selected: number | null;
    onSelect: (index: number) => void;
}

export default function MCQCard({
    question,
    selected,
    onSelect,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6">

            <h2 className="text-xl font-semibold">
                {question.question}
            </h2>

            <div className="mt-6 space-y-3">

                {question.options.map(
                    (
                        option,
                        index,
                    ) => (

                        <button
                            key={index}
                            onClick={() => onSelect(index)}
                            className={`w-full rounded-lg border p-4 text-left transition

                                ${
                                    selected === index
                                        ? "border-indigo-600 bg-indigo-50"
                                        : "hover:bg-slate-50"
                                }
                            `}
                        >

                            {option}

                        </button>

                    )
                )}

            </div>

        </div>

    );

}