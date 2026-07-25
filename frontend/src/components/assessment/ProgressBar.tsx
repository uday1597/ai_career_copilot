interface Props {
    current: number;
    total: number;
}

export default function ProgressBar({
    current,
    total,
}: Props) {

    const percentage = (current / total) * 100;

    return (

        <div>

            <div className="mb-2 flex justify-between text-sm">

                <span>
                    Question {current} / {total}
                </span>

                <span>
                    {Math.round(percentage)}%
                </span>

            </div>

            <div className="h-3 rounded bg-slate-200">

                <div
                    className="h-3 rounded bg-indigo-600 transition-all"
                    style={{
                        width: `${percentage}%`,
                    }}
                />

            </div>

        </div>

    );

}