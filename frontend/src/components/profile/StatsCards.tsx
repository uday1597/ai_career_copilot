import {
    FileText,
    Briefcase,
    Target,
    BookOpen,
    ClipboardCheck,
} from "lucide-react";

import { CareerStats } from "../../types/profile";

interface Props {
    stats: CareerStats;
}

export default function StatsCards({ stats }: Props) {

    const cards = [

        {
            title: "Resumes",
            value: stats.resumes,
            color: "bg-blue-500",
            icon: FileText,
        },

        {
            title: "Jobs",
            value: stats.jobs,
            color: "bg-green-500",
            icon: Briefcase,
        },

        {
            title: "Matches",
            value: stats.matches,
            color: "bg-violet-500",
            icon: Target,
        },

        {
            title: "Roadmaps",
            value: stats.roadmaps,
            color: "bg-orange-500",
            icon: BookOpen,
        },

        {
            title: "Assessments",
            value: stats.assessments,
            color: "bg-pink-500",
            icon: ClipboardCheck,
        },

    ];

    return (

        <div className="grid grid-cols-2 gap-5 lg:grid-cols-5">

            {cards.map((card) => {

                const Icon = card.icon;

                return (

                    <div
                        key={card.title}
                        className="rounded-2xl bg-white p-6 shadow transition-all duration-300 hover:-translate-y-1 hover:shadow-xl"
                    >

                        <div
                            className={`mb-5 flex h-12 w-12 items-center justify-center rounded-xl ${card.color}`}
                        >
                            <Icon
                                className="h-6 w-6 text-white"
                            />
                        </div>

                        <p className="text-sm font-medium text-slate-500">
                            {card.title}
                        </p>

                        <h2 className="mt-2 text-3xl font-bold text-slate-900">
                            {card.value}
                        </h2>

                    </div>

                );

            })}

        </div>

    );

}