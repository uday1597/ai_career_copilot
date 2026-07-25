interface Props {

    score: number;

    feedback: any;

}

export default function AssessmentResult({

    score,

    feedback,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-3xl font-bold">

                Overall Score

            </h2>

            <p className="mt-4 text-6xl font-bold text-indigo-600">

                {score}%

            </p>

            {feedback && (

                <div className="mt-8 space-y-4">

                    <div>

                        <h3 className="font-semibold">

                            Strengths

                        </h3>

                        <ul className="mt-2 list-disc pl-6">

                            {feedback.strengths?.map(

                                (item: string) => (

                                    <li key={item}>

                                        {item}

                                    </li>

                                )

                            )}

                        </ul>

                    </div>

                    <div>

                        <h3 className="font-semibold">

                            Recommendations

                        </h3>

                        <ul className="mt-2 list-disc pl-6">

                            {feedback.recommendations?.map(

                                (item: string) => (

                                    <li key={item}>

                                        {item}

                                    </li>

                                )

                            )}

                        </ul>

                    </div>

                </div>

            )}

        </div>

    );

}