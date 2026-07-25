interface Props {
    weaknesses: string[];
}

export default function WeaknessCard({
    weaknesses,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">
                📚 Areas to Improve
            </h2>

            <ul className="mt-5 space-y-3">

                {weaknesses.map((item) => (

                    <li
                        key={item}
                        className="rounded-lg bg-red-50 p-3"
                    >

                        ⚠ {item}

                    </li>

                ))}

            </ul>

        </div>

    );

}