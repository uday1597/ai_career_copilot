import Sidebar from "./Sidebar";
import Header from "./Header";

export default function AppLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex h-screen">

    <Sidebar />

    <div className="flex flex-1 flex-col">

        <Header />

        <main className="flex-1 overflow-y-auto p-8 bg-slate-50">

            {children}

        </main>

    </div>

</div>
  );
}