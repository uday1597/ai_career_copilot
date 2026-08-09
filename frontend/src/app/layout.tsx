import "./global.css";

import { ThemeProvider } from "../components/providers/theme-provider";
import { ResumeProvider } from "../context/ResumeContext";
import { MatchProvider } from "../context/MatchContext";
import AppLayout from "@/src/components/layout/AppLayout";

export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="en" suppressHydrationWarning>
            <body>
                <ThemeProvider>
                    <ResumeProvider>
                        <MatchProvider>
                            <AppLayout>
                                {children}
                            </AppLayout>
                        </MatchProvider>
                    </ResumeProvider>
                </ThemeProvider>
            </body>
        </html>
    );
}