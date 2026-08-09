"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import {
    ChevronLeft,
    ChevronRight,
    Plus,
    MessageSquare,
    Target,
    FileText,
    Briefcase,
    Map,
    User,
    Settings,
} from "lucide-react";
import { usePathname } from "next/navigation";
import ThemeToggle from "./ThemeToggle";

const menuItems = [
    {
        name: "Resume Match",
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
        icon: User,
    },
];

const recentChats = [
    "Analyze my resume",
    "What skills am I missing?",
    "Create my learning roadmap",
];

export default function Sidebar() {

    const pathname = usePathname();

    const [collapsed, setCollapsed] = useState(false);

    useEffect(() => {

        const saved =
            localStorage.getItem(
                "sidebar-collapsed"
            );

        if (saved) {
            setCollapsed(
                JSON.parse(saved)
            );
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
            className={`
                flex h-screen flex-col
                bg-slate-900 text-white
                transition-all duration-300
                ${collapsed ? "w-20" : "w-72"}
            `}
        >

           {/* ================================= */}
          {/* HEADER */}
          {/* ================================= */}
          <div
              className="
                  flex
                  h-16
                  items-center
                  border-b
                  border-slate-800
                  px-3
              "
          >
              <Link
                  href="/"
                  className="
                      flex
                      h-9
                      w-9
                      shrink-0
                      items-center
                      justify-center
                      rounded-lg
                      bg-blue-600
                      font-bold
                      text-white
                  "
              >
                  CC
              </Link>

              {!collapsed && (
                  <div className="ml-3 min-w-0">
                      <div className="truncate font-semibold">
                          Career Copilot
                      </div>

                      <div className="truncate text-xs text-slate-400">
                          AI Career Assistant
                      </div>
                  </div>
              )}
          </div>


            {/* ================================= */}
            {/* NEW CHAT */}
            {/* ================================= */}

            <div className="px-3 pt-4">

                <Link
                    href="/"
                    title={
                        collapsed
                            ? "New Chat"
                            : undefined
                    }
                    className={`
                        flex items-center
                        rounded-lg
                        bg-blue-600
                        px-3 py-3
                        font-medium
                        transition
                        hover:bg-blue-500
                        ${collapsed
                            ? "justify-center"
                            : "gap-3"
                        }
                    `}
                >

                    <Plus
                        size={20}
                        className="shrink-0"
                    />

                    {!collapsed && (
                        <span>
                            New Chat
                        </span>
                    )}

                </Link>

            </div>


            {/* ================================= */}
            {/* RECENT CHATS */}
            {/* ================================= */}

            {!collapsed && (

                <div className="px-3 pt-6">

                    <div className="mb-2 px-2 text-xs font-semibold uppercase tracking-wider text-slate-500">
                        Recent Chats
                    </div>

                    <div className="space-y-1">

                        {recentChats.map(
                            (chat) => (

                                <button
                                    key={chat}
                                    className="
                                        flex w-full
                                        items-center gap-3
                                        rounded-lg
                                        px-3 py-2.5
                                        text-left text-sm
                                        text-slate-300
                                        transition
                                        hover:bg-slate-800
                                        hover:text-white
                                    "
                                >

                                    <MessageSquare
                                        size={16}
                                        className="shrink-0 text-slate-500"
                                    />

                                    <span className="truncate">
                                        {chat}
                                    </span>

                                </button>

                            )
                        )}

                    </div>

                </div>

            )}


            {/* ================================= */}
            {/* NAVIGATION */}
            {/* ================================= */}

            <nav className="flex-1 overflow-y-auto p-3">

                {!collapsed && (

                    <div className="mb-2 px-2 text-xs font-semibold uppercase tracking-wider text-slate-500">
                        Career Copilot
                    </div>

                )}

                <div className="space-y-1">

                    {menuItems.map(
                        (item) => {

                            const Icon =
                                item.icon;

                            const active =
                                pathname ===
                                item.href;

                            return (

                                <Link
                                    key={item.name}
                                    href={item.href}
                                    title={
                                        collapsed
                                            ? item.name
                                            : undefined
                                    }
                                    className={`
                                        flex items-center
                                        rounded-lg
                                        px-3 py-3
                                        transition

                                        ${collapsed
                                            ? "justify-center"
                                            : "gap-3"
                                        }

                                        ${
                                            active
                                                ? "bg-blue-600 text-white"
                                                : "text-slate-300 hover:bg-slate-800 hover:text-white"
                                        }
                                    `}
                                >

                                    <Icon
                                        size={20}
                                        className="shrink-0"
                                    />

                                    {!collapsed && (
                                        <span>
                                            {item.name}
                                        </span>
                                    )}

                                </Link>

                            );

                        }
                    )}

                </div>

            </nav>


            {/* ================================= */}
            {/* SETTINGS */}
            {/* ================================= */}

            {/* <div className="border-t border-slate-800 p-3">

                <Link
                    href="/settings"
                    title={
                        collapsed
                            ? "Settings"
                            : undefined
                    }
                    className={`
                        flex items-center
                        rounded-lg
                        px-3 py-3
                        text-slate-300
                        transition
                        hover:bg-slate-800
                        hover:text-white
                        ${collapsed
                            ? "justify-center"
                            : "gap-3"
                        }
                    `}
                >

                    <Settings
                        size={20}
                        className="shrink-0"
                    />

                    {!collapsed && (
                        <span>
                            Settings
                        </span>
                    )}

                </Link>

            </div> */}

            {/* BOTTOM CONTROLS */}
            <div className="border-t border-slate-800 pt-6 px-3 pb-3">

            {/* Theme */}
            <div
                className={`
                    flex items-center
                    ${collapsed
                        ? "justify-center"
                        : "justify-between"
                    }
                `}
            >
                {!collapsed && (
                    <span className="text-sm text-slate-400">
                        Theme
                    </span>
                )}

                <ThemeToggle />
            </div>

            {/* Collapse */}
            <button
                onClick={toggleSidebar}
                className={`
                    mt-2
                    flex
                    w-full
                    items-center
                    rounded-lg
                    p-2
                    text-slate-400 dark:text-slate-500
                    transition
                    hover:bg-slate-800
                    hover:text-white

                    ${collapsed
                        ? "justify-center"
                        : "justify-center"
                    }
                `}
                title={
                    collapsed
                        ? "Expand sidebar"
                        : "Collapse sidebar"
                }
            >
                {collapsed ? (
                    <ChevronRight size={20} />
                ) : (
                    <ChevronLeft size={20} />
                )}
            </button>

            </div>

        </aside>
    );
}