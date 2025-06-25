"use client";

import { useEffect, useMemo, useState } from "react";
import Image from "next/image";

import {
  Alert,
  Accordion,
  AccordionDetails,
  AccordionSummary,
  Button,
  TextField,
  Snackbar,
  InputAdornment,
  Tooltip,
  IconButton,
  CircularProgress,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Typography,
} from "@mui/material";
import InfoOutlinedIcon from "@mui/icons-material/InfoOutlined";
import tests from "@/constants/tests";

import {
  calculatePrincipleScores,
  evaluateDataset,
  generateData,
  getDataset,
  login,
  updateDataset,
  uploadGraphImage,
  updateEvaluationResult,
} from "./util";
import { PrincipleScores, ResponseItem } from "@/constants/types";

export default function Home() {
  const [guid, setGuid] = useState("");
  const [doi, setDoi] = useState("");
  const [dataset, setDataset] = useState("");
  const [image, setImage] = useState("");
  const [response, setResponse] = useState<ResponseItem[] | string | null>(
    null
  );

  const [principleScores, setPrincipleScores] = useState<PrincipleScores>({});
  const [uploadEmail, setUploadEmail] = useState("");
  const [uploadPassword, setUploadPassword] = useState("");

  const [loadingCyberResponse, setLoadingCyberResponse] = useState(false);
  const [loadingFairResponse, setLoadingFairResponse] = useState(false);

  const [isSnackbarOpen, setIsSnackbarOpen] = useState(false);
  const [isGuidSubmitted, setIsGuidSubmitted] = useState(false);
  const [isUploadModalOpen, setIsUploadModalOpen] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [isAlreadyAuthenticated, setIsAlreadyAuthenticated] = useState(false);

  const options = useMemo(
    () =>
      Object.keys(tests).map((key) => ({
        value: key,
        label: tests[key].label,
      })),
    []
  );

  const handleLogin = async (guid: string, email: string, password: string) => {
    try {
      await login(guid, email, password);
    } catch (error) {
      console.error("Erro ao fazer login:", error);
      alert(
        "Erro ao fazer login. Verifique suas credenciais e tente novamente."
      );
      throw error;
    }
  };

  const handleGenerateData = async () => {
    setIsGuidSubmitted(true);
    setLoadingFairResponse(true);

    try {
      const response = await getDataset(guid);
      handleEvaluateDataset(response, doi);

      setDataset(response);
      const processedData = await generateData(
        guid,
        options.map((option) => option.value),
        () => setIsSnackbarOpen(true)
      );
      if (processedData) {
        setResponse(processedData as ResponseItem[]);
      } else {
        setResponse(
          "Erro ao gerar os dados. Verifique o console para mais detalhes."
        );
      }
    } catch (error) {
      console.error("Erro ao gerar dados:", error);
      setResponse(
        "Erro ao gerar os dados. Verifique o console para mais detalhes."
      );
    }

    setLoadingFairResponse(false);
  };

  const handleEvaluateDataset = async (dataset: string, doi?: string) => {
    setLoadingCyberResponse(true);
    try {
      const response = await evaluateDataset(dataset, doi);
      setImage(response.imageBase64);
    } catch (error) {
      console.error("Erro ao atualizar o dataset", error);
      setResponse(
        "Erro ao atualizar o dataset. Verifique o console para mais detalhes."
      );
    }
    setLoadingCyberResponse(false);
  };

  useEffect(
    function calculateScoresFromArray() {
      if (Array.isArray(response)) {
        calculatePrincipleScores(response).then(setPrincipleScores);
      }
    },
    [response]
  );

  useEffect(
    function verifyGuidAuth() {
      if (!isUploadModalOpen || !guid) return;

      try {
        const baseUrl = new URL(guid).origin;
        const authData = JSON.parse(localStorage.getItem("auth") || "{}");
        const storedUrl = authData?.session?.baseUrl;
        const token = authData?.session?.token;

        setIsAlreadyAuthenticated(Boolean(token && storedUrl === baseUrl));
      } catch (err) {
        console.error("Erro ao verificar autenticação:", err);
        setIsAlreadyAuthenticated(false);
      }
    },
    [isUploadModalOpen, guid]
  );

  return (
    <div className="p-4">
      <h1 className="mb-10 font-bold text-3xl">ATHENA Evaluator</h1>
      <label htmlFor="uriInput">Insira a GUID:</label>
      <div className="w-full flex items-center my-2 gap-2">
        <TextField
          required
          id="uriInput"
          label="GUID"
          placeholder="Digite a GUID..."
          value={guid}
          onChange={(e) => setGuid(e.target.value)}
          className="border rounded p-2 w-full"
        />
        <TextField
          id="doiInput"
          label="DOI"
          placeholder="Digite o DOI..."
          value={doi}
          onChange={(e) => setDoi(e.target.value)}
          className="border rounded p-2 w-8/12"
          InputProps={{
            endAdornment: (
              <InputAdornment position="end">
                <Tooltip title="Informe o DOI (ex: 10.1234/abcd1234) para melhor avaliação da relevância caso não tenha essa informação em seu dataset.">
                  <IconButton>
                    <InfoOutlinedIcon />
                  </IconButton>
                </Tooltip>
              </InputAdornment>
            ),
          }}
        />
        <Button
          onClick={handleGenerateData}
          loading={loadingFairResponse}
          disabled={!guid}
          style={{ minWidth: "300px", padding: "12px" }}>
          Fazer avaliação
        </Button>
      </div>

      {isGuidSubmitted && (
        <div>
          <h2 className="text-lg font-semibold">Avaliação CyberSegurança</h2>
        </div>
      )}
      {loadingCyberResponse ? (
        <div className="flex h-[400px] w-6/12 items-center justify-center">
          <CircularProgress />
        </div>
      ) : image ? (
        <div className="flex my-2 items-center">
          <Image
            width={500}
            height={500}
            src={image}
            alt="Avaliação do Dataset"
            unoptimized
          />
          <Button onClick={() => setIsUploadModalOpen(true)}>
            Upload Gráfico
          </Button>
        </div>
      ) : (
        isGuidSubmitted && (
          <div className="flex my-2 items-center">
            <p className="text-red-500">
              Erro ao gerar o gráfico. Verifique o console para mais detalhes.
            </p>
          </div>
        )
      )}
      {isGuidSubmitted && (
        <div>
          <h2 className="text-lg font-semibold">Avaliação FAIR</h2>
        </div>
      )}
      {loadingFairResponse ? (
        <div className="flex my-2 w-2/4 items-center justify-center">
          <CircularProgress />
        </div>
      ) : (
        <>
          {Object.keys(principleScores).length > 0 && (
            <div className="mx-2">
              <h3 className="text-lg font-semibold">Notas por Princípio</h3>
              {Object.keys(principleScores).map((principle) => (
                <p key={principle}>
                  {principle}: {principleScores[principle].passed}/
                  {principleScores[principle].total}
                </p>
              ))}
            </div>
          )}
          <br />
          {Array.isArray(response) && (
            <div id="responseDisplay">
              {response.map((item: ResponseItem, index: number) => (
                <div key={index}>
                  <Accordion>
                    <AccordionSummary
                      aria-controls="panel1-content"
                      id="panel1-header">
                      <h2 className="text-lg font-semibold">
                        Teste {index + 1}: {item.test ?? "N/A"}{" "}
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
                        }}></p>
                    </AccordionDetails>
                  </Accordion>
                  <br />
                </div>
              ))}
            </div>
          )}
        </>
      )}

      <Snackbar
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
        open={isSnackbarOpen}
        onClose={() => setIsSnackbarOpen(false)}
        key="Snackbar.Success.SlideTransition"
        autoHideDuration={5000}>
        <Alert
          onClose={() => setIsSnackbarOpen(false)}
          severity="success"
          variant="filled"
          sx={{ width: "100%" }}>
          Dados gerados com sucesso!
        </Alert>
      </Snackbar>

      <Dialog
        open={isUploadModalOpen}
        onClose={() => setIsUploadModalOpen(false)}>
        <DialogTitle>Confirmar Upload</DialogTitle>
        <DialogContent>
          {isAlreadyAuthenticated ? (
            <>
              <Typography>
                ✅ Você já está autenticado para essa URL.
              </Typography>
              <Button
                className="mt-2"
                variant="outlined"
                color="secondary"
                onClick={() => {
                  localStorage.removeItem("auth");
                  setIsAlreadyAuthenticated(false);
                  setUploadEmail("");
                  setUploadPassword("");
                }}>
                Fazer logout
              </Button>
            </>
          ) : (
            <>
              <Typography gutterBottom>
                Para continuar com o upload do gráfico, faça login com as
                credenciais autorizadas.
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
                label="Senha"
                type="password"
                fullWidth
                value={uploadPassword}
                onChange={(e) => setUploadPassword(e.target.value)}
                margin="dense"
              />
            </>
          )}
        </DialogContent>
        <DialogActions>
          <Button
            onClick={() => setIsUploadModalOpen(false)}
            disabled={isUploading}>
            Cancelar
          </Button>

          <Button
            onClick={async () => {
              setIsUploading(true);
              try {
                if (!isAlreadyAuthenticated)
                  await handleLogin(guid, uploadEmail, uploadPassword);

                const imageUrl = await uploadGraphImage(image);
                const newDataset = updateEvaluationResult(
                  guid,
                  dataset,
                  imageUrl
                );

                const status = await updateDataset(newDataset, guid);
                if (status === 200) {
                  <Alert
                    severity="success"
                    variant="filled"
                    sx={{ width: "100%" }}>
                    Upload realizado com sucesso!
                  </Alert>;
                } else {
                  <Alert
                    severity="error"
                    variant="filled"
                    sx={{ width: "100%" }}>
                    Erro ao fazer upload. Verifique o console para mais
                    detalhes.
                  </Alert>;
                }

                setIsUploadModalOpen(false);
              } catch (err) {
                console.error("Erro no upload:", err);
              }
              setIsUploading(false);
            }}
            disabled={
              isAlreadyAuthenticated
                ? !guid
                : !uploadEmail || !uploadPassword || !guid
            }
            loading={isUploading}
            variant="contained"
            color="primary">
            Confirmar Upload
          </Button>
        </DialogActions>
      </Dialog>
    </div>
  );
}
