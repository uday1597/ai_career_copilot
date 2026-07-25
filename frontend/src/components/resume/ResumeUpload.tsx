"use client";

import { useRef, useState } from "react";
import { Upload } from "lucide-react";

import { uploadResume } from "../../services/resume";
import { Resume } from "../../types/resume";

interface ResumeUploadProps {
  onUpload: (resume: Resume) => void;
}

export default function ResumeUpload({
  onUpload,
}: ResumeUploadProps) {
  const inputRef = useRef<HTMLInputElement>(null);

  const [loading, setLoading] = useState(false);

  const handleFile = async (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    const file = event.target.files?.[0];

    if (!file) return;

    try {
      setLoading(true);

      const resume = await uploadResume(file);

      onUpload(resume);
    } catch (error) {
      console.error("Resume upload failed", error);
      alert("Failed to upload resume.");
    } finally {
      setLoading(false);

      event.target.value = "";
    }
  };

  return (
    <div className="rounded-xl border-2 border-dashed border-slate-300 bg-white p-10 text-center">
      <Upload className="mx-auto h-12 w-12 text-slate-500" />

      <h2 className="mt-4 text-xl font-semibold">
        Upload Resume
      </h2>

      <p className="mt-2 text-slate-500">
        Drag & Drop your PDF here
      </p>

      <input
        ref={inputRef}
        type="file"
        accept=".pdf"
        hidden
        onChange={handleFile}
      />

      <button
        className="mt-6 rounded-lg bg-slate-900 px-6 py-3 text-white hover:bg-slate-800 disabled:opacity-50"
        disabled={loading}
        onClick={() => inputRef.current?.click()}
      >
        {loading ? "Uploading..." : "Choose File"}
      </button>
    </div>
  );
}