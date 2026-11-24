"use client";
import React, { useMemo, useState, useEffect } from "react";
import { EvaluatePageShell } from "@/components/fair/shared";

import {
  Alert,
  Accordion,
  AccordionDetails,
  AccordionSummary,
  TextField,
  Snackbar,
  CircularProgress,
  Typography,
  Button as MUIButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
} from "@mui/material";
import type { ButtonProps as MuiButtonProps } from "@mui/material/Button";

import tests from "@/constants/tests";
import {
  evaluateDataset,
  generateData,
  getDataset,
  login,
  updateDataset,
} from "../util";
import { updateDatasetWithScoresN3 } from "../utils/updateDataset";
import { ResponseItem } from "@/constants/types";

// LoadingButton
const LoadingButton = ({
  loading,
  startIcon,
  disabled,
  children,
  ...rest
}: MuiButtonProps & { loading?: boolean }) => (
  <MUIButton
    disabled={Boolean(disabled) || Boolean(loading)}
    startIcon={loading ? <CircularProgress size={16} /> : startIcon}
    {...rest}>
    {children}
  </MUIButton>
);

// Recharts
import {
  ResponsiveContainer,
  RadarChart,
  Radar,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Tooltip,
  Legend,
} from "recharts";

type CyberScores = {
  timeliness: number;
  availability: number;
  anonymization: number;
  labeling: number;
  attackDiversity: number;
  normalAndAttackTraffic: number;
  networkCompleteness: number;
  relevance: number;
} | null;

type AggregateScores = {
  subprinciples: Record<string, number>;
  principles: Record<string, number>;
} | null;

function RadarCard({
  title,
  data,
}: {
  title: string;
  data: Array<{ key: string; value: number }>;
}) {
  const chartData = data.map((d) => ({ metric: d.key, score: d.value }));
  return (
    <div className="w-[700px] h-[500px] p-2 border rounded-md">
      <div className="font-semibold mb-2">{title}</div>
      <ResponsiveContainer width="100%" height="90%">
        <RadarChart data={chartData}>
          <PolarGrid />
          <PolarAngleAxis dataKey="metric" />
          <PolarRadiusAxis domain={[0, 1]} tickCount={5} />
          <Tooltip />
          <Legend />
          <Radar
            name={title}
            dataKey="score"
            stroke="#8884d8"
            fill="#8884d8"
            fillOpacity={0.4}
          />
        </RadarChart>
      </ResponsiveContainer>
    </div>
  );
}

