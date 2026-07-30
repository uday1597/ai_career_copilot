"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  ChevronLeft,
  ChevronRight,
  LayoutDashboard,
  FileText,
  Briefcase,
  Target,
  Map,
  Settings,
} from "lucide-react";
import { usePathname } from "next/navigation";

const menuItems = [
  {
    name: "Dashboard",
    href: "/",
    icon: LayoutDashboard,
  },
  {
    name: "Match",
    href: "/match",
    icon: Target,
  },
  {
    name: "Resume",
    href: "/resume",
    icon: FileText,
  },
  {
    name: "Jobs",
    href: "/jobs",
    icon: Briefcase,
  },
  {
    name: "Roadmap",
    href: "/roadmap",
    icon: Map,
  },
  {
    name: "Profile",
    href: "/profile",
    icon: Settings,
  },
];

export default function Sidebar() {
  const pathname = usePathname();

  const [collapsed, setCollapsed] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem("sidebar-collapsed");
    if (saved) {
      setCollapsed(JSON.parse(saved));
    }
  }, []);

  const toggleSidebar = () => {
    const next = !collapsed;
    setCollapsed(next);
    localStorage.setItem(
      "sidebar-collapsed",
      JSON.stringify(next)
    );
  };

  return (
    <aside
      className={`bg-slate-900 text-white h-screen transition-all duration-300 flex flex-col ${
        collapsed ? "w-20" : "w-64"
      }`}
    >
      <div className="flex items-center justify-between p-5 border-b border-slate-800">
        {!collapsed && (
          <h1 className="text-xl font-bold whitespace-nowrap">
            Career Copilot
          </h1>
        )}

        <button
          onClick={toggleSidebar}
          className="rounded-md p-2 hover:bg-slate-800 transition"
        >
          {collapsed ? (
            <ChevronRight size={20} />
          ) : (
            <ChevronLeft size={20} />
          )}
        </button>
      </div>

      <nav className="flex-1 p-3 space-y-2">
        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <Link
              key={item.name}
              href={item.href}
              title={collapsed ? item.name : ""}
              className={`flex items-center gap-3 rounded-lg px-3 py-3 transition
                ${
                  pathname === item.href
                    ? "bg-blue-600 text-white"
                    : "hover:bg-slate-800 text-slate-300"
                }`}
            >
              <Icon size={20} className="shrink-0" />

              {!collapsed && (
                <span>{item.name}</span>
              )}
            </Link>
          );
        })}
      </nav>
    </aside>
  );
}