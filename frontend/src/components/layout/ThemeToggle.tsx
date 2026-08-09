"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export default function ThemeToggle() {
    const { theme, setTheme } = useTheme();
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    if (!mounted) {
        return null;
    }

    const dark = theme === "dark";

    return (
        <button
            type="button"
            onClick={() =>
                setTheme(dark ? "light" : "dark")
            }
            className="
                rounded-lg
                p-2
                text-slate-600
                hover:bg-slate-100
                dark:text-slate-300
                dark:hover:bg-slate-800
            "
        >
            {dark ? (
                <Sun size={20} />
            ) : (
                <Moon size={20} />
            )}
        </button>
    );
}