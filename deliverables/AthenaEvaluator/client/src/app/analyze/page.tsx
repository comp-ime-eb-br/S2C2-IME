// page.tsx
"use client";
import React from "react";
import { Header, DatasetCard, DatasetTable } from "@/components/fair/shared";

import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import SearchIcon from "@mui/icons-material/Search";

import {
  getDatasetsFromRDF,
  fetchTitlesForDatasets,
  buildUiRowFromDataset,
  type UiRow,
} from "./util";

type EvaluatedOption = { label: string; uri: string };

export default function Page() {
  const [query, setQuery] = React.useState("");
  const [view, setView] = React.useState<"grid" | "table">("grid");

  // Autocomplete options
  const [evaluatedOptions, setEvaluatedOptions] = React.useState<
    EvaluatedOption[]
  >([]);
  const [loadingOptions, setLoadingOptions] = React.useState(false);
  const [loadError, setLoadError] = React.useState<string | null>(null);

  // Actual rows to display
  const [rows, setRows] = React.useState<UiRow[]>([]);
  const [loadingRows, setLoadingRows] = React.useState(false);

  // 1) load URIs (ldp:contains) and titles for autocomplete
  React.useEffect(() => {
    (async () => {
      try {
        setLoadingOptions(true);
        setLoadError(null);

        const catalogUrl =
          "https://app.fairdatapoint.org/catalog/60234295-e5c9-45e7-b96f-6bed7bba3134";
        // const datasetContainer = "https://app.fairdatapoint.org/Dataset/";
        const datasetContainer =
          "https://app.fairdatapoint.org/NetworkIntrusionDetectionDataset/";

        const res = await fetch(catalogUrl, {
          headers: { Accept: "text/turtle" },
        });
        const rdfText = await res.text();
        const datasetUris = await getDatasetsFromRDF(rdfText, datasetContainer);
        console.log("Found datasets:", datasetUris.length);

        const titles = await fetchTitlesForDatasets(datasetUris);

        const options: EvaluatedOption[] = titles
          .map(({ uri, title }) => ({
            uri,
            label: title?.trim() || uri,
          }))
          .sort((a, b) =>
            a.label.localeCompare(b.label, undefined, { sensitivity: "base" })
          );

        setEvaluatedOptions(options);
      } catch (e: unknown) {
        setLoadError(
          e instanceof Error ? e.message : "Failed to load datasets."
        );
      } finally {
        setLoadingOptions(false);
      }
    })();
  }, []);

  // 2) once options arrive, build actual rows (scores)
  React.useEffect(() => {
    if (!evaluatedOptions.length) return;

    (async () => {
      setLoadingRows(true);
      try {
        const results = await Promise.allSettled(
          evaluatedOptions.map((opt) => buildUiRowFromDataset(opt.uri))
        );
        const ok = results
          .filter(
            (r): r is PromiseFulfilledResult<UiRow | null> =>
              r.status === "fulfilled"
          )
          .map((r) => r.value)
          .filter(Boolean) as UiRow[];

        // sort by title (or change to overallScore desc, etc.)
        ok.sort((a, b) =>
          a.title.localeCompare(b.title, undefined, { sensitivity: "base" })
        );
        setRows(ok);
      } finally {
        setLoadingRows(false);
      }
    })();
  }, [evaluatedOptions]);

  // 3) filter by title/URL
  const filtered = React.useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return rows;
    return rows.filter(
      (d) =>
        d.title.toLowerCase().includes(q) || d.uri.toLowerCase().includes(q)
    );
  }, [rows, query]);

  return (
    <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
      <Header />
      <section className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
          <div>
            <h1 className="text-2xl md:text-3xl font-semibold tracking-tight">
              Analyze evaluations
            </h1>
            <p className="text-muted-foreground">
              Search, filter, and compare previously evaluated datasets.
            </p>
          </div>
          <Tabs
            value={view}
            onChange={(_, v) => setView(v)}
            aria-label="switch view">
            <Tab value="grid" label="Cards" />
            <Tab value="table" label="Table" />
          </Tabs>
        </div>

        <Card sx={{ borderRadius: 3 }}>
          <CardContent sx={{ p: { xs: 2, md: 3 } }}>
            <div className="grid gap-4 md:grid-cols-4 md:gap-6">
              <div className="md:col-span-2 flex items-center gap-2">
                <SearchIcon
                  fontSize="small"
                  className="text-muted-foreground"
                />
                <Autocomplete
                  fullWidth
                  freeSolo
                  options={evaluatedOptions}
                  loading={loadingOptions}
                  getOptionLabel={(o) => (typeof o === "string" ? o : o.label)}
                  filterOptions={(options, state) => {
                    const q = (state.inputValue ?? "").toLowerCase().trim();
                    if (!q) return options;
                    return options.filter((opt) => {
                      const { label, uri } =
                        typeof opt === "string" ? { label: opt, uri: "" } : opt;
                      return (
                        label.toLowerCase().includes(q) ||
                        (uri?.toLowerCase().includes(q) ?? false)
                      );
                    });
                  }}
                  onChange={(_, value) => {
                    if (typeof value === "string") setQuery(value);
                    else if (value) setQuery(value.label);
                  }}
                  onInputChange={(_, value) => setQuery(value)}
                  renderInput={(params) => (
                    <TextField
                      {...params}
                      fullWidth
                      size="small"
                      label="Search by title or URL"
                      value={query}
                      onChange={(e) => setQuery(e.target.value)}
                      helperText={
                        loadError
                          ? `Error: ${loadError}`
                          : loadingRows
                          ? "Loading scores..."
                          : undefined
                      }
                    />
                  )}
                  renderOption={(props, option) => {
                    const opt =
                      typeof option === "string"
                        ? { label: option, uri: "" }
                        : option;
                    return (
                      <li {...props} key={opt.uri || opt.label}>
                        <div className="flex flex-col">
                          <span>{opt.label}</span>
                          {opt.uri && (
                            <span className="text-xs text-muted-foreground">
                              {opt.uri}
                            </span>
                          )}
                        </div>
                      </li>
                    );
                  }}
                />
              </div>
            </div>
          </CardContent>
        </Card>

        {/* RENDER using actual data */}
        {view === "grid" ? (
          <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {filtered.map((d) => (
              <DatasetCard key={d.id} data={d} />
            ))}
            {!loadingRows && filtered.length === 0 && <EmptyState />}
          </div>
        ) : (
          <div className="mt-6">
            <DatasetTable rows={filtered} />
            {!loadingRows && filtered.length === 0 && <EmptyState />}
          </div>
        )}
      </section>
    </main>
  );
}

function EmptyState() {
  return (
    <div className="rounded-3xl border bg-card p-12 text-center text-sm text-muted-foreground">
      No results with the current filters
    </div>
  );
}
