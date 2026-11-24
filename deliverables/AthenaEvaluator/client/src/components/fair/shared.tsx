"use client";
import React from "react";
import Link from "next/link";
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Box from "@mui/material/Box";
import Chip from "@mui/material/Chip";
import Button from "@mui/material/Button";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
// components/fair/shared/DatasetCard.tsx
import ScoresRadar from "./scoresRadar";
import { UiRow } from "@/app/analyze/util"; // ajuste o path
// import TextField from "@mui/material/TextField";
import Dialog from "@mui/material/Dialog";
import DialogContent from "@mui/material/DialogContent";
import DialogTitle from "@mui/material/DialogTitle";
import IconButton from "@mui/material/IconButton";
import CloseIcon from "@mui/icons-material/Close";
import {
  ResponsiveContainer,
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  BarChart,
  CartesianGrid,
  XAxis,
  YAxis,
  Bar,
} from "recharts";
import ArrowForwardIcon from "@mui/icons-material/ArrowForward";
import { CardActions } from "@mui/material";

export type FairPrinciple = "A" | "F" | "I" | "R";

export type DatasetEvaluation = {
  id: string;
  title: string;
  doi?: string;
  uri?: string;
  sourceUrl?: string;
  overallScore: number; // 0..100
  principleScores: Record<FairPrinciple, number>; // each 0..100
  tags?: string[];
};

export const ATTRIBUTE_NAMES = [
  "Timeliness",
  "Public Availability",
  "Normal and Attack Traffic",
  "Metadata",
  "Anonymity",
  "Complete Network",
  "Labeled",
  "Findable",
  "Accessible",
  "Interoperable",
  "Reusable",
] as const;

export const MOCK_DATASET_ATTRIBUTES: Record<
  string,
  { name: string; value: number }[]
> = {
  "ctu-13": [
    { name: "Timeliness", value: 82 },
    { name: "Public Availability", value: 90 },
    { name: "Normal and Attack Traffic", value: 76 },
    { name: "Metadata", value: 64 },
    { name: "Anonymity", value: 58 },
    { name: "Complete Network", value: 70 },
    { name: "Labeled", value: 73 },
    { name: "Findable", value: 80 },
    { name: "Accessible", value: 77 },
    { name: "Interoperable", value: 62 },
    { name: "Reusable", value: 68 },
  ],
  "unsw-nb15": [
    { name: "Timeliness", value: 74 },
    { name: "Public Availability", value: 85 },
    { name: "Normal and Attack Traffic", value: 71 },
    { name: "Metadata", value: 60 },
    { name: "Anonymity", value: 66 },
    { name: "Complete Network", value: 63 },
    { name: "Labeled", value: 69 },
    { name: "Findable", value: 72 },
    { name: "Accessible", value: 70 },
    { name: "Interoperable", value: 58 },
    { name: "Reusable", value: 61 },
  ],
  kddcup99: [
    { name: "Timeliness", value: 45 },
    { name: "Public Availability", value: 60 },
    { name: "Normal and Attack Traffic", value: 52 },
    { name: "Metadata", value: 40 },
    { name: "Anonymity", value: 54 },
    { name: "Complete Network", value: 47 },
    { name: "Labeled", value: 50 },
    { name: "Findable", value: 55 },
    { name: "Accessible", value: 57 },
    { name: "Interoperable", value: 42 },
    { name: "Reusable", value: 46 },
  ],
};

export const MOCK_DATASETS: DatasetEvaluation[] = [
  {
    id: "ctu-13",
    title: "CTU-13 Network Intrusion Dataset",
    doi: "10.5281/zenodo.1234567",
    sourceUrl: "https://example.org/ctu-13",
    overallScore: 72,
    principleScores: { A: 65, F: 78, I: 70, R: 75 },
    tags: ["network", "security", "traffic"],
  },
  {
    id: "unsw-nb15",
    title: "UNSW-NB15 Security Dataset",
    doi: "10.5281/zenodo.7654321",
    sourceUrl: "https://example.org/unsw-nb15",
    overallScore: 61,
    principleScores: { A: 55, F: 66, I: 60, R: 63 },
    tags: ["security", "benchmark"],
  },
  {
    id: "kddcup99",
    title: "KDDCup'99",
    overallScore: 48,
    principleScores: { A: 40, F: 58, I: 41, R: 52 },
    tags: ["legacy"],
  },
];

