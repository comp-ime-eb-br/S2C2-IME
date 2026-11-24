// getDatasetsFromRDF.ts
import { Parser, Quad, NamedNode } from "n3";

const LDP_CONTAINS = "http://www.w3.org/ns/ldp#contains";
const RDF_TYPE = "http://www.w3.org/1999/02/22-rdf-syntax-ns#type";
const LDP_DIRECT_CONTAINER = "http://www.w3.org/ns/ldp#DirectContainer";

// util.ts (adicione perto do topo)
export const POLAR_PARAMS = [
  // fair general
  // "F",
  // "A",
  // "I",
  // "R",
  // FAIR
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
  // General Evaluation
  "anonymization",
  "availability",
  "labeling",
  "timeliness",
  "relevance",
  // Specific Evaluation
  "attackDiversity",
  "networkConfigurationCompleteness",
  "normalAndAttackTraffic",
] as const;

export type PolarParam = (typeof POLAR_PARAMS)[number];

/**
 * Extrai a lista de URIs do ldp:contains a partir de um RDF/Turtle.
 * - Se "containerUri" for informado, filtra apenas o contains desse sujeito.
 * - Se não for informado, pega o(s) sujeito(s) que são ldp:DirectContainer.
 */
export function getDatasetsFromRDF(
  rdfText: string,
  containerUri?: string
): string[] {
  const parser = new Parser();
  const quads: Quad[] = parser.parse(rdfText);

  // Se não foi passado um container específico, descubra quem é DirectContainer
  const candidateSubjects = new Set<string>();
  if (containerUri) {
    candidateSubjects.add(containerUri);
  } else {
    for (const q of quads) {
      if (
        q.predicate.value === RDF_TYPE &&
        q.object.value === LDP_DIRECT_CONTAINER
      ) {
        candidateSubjects.add(q.subject.value);
      }
    }
  }

  // Colete objetos do ldp:contains desses sujeitos
  const results = new Set<string>();
  for (const q of quads) {
    if (q.predicate.value === LDP_CONTAINS) {
      if (
        candidateSubjects.size === 0 ||
        candidateSubjects.has(q.subject.value)
      ) {
        results.add(q.object.value);
      }
    }
  }

  return Array.from(results);
}

// fairScores.ts
const FDP_BASE = "http://fairdatapoint.org/";
const XSD_INT = "http://www.w3.org/2001/XMLSchema#integer";
const XSD_DEC = "http://www.w3.org/2001/XMLSchema#decimal";
const XSD_FLOAT = "http://www.w3.org/2001/XMLSchema#float";
const XSD_DOUBLE = "http://www.w3.org/2001/XMLSchema#double";

function iriToParam(iri: string): string | null {
  if (!iri.startsWith(FDP_BASE)) return null;
  return iri.substring(FDP_BASE.length);
}

function parseNumericLiteral(q: Quad): number | null {
  if (q.object.termType !== "Literal") return null;

  // aceita número sem datatype ou com xsd numérico
  const dt = q.object.datatype?.value;
  const raw = q.object.value.trim();

  const isNumericDT =
    !dt ||
    dt === XSD_INT ||
    dt === XSD_DEC ||
    dt === XSD_FLOAT ||
    dt === XSD_DOUBLE;

  if (!isNumericDT) return null;

  // aceita inteiros/decimais: "1", "1.0"
  const n = Number(raw);
  return Number.isFinite(n) ? n : null;
}

/**
 * Busca as notas dos parâmetros http://fairdatapoint.org/{param} presentes no RDF.
 * @param datasetUrl URL do dataset que retorna Turtle
 * @param expectedParams lista opcional de parâmetros esperados; se fornecida, completa ausentes com null
 * @returns Record<param, number|null>
 */
// util/fairScores.ts
export async function fetchFairParamScores(
  datasetUrl: string,
  expectedParams?: string[]
): Promise<Record<string, number | null>> {
  const res = await fetch(datasetUrl, { headers: { Accept: "text/turtle" } });
  if (!res.ok)
    throw new Error(`Falha ao buscar RDF (${res.status} ${res.statusText})`);
  const ttl = await res.text();

  const parser = new Parser();
  const quads = parser.parse(ttl);

  const found: Record<string, number> = {};
  for (const q of quads) {
    const param = iriToParam(q.predicate.value);
    if (!param) continue;
    const num = parseNumericLiteral(q);
    if (num === null) continue;
    if (!(param in found)) found[param] = num;
  }

  if (expectedParams?.length) {
    const completed: Record<string, number | null> = {};
    for (const p of expectedParams) completed[p] = p in found ? found[p] : null;
    return completed;
  }
  return found;
}

const DCTERMS_TITLE = "http://purl.org/dc/terms/title";

// export async function fetchDatasetTitle(
//   datasetUrl: string
// ): Promise<string | null> {
//   const res = await fetch(datasetUrl, { headers: { Accept: "text/turtle" } });
//   if (!res.ok) return null;
//   const ttl = await res.text();

//   const parser = new Parser();
//   const quads: Quad[] = parser.parse(ttl);

//   // pega o primeiro literal encontrado em dcterms:title
//   for (const q of quads) {
//     if (
//       q.predicate.value === DCTERMS_TITLE &&
//       q.object.termType === "Literal"
//     ) {
//       return q.object.value; // ignora duplicatas/idiomas, usa o primeiro
//     }
//   }
//   return null;
// }

/** Dedupe simples pra evitar bater duas vezes no mesmo dataset */
export async function fetchTitlesForDatasets(
  datasetUrls: string[]
): Promise<Array<{ uri: string; title: string | null }>> {
  const uniq = Array.from(new Set(datasetUrls));
  const results = await Promise.all(
    uniq.map(async (uri) => ({ uri, title: await fetchDatasetTitle(uri) }))
  );
  return results;
}

