interface Props {
    resources: string[];
}

export default function ResourceCard({
    resources,
}: Props) {

    return (

        <div className="rounded-lg border p-4">

            <h3 className="font-semibold text-slate-800">
                Resources
            </h3>

            <ul className="mt-2 space-y-2">

                {resources.map((resource) => (

                    <li
                        key={resource}
                        className="text-slate-600"
                    >
                        📚 {resource}
                    </li>

                ))}

            </ul>

        </div>

    );

}