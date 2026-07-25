"use client";

interface Props {

    onSearch: () => void;

}

export default function JobSearch({

    onSearch

}: Props) {

    return (

        <button

            onClick={onSearch}

            className="rounded bg-blue-600 px-5 py-3 text-white"

        >

            Discover Jobs

        </button>

    );

}