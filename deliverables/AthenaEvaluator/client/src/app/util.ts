import tests from "@/constants/tests";
import { ApiResponseItem, ResponseItem } from "@/constants/types";

export async function generateData(
  uri: string,
  selectedTests: string[],
  onSuccess: VoidFunction
) {
  if (!uri) {
    alert("Por favor, insira uma URI.");
    return;
  }

  if (selectedTests.length === 0) {
    alert("Por favor, selecione ao menos um teste.");
    return;
  }

  const payload = {
    subject: uri,
    tests: selectedTests,
  };

  try {
    const response = await fetch(`${process.env.SERVER_URL}/proxy`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.statusText}`);
    }

    const data = await response.json();

    // Exibir os resultados processados
    const processedData = processApiResponse(data);
    onSuccess();
    return processedData;
  } catch (error) {
    console.error("Erro ao chamar a API:", error);
    throw error;
  }
}

function processApiResponse(data: ApiResponseItem[][]) {
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
    group.forEach((item) => {
      const test = item["@id"]?.split("//tests/")[1]?.split("#")[0];
      const result = {
        id: item["@id"] || null,
        test: test || null,
        type: item["@type"] ? item["@type"].join(", ") : null,
        score:
          item["http://semanticscience.org/resource/SIO_000300"]?.[0]?.[
            "@value"
          ] || null,
        date:
          item["http://purl.obolibrary.org/obo/date"]?.[0]?.["@value"] || null,
        softwareVersion:
          item["http://schema.org/softwareVersion"]?.[0]?.["@value"] || null,
        relatedUri:
          item["http://semanticscience.org/resource/SIO_000332"]?.[0]?.[
            "@id"
          ] || null,
        comments:
          item["http://schema.org/comment"]?.[0]?.["@value"].replace(
            /\n/g,
            "<br/>"
          ) || null,
        principle: test ? tests[test]?.principle || null : null,
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
      // mode: "no-cors", // Adicionado para evitar o erro de CORS
      headers: { Accept: "text/turtle" },
    });

    return response.text(); // Note que com 'no-cors', a resposta pode ser opaca
  } catch (error) {
    console.log("ERRO AO RECUPERAR O DATASET: ", error);
    window.alert(
      "Erro ao recuperar o dataset. Verifique o console para mais detalhes."
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
    console.log("ERRO AO ATUALIZAR O DATASET: ", error);
    window.alert(
      "Erro ao atualizar o dataset. Verifique o console para mais detalhes."
    );
    throw error;
  }
}

export const uploadGraphImage = async (base64Image: string, name?: string) => {
  const response = await fetch(`${process.env.SERVER_URL}/upload-image`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      image: base64Image,
      name: name || "evaluation",
      fileName: "fair-evaluation.png",
    }),
  });

  const data = await response.json();
  if (response.ok) {
    return data.url;
  } else {
    console.error("Erro:", data.error);
  }
};

export async function evaluateDataset(dataset: string, doi?: string) {
  try {
    const response = await fetch(`${process.env.SERVER_URL}/evaluate`, {
      method: "POST",
      headers: {
        Accept: "text/turtle",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ dataset, doi }),
    });
    if (!response.ok) {
      throw new Error("Erro ao avaliar o dataset");
    }
    return response.json();
  } catch (error) {
    console.log("ERRO AO AVALIAR O DATASET: ", error);
    window.alert(
      "Erro ao avaliar o dataset. Verifique o console para mais detalhes."
    );
    throw error;
  }
}

export async function calculatePrincipleScores(responses: ResponseItem[]) {
  const principleScores: {
    [key: string]: { total: number; passed: number };
  } = {};

  responses.forEach((item) => {
    if (item.principle) {
      if (!principleScores[item.principle]) {
        principleScores[item.principle] = { total: 0, passed: 0 };
      }
      principleScores[item.principle].total += 1;
      if (item.score && item.score > 0) {
        principleScores[item.principle].passed += 1;
      }
    }
  });

  return principleScores;
}

export async function login(guid: string, email: string, password: string) {
  if (!guid || !email || !password) {
    alert("Por favor, preencha URI, Usuário e Senha.");
    return;
  }

  const baseUrl = new URL(guid).origin; // Extrai a base da URL fornecida
  const loginUrl = `${baseUrl}/tokens`; // Constrói a URL de login

  try {
    const response = await fetch(loginUrl, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error("Falha ao autenticar.");
    }

    const data = await response.json();

    localStorage.setItem(
      "auth",
      JSON.stringify({
        session: {
          token: data.token,
          baseUrl: baseUrl, // Armazena a URL associada ao token
        },
      })
    );
    alert("Autenticado com sucesso!");
    return data.token;
  } catch (error) {
    console.error("Erro no login:", error);
    alert("Erro ao autenticar. Verifique suas credenciais e tente novamente.");
  }
}

export function updateEvaluationResult(
  baseUrl: string,
  dataset: string,
  newImageUrl: string
): string {
  const predicate = `<http://fairdatapoint.org/evaluationResult>`;

  // Encontra a URI principal do dataset com base na linha que define o tipo como Dataset
  const datasetUriMatch = [
    ...dataset.matchAll(/^<([^>]+)>\s+a\s+[^.]*dcat:Dataset[^.]*;/gm),
  ];

  if (!datasetUriMatch.length) {
    console.warn("Não foi possível identificar a URI do dataset.");
    return dataset;
  }

  const datasetUri = datasetUriMatch[0][1];
  console.log("datasetUri", datasetUri);

  const hasEvaluationResult = dataset.includes(predicate);

  if (hasEvaluationResult) {
    // Substitui a URL existente do evaluationResult
    const updated = dataset.replace(
      /<http:\/\/fairdatapoint\.org\/evaluationResult>\s*<[^>]+>([.;])/,
      (_match, endingChar) => {
        const end = endingChar === ";" ? ";" : " .";
        return `<http://fairdatapoint.org/evaluationResult> <${newImageUrl}>${end}`;
      }
    );

    return updated;
  } else {
    const lines = dataset.split("\n");

    // 1. Localiza a linha que inicia o bloco do subject
    const startIdx = lines.findIndex(
      (line, index) =>
        line.trim().startsWith(`<${baseUrl}>`) &&
        lines.slice(0, index).filter((l) => l.trim().startsWith(`<${baseUrl}>`))
          .length === 1
    );
    if (startIdx === -1) {
      console.warn("Subject URI não encontrado.");
      return dataset;
    }

    // 2. Encontra o final do bloco: primeira linha depois do início que termina com ponto (.)
    let endIdx = startIdx + 1;
    while (endIdx < lines.length && !lines[endIdx].trim().endsWith(".")) {
      endIdx++;
    }

    if (endIdx >= lines.length) {
      console.warn("Não foi encontrado fim de bloco com ponto.");
      return dataset;
    }

    // 3. Garante que a última linha seja convertida de ponto final para ponto e vírgula
    const lastLine = lines[endIdx];
    const updatedLastLine = lastLine.replace(/\s*\.\s*$/, ";");
    const newTriple = `  ${predicate} <${newImageUrl}> .`;

    // 4. Constrói novo bloco com a tripla adicionada
    const updatedBlock = [
      ...lines.slice(startIdx, endIdx),
      updatedLastLine,
      newTriple,
    ];

    // 5. Junta tudo
    return [
      ...lines.slice(0, startIdx),
      ...updatedBlock,
      ...lines.slice(endIdx + 1),
    ].join("\n");
  }
}

export const handleUpdateDatasetFair = async (
  principleScores: {
    [key: string]: {
      total: number;
      passed: number;
    };
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
    const calculateScore = (passed: number, total: number) => {
      return Math.round((passed / total) * 1000) / 1000 || "0.0";
    };
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
    console.error("Erro ao atualizar o dataset", error);
  }
};
