interface Props {

    current: number;

    total: number;

    onPrevious: () => void;

    onNext: () => void;

}

export default function AssessmentNavigation({

    current,

    total,

    onPrevious,

    onNext,

}: Props) {

    return (

        <div className="flex justify-between">

            <button

                onClick={onPrevious}

                disabled={current === 1}

                className="rounded bg-slate-700 px-5 py-2 text-white disabled:opacity-50"

            >

                Previous

            </button>

            <button

                onClick={onNext}

                disabled={current === total}

                className="rounded bg-indigo-600 px-5 py-2 text-white disabled:opacity-50"

            >

                Next

            </button>

        </div>

    );

}