export function Header() {
  return (
    <AppBar
      position="sticky"
      color="default"
      elevation={0}
      sx={{
        borderBottom: 1,
        borderColor: "divider",
        bgcolor: "background.paper",
      }}>
      <Toolbar sx={{ maxWidth: 1200, mx: "auto", width: "100%" }}>
        <Box sx={{ display: "flex", alignItems: "center", gap: 1 }}>
          <Box
            sx={{
              width: 24,
              height: 24,
              bgcolor: "primary.main",
              borderRadius: 1,
            }}
          />
          <Typography variant="subtitle1" fontWeight={600}>
            Athena Evaluator
          </Typography>
          <Chip size="small" label="FAIR" variant="outlined" sx={{ ml: 1 }} />
        </Box>
        <Box sx={{ ml: "auto", display: { xs: "none", md: "flex" }, gap: 2 }}>
          <Button component={Link} href="/" color="inherit">
            Home
          </Button>
          <Button component={Link} href="/evaluate" color="inherit">
            Evaluate
          </Button>
          <Button component={Link} href="/analyze" color="inherit">
            Analyze
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
}

export function HubCard({
  icon,
  title,
  description,
  href,
  ctaLabel,
}: {
  icon: React.ReactNode;
  title: string;
  description: string;
  href: string;
  ctaLabel: string;
}) {
  return (
    <Card
      sx={{ borderRadius: 3, position: "relative", overflow: "hidden", p: 1 }}>
      <CardHeader
        avatar={
          <Box
            sx={{
              p: 1,
              borderRadius: 3,
              bgcolor: "primary.main",
              color: "primary.contrastText",
              display: "flex",
            }}>
            {icon}
          </Box>
        }
        title={<Typography variant="h6">{title}</Typography>}
        subheader={
          <Typography variant="body2" color="text.secondary">
            {description}
          </Typography>
        }
      />
      <CardContent sx={{ pt: 0 }}>
        <Button
          component={Link}
          href={href}
          variant="contained"
          endIcon={<ArrowForwardIcon fontSize="small" />}>
          {ctaLabel}
        </Button>
      </CardContent>
    </Card>
  );
}

export function QuickActions() {
  const [openPdf, setOpenPdf] = React.useState(false);

  // Dica: coloque o PDF em /public/docs/general-specific.pdf
  // assim o href abaixo funciona em produção: /docs/general-specific.pdf
  const pdfHref = "/docs/general-specific.pdf";

  return (
    <div className="mt-6 grid gap-4 md:grid-cols-2">
      {/* 1) What are the FAIR Principles? (GO FAIR) */}
      <Card sx={{ borderRadius: 2 }}>
        <CardContent>
          <Typography variant="subtitle1">
            What are the FAIR Principles?
          </Typography>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
            Official description from GO FAIR
          </Typography>

          <Button
            variant="text"
            fullWidth
            component="a"
            href="https://www.go-fair.org/fair-principles/"
            target="_blank"
            rel="noreferrer">
            Open GO FAIR page
          </Button>
        </CardContent>
      </Card>

      {/* 2) Details of general and specific criteria (abre PDF) */}
      <Card sx={{ borderRadius: 2 }}>
        <CardContent>
          <Typography variant="subtitle1">
            Details of general and specific criteria
          </Typography>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
            Full explanation used in our evaluation
          </Typography>

          {/* Opção A: abrir num diálogo dentro do app */}
          <Button
            variant="contained"
            fullWidth
            onClick={() => setOpenPdf(true)}>
            Open inside the app
          </Button>

          {/* Opção B: abrir em uma nova aba (download/viewer do navegador) */}
          <Button
            sx={{ mt: 1 }}
            variant="text"
            fullWidth
            component="a"
            href={pdfHref}
            target="_blank"
            rel="noreferrer">
            Open in a new tab
          </Button>
        </CardContent>
      </Card>

      {/* Dialog com o PDF embutido */}
      <Dialog
        open={openPdf}
        onClose={() => setOpenPdf(false)}
        maxWidth="lg"
        fullWidth
        PaperProps={{ sx: { height: { xs: "90dvh", md: "85dvh" } } }}>
        <DialogTitle sx={{ pr: 6 }}>
          General and Specific Criteria
          <IconButton
            aria-label="close"
            onClick={() => setOpenPdf(false)}
            sx={{ position: "absolute", right: 8, top: 8 }}>
            <CloseIcon />
          </IconButton>
        </DialogTitle>

        <DialogContent dividers sx={{ p: 0 }}>
          {/* <object> costuma ter o melhor suporte com fallback */}
          <object
            data={pdfHref}
            type="application/pdf"
            width="100%"
            height="100%"
            style={{ minHeight: "70dvh" }}>
            <Typography sx={{ p: 2 }}>
              Your browser could not display the PDF.{" "}
              <a href={pdfHref} target="_blank" rel="noreferrer">
                Click here to open/download.
              </a>
            </Typography>
          </object>
        </DialogContent>
      </Dialog>
    </div>
  );
}

export function QuickActions2() {
  return (
    <div className="mt-6 grid gap-4 md:grid-cols-2">
      {/* Kept commented blocks */}
      <Card sx={{ borderRadius: 2 }}>
        <CardContent>
          <Typography variant="subtitle1">Documentation</Typography>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
            How the FAIR metrics work
          </Typography>
          <Button
            variant="text"
            fullWidth
            component="a"
            href="https://www.go-fair.org/fair-principles/"
            target="_blank"
            rel="noreferrer">
            Open the guide
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}

export function DatasetCard3({ data }: { data: DatasetEvaluation }) {
  const fairData = [
    { principle: "A", value: data.principleScores.A },
    { principle: "F", value: data.principleScores.F },
    { principle: "I", value: data.principleScores.I },
    { principle: "R", value: data.principleScores.R },
  ];
  const attrData =
    MOCK_DATASET_ATTRIBUTES[data.id] ||
    ATTRIBUTE_NAMES.map((n) => ({ name: n as string, value: 50 }));

  return (
    <Card sx={{ borderRadius: 3 }}>
      <CardHeader
        title={
          <Typography noWrap variant="subtitle1">
            {data.title}
          </Typography>
        }
        subheader={
          <Box sx={{ display: "flex", alignItems: "center", gap: 1, mt: 0.5 }}>
            {data.doi && (
              <Chip size="small" variant="outlined" label={data.doi} />
            )}
            <ScorePill score={data.overallScore} />
          </Box>
        }
      />
      <CardContent sx={{ display: "grid", gap: 2 }}>
        <Box
          sx={{
            display: "grid",
            gridTemplateColumns: { xs: "1fr", md: "1fr 1fr" },
            gap: 2,
          }}>
          <Box sx={{ height: 160 }}>
            <ResponsiveContainer width="100%" height="100%">
              <RadarChart data={fairData} outerRadius="80%">
                <PolarGrid />
                <PolarAngleAxis dataKey="principle" />
                <PolarRadiusAxis angle={30} domain={[0, 100]} tickCount={6} />
                <Radar dataKey="value" fillOpacity={0.3} />
              </RadarChart>
            </ResponsiveContainer>
          </Box>
          <Box sx={{ height: 160 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={attrData}
                layout="vertical"
                margin={{ left: 0, right: 0, top: 0, bottom: 0 }}>
                <CartesianGrid horizontal={false} />
                <XAxis type="number" domain={[0, 100]} hide />
                <YAxis type="category" dataKey="name" hide />
                <Bar dataKey="value" />
              </BarChart>
            </ResponsiveContainer>
          </Box>
        </Box>
        <Box sx={{ display: "flex", flexWrap: "wrap", gap: 1 }}>
          {(["A", "F", "I", "R"] as FairPrinciple[]).map((p) => (
            <PrincipleBadge key={p} p={p} value={data.principleScores[p]} />
          ))}
        </Box>
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}>
          <Box sx={{ display: "flex", gap: 1 }}>
            <Button
              component={Link}
              href={`/analyze/${data.id}`}
              variant="outlined"
              size="small">
              Details
            </Button>
            {data.sourceUrl && (
              <Button
                href={data.sourceUrl}
                target="_blank"
                rel="noreferrer"
                variant="contained"
                size="small">
                Open source page
              </Button>
            )}
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
}

function getDatasetId(uri: string) {
  return uri.replace(/\/+$/, "").split("/").pop()!;
}

export function DatasetCard({ data }: { data: UiRow }) {
  const evaluated = data.overallScore != 0;
  const id = getDatasetId(data.uri);

  if (!evaluated) {
    return <></>;
  }

  return (
    <Card sx={{ borderRadius: 3, display: "flex", flexDirection: "column" }}>
      <CardContent sx={{ pb: 0 }}>
        <div className="flex items-start justify-between">
          <h3 className="font-medium leading-tight line-clamp-2">
            {data.title}
          </h3>
          <span className="text-xs text-muted-foreground">
            {data.overallScore}%
          </span>
        </div>

        {/* your radar here */}
        {/* <ScoresRadar scoresByParam={data.scoresByParam} /> */}
        <ScoresRadar
          scoresByParam={data.scoresByParam}
          params={[
            "f1",
            "f2",
            "f3",
            "f4",
            "a11",
            "a2",
            "i1",
            "i2",
            "i3",
            "r11",
          ]}
        />
        <ScoresRadar
          scoresByParam={data.scoresByParam}
          params={[
            "anonymization",
            "availability",
            "labeling",
            "timeliness",
            "relevance",
          ]}
        />
        <ScoresRadar
          scoresByParam={data.scoresByParam}
          params={[
            "attackDiversity",
            "networkConfigurationCompleteness",
            "normalAndAttackTraffic",
          ]}
        />
        <div className="grid grid-cols-4 gap-2 text-xs">
          <div>
            F: <b>{data.principleScores.F}%</b>
          </div>
          <div>
            A: <b>{data.principleScores.A}%</b>
          </div>
          <div>
            I: <b>{data.principleScores.I}%</b>
          </div>
          <div>
            R: <b>{data.principleScores.R}%</b>
          </div>
        </div>
      </CardContent>

      <CardActions sx={{ mt: "auto", px: 2, pb: 2 }}>
        <Button
          component={Link}
          href={`/analyze/${encodeURIComponent(id)}`}
          size="small"
          variant="outlined">
          Details
        </Button>
      </CardActions>
    </Card>
  );
}

export function DatasetCard2({ data }: { data: DatasetEvaluation }) {
  const chartData = [
    { principle: "A", value: data.principleScores.A },
    { principle: "F", value: data.principleScores.F },
    { principle: "I", value: data.principleScores.I },
    { principle: "R", value: data.principleScores.R },
  ];

  return (
    <Card sx={{ borderRadius: 3 }}>
      <CardHeader
        title={
          <Typography noWrap variant="subtitle1">
            {data.title}
          </Typography>
        }
        subheader={
          <Box sx={{ display: "flex", alignItems: "center", gap: 1, mt: 0.5 }}>
            {data.doi && (
              <Chip size="small" variant="outlined" label={data.doi} />
            )}
            <ScorePill score={data.overallScore} />
          </Box>
        }
      />
      <CardContent sx={{ display: "grid", gap: 2 }}>
        <Box sx={{ height: 160 }}>
          <ResponsiveContainer width="100%" height="100%">
            <RadarChart data={chartData} outerRadius="80%">
              <PolarGrid />
              <PolarAngleAxis dataKey="principle" />
              <PolarRadiusAxis angle={30} domain={[0, 100]} tickCount={6} />
              <Radar dataKey="value" fillOpacity={0.3} />
            </RadarChart>
          </ResponsiveContainer>
        </Box>
        <Box sx={{ display: "flex", flexWrap: "wrap", gap: 1 }}>
          {(["A", "F", "I", "R"] as FairPrinciple[]).map((p) => (
            <PrincipleBadge key={p} p={p} value={data.principleScores[p]} />
          ))}
        </Box>
        <Box
          sx={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
          }}>
          <Box sx={{ display: "flex", gap: 1 }}>
            <Button
              component={Link}
              href={`/analyze/${data.id}`}
              variant="outlined"
              size="small">
              Details
            </Button>
            {data.sourceUrl && (
              <Button
                href={data.sourceUrl}
                target="_blank"
                rel="noreferrer"
                variant="contained"
                size="small">
                Open source page
              </Button>
            )}
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
}

export function DatasetTable({ rows }: { rows: DatasetEvaluation[] }) {
  return (
    <div className="overflow-x-auto rounded-2xl border bg-card">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b bg-muted/50">
            <th className="px-4 py-3 text-left font-medium">Title</th>
            {/* <th className="px-4 py-3 text-left font-medium">DOI</th> */}
            <th className="px-4 py-3 text-left font-medium">F</th>
            <th className="px-4 py-3 text-left font-medium">A</th>
            <th className="px-4 py-3 text-left font-medium">I</th>
            <th className="px-4 py-3 text-left font-medium">R</th>
            <th className="px-4 py-3 text-left font-medium">Score</th>
            <th className="px-4 py-3 text-left font-medium">Actions</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((d) =>
            d.overallScore == 0 ? null : (
              <tr key={d.id} className="border-b last:border-0">
                <td className="px-4 py-3">
                  <div className="font-medium line-clamp-1">{d.title}</div>
                </td>
                {/* <td className="px-4 py-3">{d.doi ?? "—"}</td> */}
                {(["F", "A", "I", "R"] as FairPrinciple[]).map((p) => (
                  <td key={p} className="px-4 py-3">
                    <MiniBar value={d.principleScores[p]} />
                  </td>
                ))}
                <td className="px-4 py-3">
                  <ScorePill score={d.overallScore} />
                </td>
                <td className="px-4 py-3">
                  <div className="flex gap-2">
                    <Button
                      component={Link}
                      href={`/analyze/${d.id}`}
                      size="small"
                      variant="outlined">
                      View
                    </Button>
                    {/* <Button size="small" variant="contained">
                    Export
                  </Button> */}
                  </div>
                </td>
              </tr>
            ),
          )}
        </tbody>
      </table>
    </div>
  );
}

export function MiniBar({ value }: { value: number }) {
  return (
    <Box
      sx={{ height: 8, width: 80, bgcolor: "action.hover", borderRadius: 1 }}>
      <Box
        sx={{
          height: 8,
          width: `${Math.max(0, Math.min(100, value))}%`,
          bgcolor: "primary.main",
          borderRadius: 1,
        }}
      />
    </Box>
  );
}

export function PrincipleBadge({
  p,
  value,
}: {
  p: FairPrinciple;
  value: number;
}) {
  const map: Record<
    FairPrinciple,
    {
      label: string;
      color: "default" | "primary" | "success" | "info" | "warning" | "error";
    }
  > = {
    A: { label: "A", color: "warning" },
    F: { label: "F", color: "primary" },
    I: { label: "I", color: "success" },
    R: { label: "R", color: "info" },
  };
  return (
    <Chip
      size="small"
      color={map[p].color}
      variant="outlined"
      label={`${map[p].label}: ${value}`}
    />
  );
}

export function ScorePill({ score }: { score: number }) {
  const color: "success" | "warning" | "error" =
    score >= 75 ? "success" : score >= 50 ? "warning" : "error";
  return (
    <Chip
      size="small"
      color={color}
      variant="outlined"
      label={`${score}/100`}
    />
  );
}

export function EvaluatePageShell({
  children,
}: {
  children?: React.ReactNode;
}) {
  return (
    <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
      <Header />
      <section className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </section>
    </main>
  );
}

// ===============================
// Optional: RecentEvaluations component (kept from earlier design)
// ===============================
export function RecentEvaluations() {
  return (
    <div className="mt-12">
      <div className="flex items-center justify-between">
        <h2 className="text-lg font-medium">Recent</h2>
        <Button component={Link} href="/analyze" size="small" variant="text">
          View all
        </Button>
      </div>
      <div className="mt-4 grid gap-4 md:grid-cols-3">
        {MOCK_DATASETS.slice(0, 3).map((d) => {
          // Convert DatasetEvaluation to UiRow with mock scoresByParam
          const PARAMS = [
            // "F",
            // "A",
            // "I",
            // "R",
            "f1",
            "f2",
            "f3",
            "f4",
            "a11",
            "a2",
            "i1",
            "i2",
            "i3",
            "r11",
            "anonymization",
            "availability",
            "labeling",
            "timeliness",
            "relevance",
            "attackDiversity",
            "networkConfigurationCompleteness",
            "normalAndAttackTraffic",
          ] as const;
          const scoresByParam: Record<(typeof PARAMS)[number], number | null> =
            Object.fromEntries(PARAMS.map((p) => [p, null])) as Record<
              (typeof PARAMS)[number],
              number | null
            >;
          const uiRow = {
            ...d,
            uri: d.sourceUrl ?? "",
            scoresByParam,
          };
          return <DatasetCard key={d.id} data={uiRow} />;
        })}
      </div>
    </div>
  );
}
