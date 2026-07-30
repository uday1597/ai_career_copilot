import { ProfileSummary } from "../../types/profile";

interface Props {
    profile: ProfileSummary;
}

export default function HeroCard({ profile }: Props) {
    return (
        <div className="relative overflow-hidden rounded-3xl border border-gray-200 bg-white p-8 shadow-lg">
            <div className="flex items-center gap-5">
                <div className="flex h-20 w-20 items-center justify-center rounded-full bg-indigo-100 text-3xl font-bold text-indigo-700">
                    {profile.resume_filename.charAt(0).toUpperCase()}
                </div>

                <div>
                    <h2 className="text-2xl font-bold text-gray-900">
                        Career Profile
                    </h2>

                    <p className="text-gray-600">
                        {profile.resume_filename}
                    </p>

                    <p className="mt-2 text-sm text-gray-500">
                        Uploaded{" "}
                        {profile.resume_uploaded_at
                            ? new Date(
                                  profile.resume_uploaded_at
                              ).toLocaleDateString()
                            : "-"}
                    </p>
                </div>
            </div>

            <div className="mt-8">
                <h3 className="mb-2 font-semibold text-gray-900">
                    Professional Summary
                </h3>

                <p className="leading-7 text-gray-700">
                    {profile.summary}
                </p>
            </div>

            <div className="mt-8">
                <h3 className="mb-3 font-semibold text-gray-900">
                    Skills
                </h3>

                <div className="flex flex-wrap gap-3">
                    {profile.skills.map((skill) => (
                        <span
                            key={skill}
                            className="
                                rounded-full
                                border
                                border-indigo-100
                                bg-indigo-50
                                px-4
                                py-2
                                text-sm
                                font-medium
                                text-indigo-700
                                transition
                                duration-200
                                hover:bg-indigo-100
                                hover:scale-105
                            "
                        >
                            {skill}
                        </span>
                    ))}
                </div>
            </div>
        </div>
    );
}