interface Props{
    score:number;
}

export default function RoadmapHeader({
    score,
}:Props){

    return(

        <div className="rounded-xl border bg-white p-6">

            <h1 className="text-3xl font-bold">
                Personalized Learning Roadmap
            </h1>

            <p className="mt-2 text-slate-600">

                Based on your
                {" "}
                {score}%
                {" "}
                match analysis.

            </p>

        </div>

    );

}