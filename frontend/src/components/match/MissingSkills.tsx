"use client";

interface Props {
    skills: string[];
}

export default function MissingSkills({
    skills,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-semibold text-red-700">
                Missing Skills
            </h2>

            <div className="mt-4 flex flex-wrap gap-3">

                {skills.length === 0 && (

                    <p className="text-green-600">
                        No missing skills 🎉
                    </p>

                )}

                {skills.map(skill => (

                    <span
                        key={skill}
                        className="rounded-full bg-red-100 px-4 py-2 text-red-700"
                    >
                        ✗ {skill}
                    </span>

                ))}

            </div>

        </div>

    );

}