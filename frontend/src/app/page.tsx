'use client';

import { useEffect, useState } from "react";

import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from "@/components/ui/card";

interface PlotInfo {
  occupancy: string;
  timeData: Record<string, string>;
  time: string;
  bestTime: string;
}

export default function HomePage() {
  const [plotInfo, setPlotInfo] = useState<PlotInfo | null>(null);

  useEffect(() => {
    fetch("http://localhost:5000/api/info")
      .then(res => res.json())
      .then(data => setPlotInfo(data))
      .catch(err => console.error("Failed to fetch plot info:", err));
  }, []);

  if (!plotInfo) return <p className="text-center mt-10">Loading...</p>;

  return (
    <main className="flex items-center justify-center min-h-screen bg-gray-100 p-4">
      {/* Container for the three cards */}
      <div className="flex flex-col md:flex-row gap-4 w-full max-w-6xl">
        {/* Left Card: Current occupancy and time (smaller card) */}
        <Card className="w-full md:w-1/4 bg-[#002855] text-[#FFD100] shadow-xl border">
          <CardHeader>
            <CardTitle className="text-center text-xl">
              Current Status
            </CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col items-center space-y-4 p-4">
            <p className="text-lg">
              Current occupancy: <strong>{plotInfo.occupancy}</strong>
            </p>
            <p className="text-lg">
              Time: <span className="italic">{plotInfo.time}</span>
            </p>
          </CardContent>
        </Card>

        {/* Center Card: Graph (bigger card) */}
        <Card className="w-full md:w-1/2 shadow-xl border">
          <CardHeader>
            <CardTitle className="text-center text-xl">Graph</CardTitle>
          </CardHeader>
          <CardContent className="p-4">
            <img
              src="http://localhost:5000/static/images/plot.png"
              alt="Matplotlib Plot"
              className="w-full max-h-[600px] object-contain"
            />
          </CardContent>
        </Card>

        {/* Right Card: Best Time to Visit (smaller card) */}
        <Card className="w-full md:w-1/4 bg-[#002855] text-[#FFD100] shadow-xl border">
          <CardHeader>
            <CardTitle className="text-center text-xl">
              Best Time to Visit
            </CardTitle>
          </CardHeader>
          <CardContent className="flex flex-col items-center justify-center p-4">
            <p className="text-2xl font-bold">{plotInfo.bestTime}</p>
          </CardContent>
        </Card>
      </div>
    </main>
  );
}
