interface Props {
    strengths: string[];
}

export default function StrengthCard({
    strengths,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">
                💪 Strengths
            </h2>

            <ul className="mt-5 space-y-3">

                {strengths.map((item) => (

                    <li
                        key={item}
                        className="rounded-lg bg-green-50 p-3"
                    >

                        ✅ {item}

                    </li>

                ))}

            </ul>

        </div>

    );

}