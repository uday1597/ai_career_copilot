interface TechnologyListProps {
    resume: Resume;
}

import { Resume } from "../../types/resume";

export default function TechnologyList({
    resume,
}: TechnologyListProps) {

    return (

        <div className="rounded-xl bg-white p-6 shadow">

            <h2 className="text-xl font-semibold mb-4">
                Technologies
            </h2>

            <div className="flex flex-wrap gap-2">

                {resume.technologies.map((tech) => (

                    <span
                        key={tech}
                        className="rounded-full bg-slate-200 px-3 py-1"
                    >
                        {tech}
                    </span>

                ))}

            </div>

        </div>

    );

}