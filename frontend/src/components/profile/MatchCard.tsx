import { LatestMatch } from "../../types/profile";

interface Props {
    match: LatestMatch | null;
}

export default function LatestMatchCard({ match }: Props) {

    if (!match) {

        return (
            <div className="rounded-xl bg-white p-6 shadow">
                <h2 className="text-xl font-semibold">
                    Latest Match
                </h2>

                <p className="mt-4 text-gray-500">
                    No match generated yet.
                </p>
            </div>
        );

    }

    return (

        <div className="rounded-xl bg-white p-6 shadow">

            <div className="flex justify-between items-center">

                <div>

                    <h2 className="text-xl font-semibold">
                        Latest Match
                    </h2>

                    <p className="text-gray-500 mt-1">
                        {match.company}
                    </p>

                    <h3 className="text-lg font-bold mt-2">
                        {match.job_title}
                    </h3>

                </div>

                <div className="text-center">

                    <div className="h-28 w-28 rounded-full border-[10px] border-blue-500 flex items-center justify-center">

                        <span className="text-3xl font-bold text-blue-600">
                            {Math.round(match.match_score)}%
                        </span>

                    </div>

                </div>

            </div>

            <div className="mt-8">

                <h4 className="font-semibold mb-3">
                    Missing Skills
                </h4>

                <div className="flex flex-wrap gap-2">

                    {match.missing_skills.length === 0 ? (

                        <span className="text-green-600">
                            No missing skills 🎉
                        </span>

                    ) : (

                        match.missing_skills.map(skill => (

                            <span
                                key={skill}
                                className="rounded-full bg-red-100 text-red-700 px-3 py-1 text-sm"
                            >
                                {skill}
                            </span>

                        ))

                    )}

                </div>

            </div>

        </div>

    );

}