// util/buildUiRow.ts

export type UiRow = {
  id: string;
  uri: string;
  title: string;
  overallScore: number; // 0-100
  principleScores: { A: number; F: number; I: number; R: number }; // 0-100
  /** valores crus por parâmetro (0-100 int ou null) para o radar */
  scoresByParam: Record<PolarParam, number | null>;
};

// regra simples: prefixo da chave indica o princípio
function paramToPrinciple(param: string): "A" | "F" | "I" | "R" | "Cyber" {
  const first = param[0]?.toLowerCase();
  const second = param[1]?.toLowerCase();
  if (first === "a" && second !== undefined && /^[0-9]$/.test(second))
    return "A";
  if (first === "f" && second !== undefined && /^[0-9]$/.test(second))
    return "F";
  if (first === "i" && second !== undefined && /^[0-9]$/.test(second))
    return "I";
  if (first === "r" && second !== undefined && /^[0-9]$/.test(second))
    return "R";
  return "Cyber"; // default fallback
}

// util/buildUiRow.ts
function normalize0to100Int(n: number): number {
  // heurística: se <= 1 assume 0..1; se <= 2 assume 0..2; senão assume já 0..100
  let x = n;
  if (n <= 1) x = n * 100;
  else if (n <= 2) x = (n / 2) * 100;
  // clamp e arredonda
  const clamped = Math.max(0, Math.min(100, x));
  return Math.round(clamped);
}

export async function buildUiRowFromDataset(
  uri: string
): Promise<UiRow | null> {
  const title = (await fetchDatasetTitle(uri)) ?? uri;

  // agora pedimos explicitamente os parâmetros do radar
  const rawScores = await fetchFairParamScores(uri, [...POLAR_PARAMS]);

  console.log("rawScores for", title, rawScores);

  // mapear para Record<PolarParam, number|null> com normalização 0-100 int
  const scoresByParam = {} as Record<PolarParam, number | null>;
  const values: number[] = [];
  const perPrinciple: Record<"A" | "F" | "I" | "R" | "Cyber", number[]> = {
    A: [],
    F: [],
    I: [],
    R: [],
    Cyber: [],
  };

  for (const p of POLAR_PARAMS) {
    const v = rawScores[p];
    const norm = v == null ? null : normalize0to100Int(v);
    scoresByParam[p] = norm;

    console.log(`  param ${p}: raw=${v} norm=${norm}`);

    if (norm != null) {
      // regra de princípio pelo prefixo (já existente)
      const princ = paramToPrinciple(p);
      perPrinciple[princ].push(norm);
      values.push(norm);
    }
  }

  const overallScore = values.length
    ? Math.round(values.reduce((a, b) => a + b, 0) / values.length)
    : 0;

  const principleScores = (["A", "F", "I", "R"] as const).reduce(
    (acc, k) => {
      const arr = perPrinciple[k];
      acc[k] = arr.length
        ? Math.round(arr.reduce((a, b) => a + b, 0) / arr.length)
        : 0;
      return acc;
    },
    { A: 0, F: 0, I: 0, R: 0 } as UiRow["principleScores"]
  );

  return { id: uri, uri, title, overallScore, principleScores, scoresByParam };
}

const RDFS_LABEL = "http://www.w3.org/2000/01/rdf-schema#label";
const DCAT_DATASET = "http://www.w3.org/ns/dcat#Dataset";

const PREFERRED_LANGS = ["pt", "en", ""]; // '' = sem tag

function sameResource(a: string, b: string) {
  // compara normalizando trailing slash
  const norm = (u: string) => u.replace(/\/+$/, "");
  return norm(a) === norm(b);
}

function pickBestLiteral(quads: Quad[], predicateIri: string): string | null {
  // coleta todos os literais desse predicado
  const lits = quads
    .filter(
      (q) =>
        q.predicate.value === predicateIri && q.object.termType === "Literal"
    )
    .map((q) => {
      const literal = q.object as import("n3").Literal;
      return { value: literal.value, lang: literal.language ?? "" };
    });

  if (!lits.length) return null;

  // ordena por preferência de idioma (pt > en > sem tag)
  lits.sort((a, b) => {
    const ai = PREFERRED_LANGS.indexOf(a.lang);
    const bi = PREFERRED_LANGS.indexOf(b.lang);
    return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
  });

  return lits[0].value;
}

export async function fetchDatasetTitle(
  datasetUri: string
): Promise<string | null> {
  const res = await fetch(datasetUri, { headers: { Accept: "text/turtle" } });
  if (!res.ok) return null;
  const ttl = await res.text();

  const parser = new Parser();
  const quads: Quad[] = parser.parse(ttl);

  // 1) Tentar pegar título exatamente do sujeito == datasetUri
  const subjectQuads = quads.filter((q) =>
    sameResource(q.subject.value, datasetUri)
  );
  let title =
    pickBestLiteral(subjectQuads, DCTERMS_TITLE) ??
    pickBestLiteral(subjectQuads, RDFS_LABEL);
  if (title) return title;

  // 2) Fallback: algum sujeito que seja dcat:Dataset
  const datasetSubjects = new Set<string>();
  for (const q of quads) {
    if (
      q.predicate.value === RDF_TYPE &&
      q.object.value === DCAT_DATASET &&
      q.subject.termType === "NamedNode"
    ) {
      datasetSubjects.add((q.subject as NamedNode).value);
    }
  }

  for (const subj of datasetSubjects) {
    const qs = quads.filter((q) => q.subject.value === subj);
    title =
      pickBestLiteral(qs, DCTERMS_TITLE) ?? pickBestLiteral(qs, RDFS_LABEL);
    if (title) return title;
  }

  // 3) Nada encontrado
  return null;
}
