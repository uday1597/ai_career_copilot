import { LearningRoadmap } from "../../types/roadMap";
import TopicCard from "./TopicCard";
import {
    AssessmentHistory,
} from "@/src/types/assessmentHistory";

interface Props {

    roadmap: LearningRoadmap;

    history: AssessmentHistory[];

    onTakeAssessment: (
        week: number
    ) => void;

}

export default function LearningTimeline({

    roadmap,

    history,

    onTakeAssessment,

}: Props) {

    return (

        <div className="space-y-6">

            {roadmap.weeks.map((week) => {

                const assessment =
                    history.find(
                        h => h.week === week.week
                    );

                return (

                    <TopicCard

                        key={week.week}

                        week={week}

                        assessment={assessment}

                        onTakeAssessment={
                            onTakeAssessment
                        }

                    />

                );

            })}

        </div>

    );

}