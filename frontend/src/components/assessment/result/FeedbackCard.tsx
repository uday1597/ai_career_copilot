interface Props {
    summary: string;
}

export default function FeedbackCard({
    summary,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">

                🤖 AI Feedback

            </h2>

            <p className="mt-4 leading-8 text-slate-600">

                {summary}

            </p>

        </div>

    );

}