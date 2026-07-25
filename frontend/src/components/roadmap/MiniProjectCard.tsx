interface Props {
    project: string;
}

export default function MiniProjectCard({
    project,
}: Props) {

    return (

        <div className="rounded-lg border p-4">

            <h3 className="font-semibold text-slate-800">
                Mini Project
            </h3>

            <p className="mt-2 text-slate-600">
                {project}
            </p>

        </div>

    );

}