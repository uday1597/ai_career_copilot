"use client";

import { useState } from "react";

import { createJob } from "@/src/services/jobs";

export default function PostJobForm() {

    const [title, setTitle] =
        useState("");

    const [company, setCompany] =
        useState("");

    const [location, setLocation] =
        useState("");

    const [description, setDescription] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    async function handleSubmit(
        e: React.FormEvent
    ) {

        e.preventDefault();

        setLoading(true);

        try {

            await createJob({

                title,

                company,

                location,

                description,

            });

            alert("Job posted successfully.");

            setTitle("");
            setCompany("");
            setLocation("");
            setDescription("");

        }

        catch (err) {

            console.error(err);

            alert("Failed to post job.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <form
            onSubmit={handleSubmit}
            className="rounded-xl border bg-white p-6 shadow-sm space-y-5"
        >

            <h2 className="text-2xl font-bold">

                Post a Job

            </h2>

            <div>

                <label className="mb-2 block font-medium">

                    Job Title

                </label>

                <input
                    value={title}
                    onChange={(e) =>
                        setTitle(
                            e.target.value
                        )
                    }
                    className="w-full rounded-lg border p-3"
                    placeholder="Senior AI Engineer"
                    required
                />

            </div>

            <div>

                <label className="mb-2 block font-medium">

                    Company

                </label>

                <input
                    value={company}
                    onChange={(e) =>
                        setCompany(
                            e.target.value
                        )
                    }
                    className="w-full rounded-lg border p-3"
                    placeholder="Microsoft"
                    required
                />

            </div>

            <div>

                <label className="mb-2 block font-medium">

                    Location

                </label>

                <input
                    value={location}
                    onChange={(e) =>
                        setLocation(
                            e.target.value
                        )
                    }
                    className="w-full rounded-lg border p-3"
                    placeholder="Hyderabad"
                />

            </div>

            <div>

                <label className="mb-2 block font-medium">

                    Job Description

                </label>

                <textarea
                    rows={10}
                    value={description}
                    onChange={(e) =>
                        setDescription(
                            e.target.value
                        )
                    }
                    className="w-full rounded-lg border p-3"
                    placeholder="Paste complete job description..."
                    required
                />

            </div>

            <div className="flex justify-end">

                <button
                    type="submit"
                    disabled={loading}
                    className="rounded-lg bg-indigo-600 px-6 py-3 text-white hover:bg-indigo-700 disabled:opacity-50"
                >

                    {loading
                        ? "Posting..."
                        : "Post Job"}

                </button>

            </div>

        </form>

    );

}