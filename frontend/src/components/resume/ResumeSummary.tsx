interface ResumeSummaryProps {
    resume: Resume;
}

import { Resume } from "../../types/resume";

export default function ResumeSummary({
    resume,
}: ResumeSummaryProps) {

    return (
        <div className="rounded-xl bg-white p-6 shadow">

            <h2 className="text-xl font-semibold mb-4">
                Resume Summary
            </h2>

            <p>{resume.summary}</p>

        </div>
    );

}