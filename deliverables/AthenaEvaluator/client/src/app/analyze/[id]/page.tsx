// app/analyze/[id]/page.tsx
"use client";

import React from "react";
import { useParams, useRouter } from "next/navigation";
import Link from "next/link";

import { Header, ScorePill } from "@/components/fair/shared";
// no topo do arquivo da página
import { useTheme, alpha } from "@mui/material/styles";

import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Chip from "@mui/material/Chip";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import Slider from "@mui/material/Slider";
import Tooltip from "@mui/material/Tooltip";
import Dialog from "@mui/material/Dialog";
import DialogTitle from "@mui/material/DialogTitle";
import DialogContent from "@mui/material/DialogContent";
import DialogActions from "@mui/material/DialogActions";
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import RestartAltIcon from "@mui/icons-material/RestartAlt";
import CompareArrowsIcon from "@mui/icons-material/CompareArrows";
import CloseIcon from "@mui/icons-material/Close";

import {
  ResponsiveContainer,
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Legend,
  Tooltip as RechartsTooltip,
} from "recharts";

import {
  getDatasetsFromRDF,
  fetchTitlesForDatasets,
  buildUiRowFromDataset,
  type UiRow,
  POLAR_PARAMS,
  type PolarParam,
} from "../util";

// -------------------- Types & consts --------------------

type FairPrinciple = "A" | "F" | "I" | "R";
const PRINCIPLES: FairPrinciple[] = ["A", "F", "I", "R"];

type WeightState = Record<FairPrinciple, number>;
type AttrWeights = Record<PolarParam, number>;

// Groups by subprinciples:
const FAIR_PARAMS: PolarParam[] = [
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
];

const GENERAL_PARAMS: PolarParam[] = [
  "anonymization",
  "availability",
  "labeling",
  "timeliness",
  "relevance",
];

const SPECIFIC_PARAMS: PolarParam[] = [
  "attackDiversity",
  "networkConfigurationCompleteness",
  "normalAndAttackTraffic",
];

// Compact labels
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
  anonymization: "Anonym.",
  availability: "Avail.",
  labeling: "Labeling",
  timeliness: "Timeliness",
  relevance: "Relevance",
  attackDiversity: "Attack Div.",
  networkConfigurationCompleteness: "Net. Conf.",
  normalAndAttackTraffic: "Normal+Attack",
};

// Subprinciple → FAIR principle (apenas os FAIR)
const SUB_TO_PRINCIPLE: Partial<Record<PolarParam, FairPrinciple>> = {
  f1: "F",
  f2: "F",
  f3: "F",
  f4: "F",
  a11: "A",
  a2: "A",
  i1: "I",
  i2: "I",
  i3: "I",
  r11: "R",
} as const;

// -------------------- Helpers --------------------

function normId(u: string) {
  const s = u.replace(/\/+$/, "");
  const i = s.lastIndexOf("/");
  return i >= 0 ? s.slice(i + 1) : s;
}

function sameResource(a: string, b: string) {
  return a.replace(/\/+$/, "") === b.replace(/\/+$/, "");
}

function titleMatches(d: UiRow, q: string) {
  const term = q.trim().toLowerCase();
  if (!term) return true;
  return (
    d.title.toLowerCase().includes(term) || d.uri.toLowerCase().includes(term)
  );
}

function makeRadarData(
  params: PolarParam[],
  a: Record<PolarParam, number | null>,
  b?: Record<PolarParam, number | null> | null,
) {
  return params
    .map((p) => ({
      name: LABELS[p] ?? p,
      a: a[p] ?? undefined,
      b: b ? (b[p] ?? undefined) : undefined,
    }))
    .filter((d) => d.a != null || d.b != null);
}

// Fallback to avoid hook conditionals
const EMPTY_SCORES = Object.fromEntries(
  POLAR_PARAMS.map((p) => [p, null as number | null]),
) as Record<PolarParam, number | null>;

// -------------------- Page --------------------

