'use client';

import { useEffect, useState } from "react"

import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from "@/components/ui/card"

interface PlotInfo {
  occupancy: string
  timeData: Record<string, string>
  time: string
}

export default function HomePage() {
  const [plotInfo, setPlotInfo] = useState<PlotInfo | null>(null)

  useEffect(() => {
    fetch("http://localhost:5000/api/info")
      .then(res => res.json())
      .then(data => setPlotInfo(data))
      .catch(err => console.error("Failed to fetch plot info:", err))
  }, [])

  if (!plotInfo) return <p className="text-center mt-10">Loading...</p>

  return (
    <main className="flex items-center justify-center min-h-screen bg-gray-100 p-4">
      <Card className="w-full max-w-2x1 shadow-xl border">
        <CardHeader>
          <CardTitle className="text-center text-xl">Arc Occupancy</CardTitle>
        </CardHeader>
        <CardContent className="flex flex-col items-center space-y-4">
          <img
            src="http://localhost:5000/static/images/plot.png"
            alt="Matplotlib Plot"
            className="w-full max-h-[600px] object-contain"
            />
          <p className="text-sm text-muted-foreground text-center">
            Current occupancy: <strong>{plotInfo.occupancy}</strong><br />
            Time: <span className="italic">{plotInfo.time}</span>
          </p>
          <div className="w-full mt-4">
            <h3 className="text-sm font-semibold mb-1">History</h3>
            <div className="space-y-1 max-h-40 overflow-y-auto pr-2">
              {Object.entries(plotInfo.timeData).map(([time, occ]) => (
                <p key={time} className="text-sm text-muted-foreground">
                  {time}: {occ}
                </p>
              ))}
            </div>
          </div>
        </CardContent>
      </Card>
    </main>
  )
}

