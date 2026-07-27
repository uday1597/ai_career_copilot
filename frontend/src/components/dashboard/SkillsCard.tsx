import { SkillSummary } from "@/src/types/dashboard";

interface Props {

    skills: SkillSummary;

}

export default function SkillsCard({

    skills,

}: Props) {

    return (

        <div className="rounded-xl border bg-white p-6 shadow-sm">

            <h2 className="text-xl font-bold">

                Skills Overview

            </h2>

            <div className="mt-6">

                <h3 className="font-semibold">

                    Strongest Skills

                </h3>

                <div className="mt-2 flex flex-wrap gap-2">

                    {skills.strongest.map(skill => (

                        <span
                            key={skill}
                            className="rounded-full bg-green-100 px-3 py-1 text-sm text-green-700"
                        >

                            {skill}

                        </span>

                    ))}

                </div>

            </div>

            <div className="mt-6">

                <h3 className="font-semibold">

                    Skills to Improve

                </h3>

                <div className="mt-2 flex flex-wrap gap-2">

                    {skills.weakest.map(skill => (

                        <span
                            key={skill}
                            className="rounded-full bg-red-100 px-3 py-1 text-sm text-red-700"
                        >

                            {skill}

                        </span>

                    ))}

                </div>

            </div>

        </div>

    );

}