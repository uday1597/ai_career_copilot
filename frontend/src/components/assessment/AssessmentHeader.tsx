interface Props {
    title: string;
    difficulty: string;
    duration: string;
    week: number;
}

export default function AssessmentHeader({
    title,
    difficulty,
    duration,
    week,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h1 className="text-3xl font-bold">
                {title}
            </h1>

            <div className="mt-4 flex gap-6 text-slate-600">

                <span>
                    Week {week}
                </span>

                <span>
                    {difficulty}
                </span>

                <span>
                    {duration}
                </span>

            </div>

        </div>

    );

}