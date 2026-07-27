"use client";

import Link from "next/link";

const menuItems = [
  { name: "Dashboard", href: "/" },
  { name: "Match", href: "/match"},
  { name: "Resume", href: "/resume" },
  { name: "Jobs", href: "/jobs" },
  { name: "Roadmap", href: "/roadmap" },
  { name: "Settings", href: "/settings" },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 text-white h-screen p-6">
      <h1 className="text-2xl font-bold mb-8">
        Career Copilot
      </h1>

      <nav className="space-y-3">
        {menuItems.map((item) => (
          <Link
            key={item.name}
            href={item.href}
            className="block rounded-lg px-3 py-2 hover:bg-slate-700 transition"
          >
            {item.name}
          </Link>
        ))}
      </nav>
    </aside>
  );
}