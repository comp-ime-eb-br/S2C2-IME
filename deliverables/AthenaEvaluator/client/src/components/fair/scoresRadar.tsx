"use client";
import React from "react";
import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  ResponsiveContainer,
} from "recharts";
// Update the import path and member name to match your actual export
import type { PolarParam } from "@/app/analyze/util";

// user-facing labels (EN)
const LABELS: Record<PolarParam, string> = {
  f1: "F1",
  f2: "F2",
  f3: "F3",
  f4: "F4",
  a11: "A1",
  a2: "A2",
  i1: "I1",
  i2: "I2",
  i3: "I3",
  r11: "R1",
  anonymization: "Anonymization",
  availability: "Availability",
  labeling: "Labeling",
  timeliness: "Timeliness",
  relevance: "Relevance",
  attackDiversity: "Attack Diversity",
  networkConfigurationCompleteness: "Network Config.",
  normalAndAttackTraffic: "Normal + Attack",
};

type Props = {
  scoresByParam: Record<PolarParam, number | null>;
  /** show only a subset? if not provided, use all */
  params?: PolarParam[];
  /** chart height inside the card */
  height?: number;
};

export default function ScoresRadar({
  scoresByParam,
  params,
  height = 220,
}: Props) {
  const keys =
    params && params.length
      ? params
      : (Object.keys(scoresByParam) as PolarParam[]);

  // only parameters with a value
  const data = keys
    .filter((k) => scoresByParam[k] != null)
    .map((k) => ({ key: k, label: LABELS[k] ?? k, value: scoresByParam[k]! }));

  if (!data.length) {
    return (
      <div className="text-xs text-muted-foreground text-center py-6">
        No scores to display
      </div>
    );
  }

  return (
    <div className="w-full" style={{ height }}>
      <ResponsiveContainer width="100%" height="100%">
        <RadarChart data={data} outerRadius="80%">
          <PolarGrid />
          <PolarAngleAxis dataKey="label" tick={{ fontSize: 10 }} />
          <PolarRadiusAxis
            angle={30}
            domain={[0, 100]}
            tick={{ fontSize: 10 }}
          />
          <Radar name="Score" dataKey="value" fillOpacity={0.35} />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}