export default function Page() {
  const params = useParams<{ id: string }>();
  const router = useRouter();

  const theme = useTheme();
  const primaryStroke = alpha(theme.palette.primary.main, 0.9);
  const primaryFill = alpha(theme.palette.primary.main, 0.28);

  const compareStroke = alpha(theme.palette.secondary.main, 0.9);
  const compareFill = alpha(theme.palette.secondary.main, 0.22);

  // Base state: real dataset list (like analyze)
  const [rows, setRows] = React.useState<UiRow[]>([]);
  const [loading, setLoading] = React.useState(true);
  const [loadError, setLoadError] = React.useState<string | null>(null);

  // FAIR weights
  // const [weights] = React.useState<WeightState>({
  //   A: 25,
  //   F: 25,
  //   I: 25,
  //   R: 25,
  // });

  // // Subprinciple (attribute) weights
  // const [attrWeights, setAttrWeights] = React.useState<AttrWeights>(() => {
  //   const base: AttrWeights = {} as AttrWeights;
  //   POLAR_PARAMS.forEach((p) => (base[p] = 50));
  //   return base;
  // });

  // NEW: pesos por princípio FAIR (0–100)
  const [principleWeights, setPrincipleWeights] = React.useState<WeightState>({
    A: 50,
    F: 50,
    I: 50,
    R: 50,
  });

  // KEEP: seus attrWeights atuais (usados por General/Specific)
  // Se quiser, pode inicializar só com GENERAL_PARAMS e SPECIFIC_PARAMS:
  const [attrWeights, setAttrWeights] = React.useState<AttrWeights>(() => {
    const base: AttrWeights = {} as AttrWeights;
    // apenas General + Specific recebem sliders próprios
    [...GENERAL_PARAMS, ...SPECIFIC_PARAMS].forEach((p) => (base[p] = 50));
    return base;
  });

  const derivedAttrWeights = React.useMemo(() => {
    const out = {} as Record<PolarParam, number>;

    for (const p of POLAR_PARAMS) {
      if (p in SUB_TO_PRINCIPLE) {
        // FAIR: herda do princípio correspondente
        const princ = SUB_TO_PRINCIPLE[p]!;
        out[p] = principleWeights[princ];
      } else {
        // General/Specific: usa seus sliders próprios
        out[p] = attrWeights[p] ?? 50;
      }
    }
    return out;
  }, [principleWeights, attrWeights]);

  // Load real datasets
  React.useEffect(() => {
    (async () => {
      try {
        setLoading(true);
        setLoadError(null);

        const catalogUrl =
          "https://app.fairdatapoint.org/catalog/60234295-e5c9-45e7-b96f-6bed7bba3134";
        // const datasetContainer = "https://app.fairdatapoint.org/Dataset/";
        const datasetContainer =
          "https://app.fairdatapoint.org/NetworkIntrusionDetectionDataset/";

        const res = await fetch(catalogUrl, {
          headers: { Accept: "text/turtle" },
        });
        if (!res.ok) throw new Error(`Failed to load catalog (${res.status})`);
        const rdfText = await res.text();

        const datasetUris = getDatasetsFromRDF(rdfText, datasetContainer);
        const titles = await fetchTitlesForDatasets(datasetUris);

        const results = await Promise.allSettled(
          titles.map(({ uri }) => buildUiRowFromDataset(uri)),
        );

        const ok = results
          .filter(
            (r): r is PromiseFulfilledResult<UiRow | null> =>
              r.status === "fulfilled",
          )
          .map((r) => r.value)
          .filter((x): x is UiRow => Boolean(x));

        ok.sort((a, b) =>
          a.title.localeCompare(b.title, undefined, { sensitivity: "base" }),
        );
        setRows(ok);
      } catch (e: unknown) {
        if (
          typeof e === "object" &&
          e !== null &&
          "message" in e &&
          typeof (e as { message?: unknown }).message === "string"
        ) {
          setLoadError((e as { message: string }).message);
        } else {
          setLoadError("Failed to load datasets.");
        }
      } finally {
        setLoading(false);
      }
    })();
  }, []);

  // Dataset selected via last segment of URI
  const id = params.id;
  const dataset = React.useMemo(() => {
    if (!rows.length || !id) return null;
    return (
      (rows.find((d) => normId(d.uri) === id) ||
        rows.find((d) => sameResource(d.uri, id))) ??
      null
    );
  }, [rows, id]);

  // Comparison
  const [openCompare, setOpenCompare] = React.useState(false);
  const [compareQuery, setCompareQuery] = React.useState("");
  const [compareUri, setCompareUri] = React.useState<string | null>(null);

  const compareDataset = React.useMemo(() => {
    if (!compareUri) return null;
    return rows.find((d) => sameResource(d.uri, compareUri)) ?? null;
  }, [rows, compareUri]);

  // Weighted FAIR score
  // const scoreWithWeights = React.useCallback(
  //   (scores: Record<FairPrinciple, number>) => {
  //     const totalW = Math.max(
  //       1,
  //       PRINCIPLES.reduce((acc, p) => acc + (weights[p] || 0), 0)
  //     );
  //     const sum = PRINCIPLES.reduce(
  //       (acc, p) => acc + scores[p] * (weights[p] || 0),
  //       0
  //     );
  //     return Math.round(sum / totalW);
  //   },
  //   [weights]
  // );
  // const scoreWithWeights = React.useCallback(
  //   (scores: Record<FairPrinciple, number>) => {
  //     const totalW = Math.max(
  //       1,
  //       PRINCIPLES.reduce((acc, p) => {
  //         console.log("weight", p, principleWeights[p]);
  //         return acc + (principleWeights[p] || 0);
  //       }, 0),
  //     );
  //     const sum = PRINCIPLES.reduce((acc, p) => {
  //       console.log("score*", p, scores[p], principleWeights[p]);
  //       return acc + scores[p] * (principleWeights[p] || 0);
  //     }, 0);
  //     return Math.round(sum / totalW);
  //   },
  //   [principleWeights],
  // );

  // const personalizedScoreCompare = React.useMemo(

  //   () =>
  //     compareDataset ? scoreWithWeights(compareDataset.principleScores) : null,
  //   [compareDataset, scoreWithWeights],
  // );
  const compareScores = compareDataset?.scoresByParam ?? null;

  const personalizedScoreCompare = React.useMemo(() => {
    if (!compareScores) return null;

    const vals = POLAR_PARAMS.map((p) => ({
      v: compareScores[p],
      w: derivedAttrWeights[p] || 0,
    })).filter(({ v }) => v != null) as Array<{ v: number; w: number }>;

    const totalW = Math.max(
      1,
      vals.reduce((a, b) => a + b.w, 0),
    );
    const sum = vals.reduce((a, b) => a + b.v * b.w, 0);
    return Math.round(sum / totalW);
  }, [compareScores, derivedAttrWeights]);

  // ---------- IMPORTANT: all hooks before any return ----------
  const datasetScores = dataset?.scoresByParam ?? EMPTY_SCORES;
  // const compareScores = compareDataset?.scoresByParam ?? null;

  // Data for three subprinciple radars (optional comparison)
  const fairSubsData = React.useMemo(
    () => makeRadarData(FAIR_PARAMS, datasetScores, compareScores),
    [datasetScores, compareScores],
  );
  const generalSubsData = React.useMemo(
    () => makeRadarData(GENERAL_PARAMS, datasetScores, compareScores),
    [datasetScores, compareScores],
  );
  const specificSubsData = React.useMemo(
    () => makeRadarData(SPECIFIC_PARAMS, datasetScores, compareScores),
    [datasetScores, compareScores],
  );

  function average(nums: number[]) {
    return nums.length
      ? Math.round(nums.reduce((a, b) => a + b, 0) / nums.length)
      : 0;
  }

  const groupRealScore = React.useCallback(
    (scores: Record<PolarParam, number | null>, params: PolarParam[]) => {
      const vals = params
        .map((p) => scores[p])
        .filter((v): v is number => v != null);
      return average(vals);
    },
    [],
  );

  function groupUserScore(
    scores: Record<PolarParam, number | null>,
    weights: Record<PolarParam, number>,
    params: PolarParam[],
  ) {
    const pairs = params
      .map((p) => ({ v: scores[p], w: weights[p] || 0 }))
      .filter(({ v }) => v != null) as Array<{ v: number; w: number }>;
    const denom = Math.max(
      1,
      pairs.reduce((a, b) => a + b.w, 0),
    );
    const num = pairs.reduce((a, b) => a + b.v * b.w, 0);
    return Math.round(num / denom);
  }

  // FAIR
  const fairUser = React.useMemo(
    () => groupUserScore(datasetScores, derivedAttrWeights, FAIR_PARAMS),
    [datasetScores, derivedAttrWeights],
  );

  // General
  const generalUser = React.useMemo(
    () => groupUserScore(datasetScores, attrWeights, GENERAL_PARAMS),
    [datasetScores, attrWeights],
  );

  // Specific
  const specificUser = React.useMemo(
    () => groupUserScore(datasetScores, attrWeights, SPECIFIC_PARAMS),
    [datasetScores, attrWeights],
  );

  // FAIR
  const fairReal = React.useMemo(
    () => groupRealScore(datasetScores, FAIR_PARAMS),
    [datasetScores, groupRealScore],
  );
  // const fairUser = React.useMemo(
  //   () => groupUserScore(datasetScores, attrWeights, FAIR_PARAMS),
  //   [datasetScores, attrWeights]
  // );
  const fairComp = React.useMemo(
    () => (compareScores ? groupRealScore(compareScores, FAIR_PARAMS) : null),
    [compareScores, groupRealScore],
  );

  // GENERAL
  const generalReal = React.useMemo(
    () => groupRealScore(datasetScores, GENERAL_PARAMS),
    [datasetScores, groupRealScore],
  );
  // const generalUser = React.useMemo(
  //   () => groupUserScore(datasetScores, attrWeights, GENERAL_PARAMS),
  //   [datasetScores, attrWeights]
  // );
  const generalComp = React.useMemo(
    () =>
      compareScores ? groupRealScore(compareScores, GENERAL_PARAMS) : null,
    [compareScores, groupRealScore],
  );

  // SPECIFIC
  const specificReal = React.useMemo(
    () => groupRealScore(datasetScores, SPECIFIC_PARAMS),
    [datasetScores, groupRealScore],
  );
  // const specificUser = React.useMemo(
  //   () => groupUserScore(datasetScores, attrWeights, SPECIFIC_PARAMS),
  //   [datasetScores, attrWeights]
  // );
  const specificComp = React.useMemo(
    () =>
      compareScores ? groupRealScore(compareScores, SPECIFIC_PARAMS) : null,
    [compareScores, groupRealScore],
  );

  // Personalized subprinciple score = Σ(value × weight) / Σ(weight)
  // const personalizedAttrScore = React.useMemo(() => {
  //   const vals = POLAR_PARAMS.map((p) => ({
  //     v: datasetScores[p],
  //     w: attrWeights[p] || 0,
  //   })).filter(({ v }) => v != null) as Array<{ v: number; w: number }>;

  //   const totalW = Math.max(
  //     1,
  //     vals.reduce((a, b) => a + b.w, 0)
  //   );
  //   const sum = vals.reduce((a, b) => a + b.v * b.w, 0);
  //   return Math.round(sum / totalW);
  // }, [datasetScores, attrWeights]);
  const personalizedAttrScore = React.useMemo(() => {
    const vals = POLAR_PARAMS.map((p) => ({
      v: datasetScores[p],
      w: derivedAttrWeights[p] || 0,
    })).filter(({ v }) => v != null) as Array<{ v: number; w: number }>;

    const totalW = Math.max(
      1,
      vals.reduce((a, b) => a + b.w, 0),
    );
    const sum = vals.reduce((a, b) => a + b.v * b.w, 0);
    return Math.round(sum / totalW);
  }, [datasetScores, derivedAttrWeights]);

  // ---------- END hooks ----------

  // Real candidates to compare (like analyze)
  const candidates = React.useMemo(() => {
    if (!dataset) return [] as UiRow[];
    return rows.filter(
      (d) => d.uri !== dataset.uri && titleMatches(d, compareQuery),
    );
  }, [rows, dataset, compareQuery]);

  // -------------- Render --------------

  if (loading) {
    return (
      <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
        <Header />
        <section className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 py-8">
          <Button
            startIcon={<ArrowBackIcon />}
            onClick={() => router.push("/analyze")}
            variant="text">
            Back
          </Button>
          <Typography variant="body1" sx={{ mt: 2 }}>
            Loading…
          </Typography>
        </section>
      </main>
    );
  }

  if (loadError) {
    return (
      <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
        <Header />
        <section className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 py-8">
          <Button
            startIcon={<ArrowBackIcon />}
            onClick={() => router.push("/analyze")}
            variant="text">
            Back
          </Button>
          <Typography variant="h6" sx={{ mt: 2 }}>
            Error loading datasets
          </Typography>
          <Typography variant="body2" color="text.secondary">
            {loadError}
          </Typography>
        </section>
      </main>
    );
  }

  if (!dataset) {
    return (
      <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
        <Header />
        <section className="mx-auto max-w-5xl px-4 sm:px-6 lg:px-8 py-8">
          <Button
            startIcon={<ArrowBackIcon />}
            onClick={() => router.push("/analyze")}
            variant="text">
            Back
          </Button>
          <Typography variant="h6" sx={{ mt: 2 }}>
            Dataset not found.
          </Typography>
        </section>
      </main>
    );
  }

  return (
    <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
      <Header />
      <section className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            gap: 2,
            mb: 2,
            flexWrap: "wrap",
          }}>
          <Button
            component={Link}
            href="/analyze"
            startIcon={<ArrowBackIcon />}
            variant="text">
            Back
          </Button>
          <Typography variant="h5" fontWeight={600} sx={{ flex: 1 }}>
            {dataset.title}
          </Typography>
          <Chip size="small" variant="outlined" label={dataset.uri} />
          <Button
            startIcon={<CompareArrowsIcon />}
            variant="contained"
            onClick={() => setOpenCompare(true)}>
            Compare with another dataset
          </Button>
        </Box>

        <Box
          sx={{
            display: "flex",
            alignItems: "center",
            gap: 2,
            mb: 4,
            flexWrap: "wrap",
          }}>
          <ScorePill score={dataset.overallScore} />
          {personalizedScoreCompare !== null && (
            <Chip
              color="secondary"
              variant="outlined"
              label={`Your score (compared): ${personalizedScoreCompare}/100`}
            />
          )}
          <Tooltip title="Personalized scores are weighted averages using the weights set below. Nothing is saved.">
            <InfoOutlinedIcon fontSize="small" />
          </Tooltip>
        </Box>

        {/* Subprinciples: three radars + grouped sliders */}
        <Card sx={{ borderRadius: 3, mt: 3 }}>
          {/* <CardHeader
            title="Subprinciple analysis"
            subheader="FAIR / General / Specific"
            action={
              <div>
                <Chip
                  color="secondary"
                  variant="outlined"
                  label={`Your score: ${personalizedAttrScore}/100`}
                  sx={{ mr: 1 }}
                />
                <Button
                  startIcon={<RestartAltIcon />}
                  onClick={() => {
                    const reset: AttrWeights = {} as AttrWeights;
                    POLAR_PARAMS.forEach((p) => (reset[p] = 50));
                    setAttrWeights(reset);
                  }}>
                  Reset
                </Button>
              </div>
            }
          /> */}
          <CardHeader
            title="Subprinciple analysis"
            subheader="FAIR / General / Specific"
            action={
              <div>
                <Chip
                  color="secondary"
                  variant="outlined"
                  label={`Your score: ${personalizedAttrScore}/100`}
                  sx={{ mr: 1 }}
                />
                <Button
                  startIcon={<RestartAltIcon />}
                  onClick={() => {
                    setPrincipleWeights({ A: 50, F: 50, I: 50, R: 50 });
                    setAttrWeights((prev) => {
                      const next = { ...prev };
                      [...GENERAL_PARAMS, ...SPECIFIC_PARAMS].forEach(
                        (p) => (next[p] = 50),
                      );
                      return next;
                    });
                  }}>
                  Reset
                </Button>
              </div>
            }
          />

          <CardContent>
            {/* 3 radars */}
            <Box
              sx={{
                display: "grid",
                gridTemplateColumns: { xs: "1fr", md: "1fr 1fr 1fr" },
                gap: 3,
                mb: 3,
              }}>
              <Box>
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                  FAIR Subprinciples
                </Typography>
                <Box sx={{ display: "flex", gap: 1, flexWrap: "wrap", mb: 1 }}>
                  <Chip size="small" label={`Based score: ${fairReal}`} />
                  <Chip
                    size="small"
                    color="primary"
                    variant="filled"
                    label={`Consumer score: ${fairUser}`}
                  />
                  {fairComp !== null && (
                    <Chip
                      size="small"
                      color="secondary"
                      variant="outlined"
                      label={`Compared: ${fairComp}`}
                    />
                  )}
                </Box>

                <Box sx={{ height: 280 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <RadarChart data={fairSubsData} outerRadius="80%">
                      <PolarGrid />
                      <PolarAngleAxis dataKey="name" />
                      <PolarRadiusAxis
                        angle={30}
                        domain={[0, 100]}
                        tickCount={6}
                      />
                      <Radar
                        name="Selected"
                        dataKey="a"
                        stroke={primaryStroke}
                        fill={primaryFill}
                      />
                      {compareDataset && (
                        <Radar
                          name="Compared"
                          dataKey="b"
                          stroke={compareStroke}
                          fill={compareFill}
                        />
                      )}
                      <Legend />
                      <RechartsTooltip />
                    </RadarChart>
                  </ResponsiveContainer>
                </Box>
              </Box>

              <Box>
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                  General Evaluation
                </Typography>
                {/* General */}
                <Box sx={{ display: "flex", gap: 1, flexWrap: "wrap", mb: 1 }}>
                  <Chip size="small" label={`Based score: ${generalReal}`} />
                  <Chip
                    size="small"
                    color="primary"
                    variant="filled"
                    label={`Consumer score: ${generalUser}`}
                  />
                  {generalComp !== null && (
                    <Chip
                      size="small"
                      color="secondary"
                      variant="outlined"
                      label={`Compared: ${generalComp}`}
                    />
                  )}
                </Box>

                <Box sx={{ height: 280 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <RadarChart data={generalSubsData} outerRadius="80%">
                      <PolarGrid />
                      <PolarAngleAxis dataKey="name" />
                      <PolarRadiusAxis
                        angle={30}
                        domain={[0, 100]}
                        tickCount={6}
                      />
                      <Radar
                        name="Selected"
                        dataKey="a"
                        stroke={primaryStroke}
                        fill={primaryFill}
                      />
                      {compareDataset && (
                        <Radar
                          name="Compared"
                          dataKey="b"
                          stroke={compareStroke}
                          fill={compareFill}
                        />
                      )}
                      <Legend />
                      <RechartsTooltip />
                    </RadarChart>
                  </ResponsiveContainer>
                </Box>
              </Box>

              <Box>
                <Typography variant="subtitle2" sx={{ mb: 1 }}>
                  Specific Evaluation
                </Typography>
                {/* Specific */}
                <Box sx={{ display: "flex", gap: 1, flexWrap: "wrap", mb: 1 }}>
                  <Chip size="small" label={`Based score: ${specificReal}`} />
                  <Chip
                    size="small"
                    color="primary"
                    variant="filled"
                    label={`Consumer score: ${specificUser}`}
                  />
                  {specificComp !== null && (
                    <Chip
                      size="small"
                      color="secondary"
                      variant="outlined"
                      label={`Compared: ${specificComp}`}
                    />
                  )}
                </Box>

                <Box sx={{ height: 280 }}>
                  <ResponsiveContainer width="100%" height="100%">
                    <RadarChart data={specificSubsData} outerRadius="80%">
                      <PolarGrid />
                      <PolarAngleAxis dataKey="name" />
                      <PolarRadiusAxis
                        angle={30}
                        domain={[0, 100]}
                        tickCount={6}
                      />
                      <Radar
                        name="Selected"
                        dataKey="a"
                        stroke={primaryStroke}
                        fill={primaryFill}
                      />
                      {compareDataset && (
                        <Radar
                          name="Compared"
                          dataKey="b"
                          stroke={compareStroke}
                          fill={compareFill}
                        />
                      )}
                      <Legend />
                      <RechartsTooltip />
                    </RadarChart>
                  </ResponsiveContainer>
                </Box>
              </Box>
            </Box>

            {/* Grouped weight sliders */}
            <Box
              sx={{
                display: "grid",
                gridTemplateColumns: { xs: "1fr", md: "1fr 1fr 1fr" },
                gap: 3,
              }}>
              {/* FAIR */}
              {/* <Box sx={{ display: "grid", gap: 2 }}>
                <Typography variant="subtitle2">Weights — FAIR</Typography>
                {FAIR_PARAMS.map((name) => (
                  <Box
                    key={name}
                    sx={{
                      display: "grid",
                      gridTemplateColumns: "1fr 100px",
                      alignItems: "center",
                      gap: 2,
                    }}>
                    <Box>
                      <Typography variant="body2" sx={{ mb: 1 }}>
                        {LABELS[name] ?? name}
                      </Typography>
                      <Slider
                        value={attrWeights[name]}
                        onChange={(_, v) =>
                          setAttrWeights((w) => ({ ...w, [name]: v as number }))
                        }
                        min={0}
                        max={100}
                        valueLabelDisplay="auto"
                      />
                    </Box>
                    <TextField
                      size="small"
                      type="number"
                      label="Weight"
                      inputProps={{ min: 0, max: 100 }}
                      value={attrWeights[name]}
                      onChange={(e) => {
                        const val = Math.max(
                          0,
                          Math.min(100, Number(e.target.value))
                        );
                        setAttrWeights((w) => ({
                          ...w,
                          [name]: Number.isNaN(val) ? 0 : val,
                        }));
                      }}
                    />
                  </Box>
                ))}
              </Box> */}
              {/* FAIR (A/F/I/R) */}
              <Box sx={{ display: "grid", gap: 2, mb: 3 }}>
                <Typography variant="subtitle2">
                  Weights — FAIR (A/F/I/R)
                </Typography>

                {(["F", "A", "I", "R"] as FairPrinciple[]).map((p) => (
                  <Box
                    key={p}
                    sx={{
                      display: "grid",
                      gridTemplateColumns: "1fr 100px",
                      alignItems: "center",
                      gap: 2,
                    }}>
                    <Box>
                      <Typography variant="body2" sx={{ mb: 1 }}>
                        {p} —{" "}
                        {p === "F"
                          ? "Findable"
                          : p === "A"
                            ? "Accessible"
                            : p === "I"
                              ? "Interoperable"
                              : "Reusable"}
                      </Typography>
                      <Slider
                        value={principleWeights[p]}
                        onChange={(_, v) =>
                          setPrincipleWeights((w) => ({
                            ...w,
                            [p]: v as number,
                          }))
                        }
                        min={0}
                        max={100}
                        valueLabelDisplay="auto"
                      />
                    </Box>
                    <TextField
                      size="small"
                      type="number"
                      label="Weight"
                      inputProps={{ min: 0, max: 100 }}
                      value={principleWeights[p]}
                      onChange={(e) => {
                        const val = Math.max(
                          0,
                          Math.min(100, Number(e.target.value)),
                        );
                        setPrincipleWeights((w) => ({
                          ...w,
                          [p]: Number.isNaN(val) ? 0 : val,
                        }));
                      }}
                    />
                  </Box>
                ))}
              </Box>

              {/* General */}
              <Box sx={{ display: "grid", gap: 2 }}>
                <Typography variant="subtitle2">Weights — General</Typography>
                {GENERAL_PARAMS.map((name) => (
                  <Box
                    key={name}
                    sx={{
                      display: "grid",
                      gridTemplateColumns: "1fr 100px",
                      alignItems: "center",
                      gap: 2,
                    }}>
                    <Box>
                      <Typography variant="body2" sx={{ mb: 1 }}>
                        {LABELS[name] ?? name}
                      </Typography>
                      <Slider
                        value={attrWeights[name]}
                        onChange={(_, v) =>
                          setAttrWeights((w) => ({ ...w, [name]: v as number }))
                        }
                        min={0}
                        max={100}
                        valueLabelDisplay="auto"
                      />
                    </Box>
                    <TextField
                      size="small"
                      type="number"
                      label="Weight"
                      inputProps={{ min: 0, max: 100 }}
                      value={attrWeights[name]}
                      onChange={(e) => {
                        const val = Math.max(
                          0,
                          Math.min(100, Number(e.target.value)),
                        );
                        setAttrWeights((w) => ({
                          ...w,
                          [name]: Number.isNaN(val) ? 0 : val,
                        }));
                      }}
                    />
                  </Box>
                ))}
              </Box>

              {/* Specific */}
              <Box sx={{ display: "grid", gap: 2 }}>
                <Typography variant="subtitle2">Weights — Specific</Typography>
                {SPECIFIC_PARAMS.map((name) => (
                  <Box
                    key={name}
                    sx={{
                      display: "grid",
                      gridTemplateColumns: "1fr 100px",
                      alignItems: "center",
                      gap: 2,
                    }}>
                    <Box>
                      <Typography variant="body2" sx={{ mb: 1 }}>
                        {LABELS[name] ?? name}
                      </Typography>
                      <Slider
                        value={attrWeights[name]}
                        onChange={(_, v) =>
                          setAttrWeights((w) => ({ ...w, [name]: v as number }))
                        }
                        min={0}
                        max={100}
                        valueLabelDisplay="auto"
                      />
                    </Box>
                    <TextField
                      size="small"
                      type="number"
                      label="Weight"
                      inputProps={{ min: 0, max: 100 }}
                      value={attrWeights[name]}
                      onChange={(e) => {
                        const val = Math.max(
                          0,
                          Math.min(100, Number(e.target.value)),
                        );
                        setAttrWeights((w) => ({
                          ...w,
                          [name]: Number.isNaN(val) ? 0 : val,
                        }));
                      }}
                    />
                  </Box>
                ))}
              </Box>
            </Box>

            <Typography variant="body2" color="text.secondary" sx={{ mt: 2 }}>
              Personalized score = Σ(value × weight) / Σ(weight)
            </Typography>
          </CardContent>
        </Card>

        {/* Quick comparison table by principle */}
        {compareDataset && (
          <Card sx={{ borderRadius: 3, mt: 3 }}>
            <CardHeader
              title="Principle comparison"
              subheader="Differences by A/F/I/R"
              action={
                <Button
                  startIcon={<CloseIcon />}
                  onClick={() => setCompareUri(null)}>
                  Clear comparison
                </Button>
              }
            />
            <CardContent>
              <Box
                sx={{
                  display: "grid",
                  gridTemplateColumns: "120px 1fr 1fr 120px",
                  gap: 1,
                  alignItems: "center",
                }}>
                <Typography variant="caption" color="text.secondary">
                  Principle
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  Selected
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  Compared
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  Δ
                </Typography>
                {PRINCIPLES.map((p) => (
                  <React.Fragment key={p}>
                    <Typography variant="body2">{p}</Typography>
                    <Chip
                      size="small"
                      label={`${dataset.principleScores[p]}`}
                    />
                    <Chip
                      size="small"
                      color="secondary"
                      variant="outlined"
                      label={`${compareDataset.principleScores[p]}`}
                    />
                    <Chip
                      size="small"
                      variant="outlined"
                      label={`${
                        compareDataset.principleScores[p] -
                        dataset.principleScores[p]
                      }`}
                    />
                  </React.Fragment>
                ))}
              </Box>
            </CardContent>
          </Card>
        )}
      </section>

      {/* Comparison dialog with real list */}
      <Dialog
        open={openCompare}
        onClose={() => setOpenCompare(false)}
        maxWidth="sm"
        fullWidth>
        <DialogTitle>Select a dataset to compare</DialogTitle>
        <DialogContent>
          <TextField
            fullWidth
            size="small"
            label="Search by title or URL"
            value={compareQuery}
            onChange={(e) => setCompareQuery(e.target.value)}
            sx={{ my: 1 }}
          />
          <Box sx={{ display: "grid", gap: 1, mt: 1 }}>
            {candidates.map((d) => (
              <Card
                key={d.uri}
                variant="outlined"
                sx={{
                  p: 1,
                  borderRadius: 2,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "space-between",
                }}>
                <Box sx={{ minWidth: 0 }}>
                  <Typography variant="subtitle2" noWrap>
                    {d.title}
                  </Typography>
                  {/* <Typography variant="caption" color="text.secondary" noWrap>
                    {d.uri}
                  </Typography> */}
                  <Box sx={{ minWidth: 0 /* important inside flex/grid */ }}>
                    <Typography
                      variant="caption"
                      color="text.secondary"
                      noWrap
                      sx={{
                        display: "block",
                        maxWidth: 260, // or "100%" if the parent is sized
                        overflow: "hidden",
                        textOverflow: "ellipsis",
                      }}>
                      {d.uri}
                    </Typography>
                  </Box>
                </Box>
                <Button
                  onClick={() => setCompareUri(d.uri)}
                  size="small"
                  variant={compareUri === d.uri ? "contained" : "outlined"}>
                  {compareUri === d.uri ? "Selected" : "Compare"}
                </Button>
              </Card>
            ))}
            {candidates.length === 0 && (
              <Typography variant="body2" color="text.secondary">
                No datasets found with this filter.
              </Typography>
            )}
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenCompare(false)}>Close</Button>
          <Button
            onClick={() => setOpenCompare(false)}
            disabled={!compareUri}
            variant="contained">
            Apply comparison
          </Button>
        </DialogActions>
      </Dialog>
    </main>
  );
}
