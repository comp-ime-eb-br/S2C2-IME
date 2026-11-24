"use client";
import React from "react";
import Link from "next/link";
import { motion } from "framer-motion";
import {
  Header,
  HubCard,
  QuickActions,
  // RecentEvaluations,
} from "@/components/fair/shared";
import Button from "@mui/material/Button";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";
import ManageSearchIcon from "@mui/icons-material/ManageSearch";
import BarChartIcon from "@mui/icons-material/BarChart";
import TrackChangesIcon from "@mui/icons-material/TrackChanges";

export default function Page() {
  return (
    <main className="min-h-dvh bg-gradient-to-b from-background to-muted/40">
      <Header />
      <section className="mx-auto max-w-6xl px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4 }}
          className="mt-8 rounded-3xl bg-card p-6 shadow-sm">
          <div className="flex flex-col items-start justify-between gap-6 md:flex-row md:items-center">
            <div>
              <h1 className="text-2xl md:text-3xl font-semibold tracking-tight">
                What do you want to do today?
              </h1>
              <p className="mt-2 text-muted-foreground max-w-prose">
                Choose one of the options below to get started. You can evaluate
                a new dataset or explore previously evaluated results.
              </p>
            </div>
            <div className="flex gap-3">
              <Button
                component={Link}
                href="/evaluate"
                variant="contained"
                startIcon={<AutoAwesomeIcon fontSize="small" />}>
                Evaluate dataset
              </Button>
              <Button
                component={Link}
                href="/analyze"
                variant="outlined"
                startIcon={<ManageSearchIcon fontSize="small" />}>
                Analyze evaluations
              </Button>
            </div>
          </div>
        </motion.div>

        <QuickActions />

        <div className="grid gap-6 md:grid-cols-2 mt-8">
          <HubCard
            icon={<TrackChangesIcon />}
            title="Evaluate a new dataset"
            description="Submit an RDF/URL/DOI to run FAIR metrics and generate charts automatically."
            href="/evaluate"
            ctaLabel="Go to evaluation"
          />
          <HubCard
            icon={<BarChartIcon />}
            title="Analyze evaluated datasets"
            description="Explore previous results, filter by score, compare principles, and export reports."
            href="/analyze"
            ctaLabel="Explore evaluations"
          />
        </div>

        {/* <RecentEvaluations /> */}
      </section>
    </main>
  );
}