function EvaluateContent() {
  const [guid, setGuid] = useState("");
  const [dataset, setDataset] = useState("");

  const [cyberScores, setCyberScores] = useState<CyberScores>(null);
  const [fairTestsResponse, setFairTestsResponse] = useState<
    ResponseItem[] | null
  >(null);
  const [aggregate, setAggregate] = useState<AggregateScores>(null);

  const [loadingCyberResponse, setLoadingCyberResponse] = useState(false);
  const [loadingFairResponse, setLoadingFairResponse] = useState(false);

  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMsg, setSnackbarMsg] = useState(
    "Data generated successfully!"
  );
  const [snackbarSeverity, setSnackbarSeverity] = useState<
    "success" | "error" | "info" | "warning"
  >("success");

  const [isGuidSubmitted, setIsGuidSubmitted] = useState(false);

  // Update modal
  const [isUpdateModalOpen, setIsUpdateModalOpen] = useState(false);
  const [uploadEmail, setUploadEmail] = useState("");
  const [uploadPassword, setUploadPassword] = useState("");
  const [isAlreadyAuthenticated, setIsAlreadyAuthenticated] = useState(false);
  const [isUpdating, setIsUpdating] = useState(false);

  type TestType = { label: string; value?: string };
  const options = useMemo(
    () =>
      Object.keys(tests).map((key) => ({
        value: key,
        label: (tests as Record<string, TestType>)[key].label,
      })),
    []
  );

  useEffect(() => {
    if (!isUpdateModalOpen || !guid) return;
    try {
      const baseUrl = new URL(guid).origin;
      const authData = JSON.parse(localStorage.getItem("auth") || "{}");
      const storedUrl = authData?.session?.baseUrl;
      const token = authData?.session?.token;
      setIsAlreadyAuthenticated(Boolean(token && storedUrl === baseUrl));
    } catch {
      setIsAlreadyAuthenticated(false);
    }
  }, [isUpdateModalOpen, guid]);

  const handleEvaluateDataset = async (datasetStr: string, doiStr?: string) => {
    setLoadingCyberResponse(true);
    try {
      const res = await evaluateDataset(datasetStr, doiStr);
      setCyberScores({
        timeliness: res?.scores?.timeliness ?? 0,
        availability: res?.scores?.availability ?? 0,
        anonymization: res?.scores?.anonymization ?? 0,
        labeling: res?.scores?.labeling ?? 0,
        attackDiversity: res?.scores?.attackDiversity ?? 0,
        normalAndAttackTraffic: res?.scores?.normalAndAttackTraffic ?? 0,
        networkCompleteness: res?.scores?.networkCompleteness ?? 0,
        relevance: res?.scores?.relevance ?? 0,
      });
    } catch (error: unknown) {
      console.error("Error calling /evaluate:", error);
      setSnackbarMsg(
        `Failed to fetch Cyber metrics: ${
          error instanceof Error ? error.message : ""
        }`
      );
      setSnackbarSeverity("error");
      setSnackbarOpen(true);
    }
    setLoadingCyberResponse(false);
  };

  const handleGenerateData = async () => {
    setIsGuidSubmitted(true);
    setLoadingFairResponse(true);
    try {
      const ds = await getDataset(guid);
      setDataset(ds);

      // Cyber
      await handleEvaluateDataset(ds);

      // FAIR (/proxy) via utils.generateData
      const payload = await generateData(
        guid,
        options.map((o) => o.value),
        () => {
          setSnackbarMsg("Data generated successfully!");
          setSnackbarSeverity("success");
          setSnackbarOpen(true);
        }
      );

      if (payload) {
        setFairTestsResponse(
          Array.isArray(payload.fair_tests_response)
            ? payload.fair_tests_response.map((item) => ({
                ...item,
                score: item.score === null ? null : Number(item.score),
              }))
            : null
        );
        setAggregate(payload.aggregate_scores || null);
      }
    } catch (error: unknown) {
      console.error("Error generating data:", error);
      setSnackbarMsg(
        `Failed to generate data. ${
          error instanceof Error ? error.message : ""
        }`
      );
      setSnackbarSeverity("error");
      setSnackbarOpen(true);
    }
    setLoadingFairResponse(false);
  };

  // Data for charts
  const cyberData = useMemo(() => {
    if (!cyberScores) return [];
    return [
      { key: "Timeliness", value: cyberScores.timeliness },
      { key: "Availability", value: cyberScores.availability },
      { key: "Anonymization", value: cyberScores.anonymization },
      { key: "Labeling", value: cyberScores.labeling },
      { key: "Attack Diversity", value: cyberScores.attackDiversity },
      { key: "Normal & Attack", value: cyberScores.normalAndAttackTraffic },
      { key: "Network Completeness", value: cyberScores.networkCompleteness },
      { key: "Relevance", value: cyberScores.relevance },
    ];
  }, [cyberScores]);

  const fairSubprinciplesData = useMemo(() => {
    if (!aggregate?.subprinciples) return [];
    const subs = aggregate.subprinciples;
    const order = ["F1", "F2", "F3", "A1", "A2", "I1", "I2", "I3", "R1"];
    return order
      .filter((k) => subs.hasOwnProperty(k))
      .map((k) => ({ key: k, value: subs[k] ?? 0 }));
  }, [aggregate]);

  // Login (modal)
  const onLogin = async () => {
    try {
      await login(guid, uploadEmail, uploadPassword);
      const token = JSON.parse(localStorage.getItem("auth") || "{}")?.session
        ?.token;
      setIsAlreadyAuthenticated(Boolean(token));
      setSnackbarMsg("Authenticated successfully!");
      setSnackbarSeverity("success");
      setSnackbarOpen(true);
    } catch {
      setSnackbarMsg("Authentication failed. Check your credentials.");
      setSnackbarSeverity("error");
      setSnackbarOpen(true);
    }
  };

  // Update dataset with scores
  const onUpdateDataset = async () => {
    if (!dataset) {
      setSnackbarMsg("Dataset not loaded yet.");
      setSnackbarSeverity("warning");
      setSnackbarOpen(true);
      return;
    }
    if (!cyberScores || !aggregate?.subprinciples) {
      setSnackbarMsg("Scores not available yet. Run the evaluation first.");
      setSnackbarSeverity("warning");
      setSnackbarOpen(true);
      return;
    }

    setIsUpdating(true);
    try {
      const newDataset = await updateDatasetWithScoresN3({
        dataset,
        fairSubprinciples: aggregate.subprinciples,
        cyber: {
          timeliness: cyberScores.timeliness,
          availability: cyberScores.availability,
          anonymization: cyberScores.anonymization,
          labeling: cyberScores.labeling,
          attackDiversity: cyberScores.attackDiversity,
          normalAndAttackTraffic: cyberScores.normalAndAttackTraffic,
          networkCompleteness: cyberScores.networkCompleteness,
          relevance: cyberScores.relevance,
        },
      });

      const status = await updateDataset(newDataset, guid);
      if (status === 200) {
        setSnackbarMsg("Dataset updated successfully!");
        setSnackbarSeverity("success");
        setSnackbarOpen(true);
        setDataset(newDataset);
        setIsUpdateModalOpen(false);
      } else {
        setSnackbarMsg(`Failed to update the dataset (HTTP ${status}).`);
        setSnackbarSeverity("error");
        setSnackbarOpen(true);
      }
    } catch (err) {
      console.error("Error updating Dataset:", err);
      setSnackbarMsg("Failed to update the dataset. Check the console.");
      setSnackbarSeverity("error");
      setSnackbarOpen(true);
    }
    setIsUpdating(false);
  };

  return (
    <div className="p-4">
      <h1 className="mb-10 font-bold text-3xl">ATHENA Evaluator</h1>

      <label htmlFor="uriInput">Enter the GUID:</label>
      <div className="w-full flex items-center my-2 gap-2">
        <TextField
          required
          id="uriInput"
          label="GUID"
          placeholder="Enter the GUID..."
          value={guid}
          onChange={(e) => setGuid(e.target.value)}
          className="border rounded p-2 w-full"
        />
        <LoadingButton
          onClick={handleGenerateData}
          loading={loadingCyberResponse || loadingFairResponse}
          disabled={!guid}
          sx={{ minWidth: 220, p: "12px" }}
          variant="contained">
          Run evaluation
        </LoadingButton>

        {/* Open update modal */}
        <MUIButton
          onClick={() => setIsUpdateModalOpen(true)}
          disabled={!guid}
          sx={{ minWidth: 220, p: "12px" }}
          variant="outlined">
          Update Dataset
        </MUIButton>
      </div>

      {/* CYBER */}
      {isGuidSubmitted && (
        <h2 className="text-lg font-semibold">Cybersecurity Evaluation</h2>
      )}

      {loadingCyberResponse ? (
        <div className="flex h-[400px] w-6/12 items-center justify-center">
          <CircularProgress />
        </div>
      ) : cyberScores ? (
        <div className="flex my-2 items-start gap-3">
          <RadarCard title="Cyber — Specific Metrics" data={cyberData} />
        </div>
      ) : (
        isGuidSubmitted && (
          <div className="flex my-2 items-center">
            <p className="text-red-500">Failed to generate the Cyber chart.</p>
          </div>
        )
      )}

      {/* FAIR */}
      {isGuidSubmitted && (
        <h2 className="mt-8 text-lg font-semibold">FAIR Evaluation</h2>
      )}

      {loadingFairResponse ? (
        <div className="flex my-2 w-2/4 items-center justify-center">
          <CircularProgress />
        </div>
      ) : (
        <>
          {fairSubprinciplesData.length > 0 && (
            <div className="my-4">
              <RadarCard
                title="FAIR — Subprinciples"
                data={fairSubprinciplesData}
              />
            </div>
          )}

          {Array.isArray(fairTestsResponse) && fairTestsResponse.length > 0 && (
            <div id="responseDisplay" className="mt-4">
              <Typography className="mb-2 font-semibold">
                FAIR Tests (details)
              </Typography>
              {fairTestsResponse.map((item: ResponseItem, index: number) => (
                <div key={index}>
                  <Accordion>
                    <AccordionSummary
                      aria-controls={`panel-${index}-content`}
                      id={`panel-${index}-header`}>
                      <h2 className="text-lg font-semibold">
                        Test {index + 1}: {item.test ?? "N/A"}{" "}
                        {item.score == 1 ? "✅" : "❌"}
                      </h2>
                    </AccordionSummary>
                    <AccordionDetails>
                      <p>ID: {item.id ?? "N/A"}</p>
                      <p>Principle: {item.principle ?? "N/A"}</p>
                      <p>Type: {item.type ?? "N/A"}</p>
                      <p>Score: {item.score ?? 0}</p>
                      <p>Date: {item.date ?? "N/A"}</p>
                      <p>Software Version: {item.softwareVersion ?? "N/A"}</p>
                      <p>Related URI: {item.relatedUri ?? "N/A"}</p>
                      <p
                        dangerouslySetInnerHTML={{
                          __html: `Comments: ${item.comments ?? "N/A"}`,
                        }}
                      />
                    </AccordionDetails>
                  </Accordion>
                  <br />
                </div>
              ))}
            </div>
          )}
        </>
      )}

      {/* Update modal */}
      <Dialog
        open={isUpdateModalOpen}
        onClose={() => setIsUpdateModalOpen(false)}>
        <DialogTitle>Update Dataset</DialogTitle>
        <DialogContent>
          {!isAlreadyAuthenticated ? (
            <>
              <Typography gutterBottom>
                Sign in to the GUID host to authorize the update.
              </Typography>
              <TextField
                label="Email"
                type="email"
                fullWidth
                value={uploadEmail}
                onChange={(e) => setUploadEmail(e.target.value)}
                margin="dense"
              />
              <TextField
                label="Password"
                type="password"
                fullWidth
                value={uploadPassword}
                onChange={(e) => setUploadPassword(e.target.value)}
                margin="dense"
              />
            </>
          ) : (
            <Typography gutterBottom>
              ✅ Authenticated for {guid ? new URL(guid).origin : ""}
            </Typography>
          )}
        </DialogContent>
        <DialogActions>
          <MUIButton
            onClick={() => setIsUpdateModalOpen(false)}
            disabled={isUpdating}>
            Cancel
          </MUIButton>

          {!isAlreadyAuthenticated ? (
            <LoadingButton
              onClick={onLogin}
              loading={false}
              disabled={!guid || !uploadEmail || !uploadPassword}
              variant="contained">
              Sign in
            </LoadingButton>
          ) : (
            <LoadingButton
              onClick={onUpdateDataset}
              loading={isUpdating}
              disabled={
                !guid || !dataset || !cyberScores || !aggregate?.subprinciples
              }
              variant="contained">
              Save scores to dataset
            </LoadingButton>
          )}
        </DialogActions>
      </Dialog>

      {/* Snackbar */}
      <Snackbar
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
        open={snackbarOpen}
        onClose={() => setSnackbarOpen(false)}
        autoHideDuration={5000}
        key="Snackbar.Success.SlideTransition">
        <Alert
          onClose={() => setSnackbarOpen(false)}
          severity={snackbarSeverity}
          variant="filled"
          sx={{ width: "100%" }}>
          {snackbarMsg}
        </Alert>
      </Snackbar>
    </div>
  );
}

export default function Page() {
  return (
    <EvaluatePageShell>
      <EvaluateContent />
    </EvaluatePageShell>
  );
}
