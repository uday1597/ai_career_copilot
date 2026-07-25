"use client";

interface Props {
    skills: string[];
}

export default function MatchingSkills({
    skills,
}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-semibold text-green-700">
                Matching Skills
            </h2>

            <div className="mt-4 flex flex-wrap gap-3">

                {skills.length === 0 && (

                    <p className="text-slate-500">
                        No matching skills found.
                    </p>

                )}

                {skills.map(skill => (

                    <span
                        key={skill}
                        className="rounded-full bg-green-100 px-4 py-2 text-green-700"
                    >
                        ✓ {skill}
                    </span>

                ))}

            </div>

        </div>

    );

}