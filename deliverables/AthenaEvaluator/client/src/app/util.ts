import tests from "@/constants/tests";
import { ApiResponseItem, ResponseItem } from "@/constants/types";

// Flask backend base URL
const API_BASE =
  process.env.NEXT_PUBLIC_SERVER_URL || process.env.SERVER_URL || "";

/** Helper: POST JSON and expect JSON, with decent errors */
async function postJsonExpectJson(url: string, body: unknown) {
  const res = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json", Accept: "application/json" },
    body: JSON.stringify(body),
  });

  const ct = res.headers.get("content-type") || "";

  if (!res.ok) {
    const txt = await res.text().catch(() => "");
    throw new Error(
      `HTTP ${res.status} on ${url}. CT=${ct}. Body: ${txt.slice(0, 500)}`
    );
  }
  if (!ct.includes("application/json")) {
    const txt = await res.text().catch(() => "");
    throw new Error(
      `Expected JSON from ${url}, got '${ct}'. Body: ${txt.slice(0, 500)}`
    );
  }
  return res.json();
}

export async function generateData(
  uri: string,
  selectedTests: string[],
  onSuccess: VoidFunction
) {
  if (!uri) {
    alert("Please enter a URI.");
    return;
  }

  if (selectedTests.length === 0) {
    alert("Please select at least one test.");
    return;
  }

  const payload = { subject: uri, tests: selectedTests };

  try {
    const proxyUrl = `${API_BASE}/proxy`;
    const json = await postJsonExpectJson(proxyUrl, payload);

    // json should contain: { fair_tests_response, aggregate_scores, manual_params }
    const fairTests = json?.fair_tests_response;
    const aggregate = json?.aggregate_scores || null;

    const processedData = processApiResponse(fairTests);
    onSuccess();
    return { fair_tests_response: processedData, aggregate_scores: aggregate };
  } catch (error) {
    console.error("Error calling API (/proxy):", error);
    throw error;
  }
}

function processApiResponse(data: ApiResponseItem[][]) {
  if (!Array.isArray(data)) return [];

  const results: {
    id: string | null;
    test: string | null;
    principle: string | null;
    type: string | null;
    score: string | null;
    date: string | null;
    softwareVersion: string | null;
    relatedUri: string | null;
    comments: string | null;
  }[] = [];

  data.forEach((group: ApiResponseItem[]) => {
    (group || []).forEach((item) => {
      const test = item?.["@id"]?.split("//tests/")[1]?.split("#")[0];
      const result = {
        id: item?.["@id"] || null,
        test: test || null,
        type: item?.["@type"] ? item["@type"].join(", ") : null,
        score:
          item?.["http://semanticscience.org/resource/SIO_000300"]?.[0]?.[
            "@value"
          ] || null,
        date:
          item?.["http://purl.obolibrary.org/obo/date"]?.[0]?.["@value"] ||
          null,
        softwareVersion:
          item?.["http://schema.org/softwareVersion"]?.[0]?.["@value"] || null,
        relatedUri:
          item?.["http://semanticscience.org/resource/SIO_000332"]?.[0]?.[
            "@id"
          ] || null,
        comments:
          item?.["http://schema.org/comment"]?.[0]?.["@value"]?.replace(
            /\n/g,
            "<br/>"
          ) || null,
        principle: test
          ? (tests as Record<string, { principle?: string }>)[test]
              ?.principle || null
          : null,
      };

      results.push(result);
    });
  });

  return results;
}

export async function getDataset(guid: string) {
  try {
    const response = await fetch(guid, {
      method: "GET",
      headers: { Accept: "text/turtle" },
    });
    return response.text();
  } catch (error) {
    console.log("ERROR RETRIEVING DATASET:", error);
    window.alert(
      "Failed to retrieve the dataset. Check the console for more details."
    );
    throw error;
  }
}

export async function updateDataset(newDataset: string, guid: string) {
  try {
    const token = JSON.parse(localStorage.getItem("auth") || "{}")?.session
      ?.token;
    const response = await fetch(guid, {
      method: "PUT",
      headers: {
        Accept: "text/turtle",
        Authorization: `Bearer ${token}`,
        "Content-Type": "text/turtle",
      },
      body: newDataset,
    });
    return response.status;
  } catch (error) {
    console.log("ERROR UPDATING DATASET:", error);
    window.alert(
      "Failed to update the dataset. Check the console for more details."
    );
    throw error;
  }
}

export const uploadGraphImage = async (base64Image: string, name?: string) => {
  const url = `${API_BASE}/upload-image`;
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      image: base64Image,
      name: name || "evaluation",
      fileName: "fair-evaluation.png",
    }),
  });

  const data = await response
    .json()
    .catch(() => ({} as { url?: string; error?: string }));
  if (response.ok) return data.url;
  console.error("Error:", (data as { error?: string })?.error);
};

export async function evaluateDataset(dataset: string, doi?: string) {
  try {
    const url = `${API_BASE}/evaluate`;
    const response = await fetch(url, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ dataset, doi }),
    });
    if (!response.ok)
      throw new Error(`Failed to evaluate dataset (HTTP ${response.status})`);

    const ct = response.headers.get("content-type") || "";
    if (!ct.includes("application/json")) {
      const txt = await response.text().catch(() => "");
      throw new Error(`/evaluate returned '${ct}'. Body: ${txt.slice(0, 300)}`);
    }
    return response.json();
  } catch (error) {
    console.log("ERROR EVALUATING DATASET:", error);
    window.alert(
      "Failed to evaluate the dataset. Check the console for more details."
    );
    throw error;
  }
}

