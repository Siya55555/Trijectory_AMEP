import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AMEP - Adaptive Mastery & Engagement Platform",
  description: "Unified educational technology platform for modern classrooms",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