export async function calculatePrincipleScores(responses: ResponseItem[]) {
  const principleScores: {
    [key: string]: { total: number; passed: number };
  } = {};

  (responses || []).forEach((item) => {
    if (item?.principle) {
      if (!principleScores[item.principle]) {
        principleScores[item.principle] = { total: 0, passed: 0 };
      }
      principleScores[item.principle].total += 1;
      // item.score is string in your parser. Ensure numeric:
      const sc =
        typeof item.score === "string"
          ? Number(item.score)
          : (item.score as number);
      if (sc && sc > 0) {
        principleScores[item.principle].passed += 1;
      }
    }
  });

  return principleScores;
}

export async function login(guid: string, email: string, password: string) {
  if (!guid || !email || !password) {
    alert("Please fill in URI, User and Password.");
    return;
  }

  const baseUrl = new URL(guid).origin;
  const loginUrl = `${baseUrl}/tokens`;

  try {
    const response = await fetch(loginUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) throw new Error("Authentication failed.");

    const data = await response.json();

    localStorage.setItem(
      "auth",
      JSON.stringify({
        session: { token: data.token, baseUrl },
      })
    );
    alert("Authenticated successfully!");
    return data.token;
  } catch (error) {
    console.error("Login error:", error);
    alert("Failed to authenticate. Check your credentials and try again.");
  }
}

export function updateEvaluationResult(
  baseUrl: string,
  dataset: string,
  newImageUrl: string
): string {
  const predicate = `<http://fairdatapoint.org/evaluationResult>`;

  const datasetUriMatch = [
    ...dataset.matchAll(/^<([^>]+)>\s+a\s+[^.]*dcat:Dataset[^.]*;/gm),
  ];
  if (!datasetUriMatch.length) {
    console.warn("Could not identify the dataset URI.");
    return dataset;
  }

  const hasEvaluationResult = dataset.includes(predicate);

  if (hasEvaluationResult) {
    const updated = dataset.replace(
      /<http:\/\/fairdatapoint\.org\/evaluationResult>\s*<[^>]+>([.;])/,
      (_m, endingChar) => {
        const end = endingChar === ";" ? ";" : " .";
        return `<http://fairdatapoint.org/evaluationResult> <${newImageUrl}>${end}`;
      }
    );
    return updated;
  } else {
    const lines = dataset.split("\n");
    const startIdx = lines.findIndex(
      (line, index) =>
        line.trim().startsWith(`<${baseUrl}>`) &&
        lines.slice(0, index).filter((l) => l.trim().startsWith(`<${baseUrl}>`))
          .length === 1
    );
    if (startIdx === -1) {
      console.warn("Subject URI not found.");
      return dataset;
    }

    let endIdx = startIdx + 1;
    while (endIdx < lines.length && !lines[endIdx].trim().endsWith("."))
      endIdx++;
    if (endIdx >= lines.length) {
      console.warn("Block terminator '.' not found.");
      return dataset;
    }

    const lastLine = lines[endIdx];
    const updatedLastLine = lastLine.replace(/\s*\.\s*$/, ";");
    const newTriple = `  ${predicate} <${newImageUrl}> .`;

    const updatedBlock = [
      ...lines.slice(startIdx, endIdx),
      updatedLastLine,
      newTriple,
    ];

    return [
      ...lines.slice(0, startIdx),
      ...updatedBlock,
      ...lines.slice(endIdx + 1),
    ].join("\n");
  }
}

export const handleUpdateDatasetFair = async (
  principleScores: {
    [key: string]: { total: number; passed: number };
  },
  guid: string,
  dataset: string
) => {
  try {
    const newValues: { [key: string]: number | string } = {
      ametrics: "0.0",
      fmetrics: "0.0",
      imetrics: "0.0",
      rmetrics: "0.0",
    };
    const calculateScore = (passed: number, total: number) =>
      Math.round((passed / total) * 1000) / 1000 || "0.0";

    Object.keys(principleScores).forEach((principle) => {
      const score = calculateScore(
        principleScores[principle].passed,
        principleScores[principle].total
      );
      switch (principle) {
        case "A":
          newValues.ametrics = score;
          break;
        case "F":
          newValues.fmetrics = score;
          break;
        case "I":
          newValues.imetrics = score;
          break;
        case "R":
          newValues.rmetrics = score;
          break;
      }
    });

    const newDataset = dataset
      .replace(
        /<http:\/\/fairdatapoint\.org\/ametrics>\s[\d.]+;/,
        `<http://fairdatapoint.org/ametrics> ${
          newValues.ametrics === 1 ? "1.0" : newValues.ametrics
        };`
      )
      .replace(
        /<http:\/\/fairdatapoint\.org\/fmetrics>\s[\d.]+;/,
        `<http://fairdatapoint.org/fmetrics> ${
          newValues.fmetrics === 1 ? "1.0" : newValues.fmetrics
        };`
      )
      .replace(
        /<http:\/\/fairdatapoint\.org\/imetrics>\s[\d.]+;/,
        `<http://fairdatapoint.org/imetrics> ${
          newValues.imetrics === 1 ? "1.0" : newValues.imetrics
        };`
      )
      .replace(
        /<http:\/\/fairdatapoint\.org\/rmetrics>\s[\d.]+\s./,
        `<http://fairdatapoint.org/rmetrics> ${
          newValues.rmetrics === 1 ? "1.0" : newValues.rmetrics
        } .`
      );

    await updateDataset(newDataset, guid);
  } catch (error) {
    console.error("Error updating dataset", error);
  }
};
