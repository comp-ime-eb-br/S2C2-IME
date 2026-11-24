// --- N3 helpers (substitua estes no seu util.ts com N3) ---
import { Parser, Store, Writer, DataFactory } from "n3";
const { namedNode, literal, quad } = DataFactory;

const DEFAULT_PREFIXES: Record<string, string> = {
  dcat: "http://www.w3.org/ns/dcat#",
  dct: "http://purl.org/dc/terms/",
  xsd: "http://www.w3.org/2001/XMLSchema#",
  foaf: "http://xmlns.com/foaf/0.1/",
  rdfs: "http://www.w3.org/2000/01/rdf-schema#",
  sio: "http://semanticscience.org/resource/",
  wd: "https://www.wikidata.org/wiki/",
  ldp: "http://www.w3.org/ns/ldp#",
  f: "http://fairdatapoint.org/",
  n1: "http://purl.org/athena-o#",
  time: "http://www.w3.org/2006/time#",
  gloss: "https://csrc.nist.gov/glossary/",
  fdp: "https://w3id.org/fdp/fdp-o#",
};

async function parseTurtleToStore(
  turtle: string
): Promise<{ store: Store; prefixes: Record<string, string> }> {
  return new Promise((resolve, reject) => {
    const store = new Store();
    const parser = new Parser();
    let collectedPrefixes: Record<string, string> = {};
    try {
      parser.parse(turtle, (error, q, prefixes) => {
        if (error) return reject(error);
        if (q) {
          store.addQuad(q);
        } else {
          collectedPrefixes = prefixes
            ? Object.fromEntries(
                Object.entries(prefixes).map(([k, v]) => [
                  k,
                  typeof v === "string" ? v : v.value,
                ])
              )
            : {};
          resolve({ store, prefixes: collectedPrefixes });
        }
      });
    } catch (err) {
      reject(err);
    }
  });
}

function findDatasetSubject(store: Store): string | null {
  const DCAT = DEFAULT_PREFIXES.dcat;
  const RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#";
  const types = store.getQuads(
    null,
    namedNode(`${RDF}type`),
    namedNode(`${DCAT}Dataset`),
    null
  );
  return types.length ? types[0].subject.value : null;
}

// --- NOVO: escala para inteiro 0..100 ---
function toPercentInt(v: number | undefined): number | undefined {
  if (typeof v !== "number" || !isFinite(v)) return undefined;
  // Se já vier 0..100, só clampa e arredonda; se vier 0..1, converte
  const scaled = v <= 1 ? v * 100 : v;
  return Math.max(0, Math.min(100, Math.round(scaled)));
}

// --- NOVO: upsert como xsd:integer ---
function upsertInteger(
  store: Store,
  subjectIri: string,
  predicateIri: string,
  valueInt: number
) {
  const toRemove = store.getQuads(
    namedNode(subjectIri),
    namedNode(predicateIri),
    null,
    null
  );
  store.removeQuads(toRemove);
  store.addQuad(
    quad(
      namedNode(subjectIri),
      namedNode(predicateIri),
      literal(String(valueInt), namedNode(`${DEFAULT_PREFIXES.xsd}integer`))
    )
  );
}

async function storeToTurtle(
  store: Store,
  existingPrefixes: Record<string, string>
): Promise<string> {
  const prefixes: Record<string, string> = {
    ...DEFAULT_PREFIXES,
    ...existingPrefixes,
  };
  return new Promise((resolve, reject) => {
    const writer = new Writer({ prefixes });
    writer.addQuads(store.getQuads(null, null, null, null));
    writer.end((err, result) => (err ? reject(err) : resolve(result)));
  });
}

const FAIR_SUBPRED_MAP: Record<string, string> = {
  F1: `${DEFAULT_PREFIXES.f}f1`,
  F2: `${DEFAULT_PREFIXES.f}f2`,
  F3: `${DEFAULT_PREFIXES.f}f3`,
  A1: `${DEFAULT_PREFIXES.f}a11`,
  A2: `${DEFAULT_PREFIXES.f}a2`,
  I1: `${DEFAULT_PREFIXES.f}i1`,
  I2: `${DEFAULT_PREFIXES.f}i2`,
  I3: `${DEFAULT_PREFIXES.f}i3`,
  // "R1.1": `${DEFAULT_PREFIXES.f}r11`,
  R1: `${DEFAULT_PREFIXES.f}r11`,
};

const CYBER_PRED_MAP: Record<string, string> = {
  timeliness: `${DEFAULT_PREFIXES.f}timeliness`,
  availability: `${DEFAULT_PREFIXES.f}availability`,
  anonymization: `${DEFAULT_PREFIXES.f}anonymization`,
  labeling: `${DEFAULT_PREFIXES.f}labeling`,
  attackDiversity: `${DEFAULT_PREFIXES.f}attackDiversity`,
  normalAndAttackTraffic: `${DEFAULT_PREFIXES.f}normalAndAttackTraffic`,
  networkCompleteness: `${DEFAULT_PREFIXES.f}networkConfigurationCompleteness`,
  relevance: `${DEFAULT_PREFIXES.f}relevance`,
};

// --- Troque sua updateDatasetWithScoresN3 por esta ---
export async function updateDatasetWithScoresN3(params: {
  dataset: string;
  fairSubprinciples?: Record<string, number> | null;
  cyber?: {
    timeliness?: number;
    availability?: number;
    anonymization?: number;
    labeling?: number;
    attackDiversity?: number;
    normalAndAttackTraffic?: number;
    networkCompleteness?: number;
    relevance?: number;
  } | null;
}): Promise<string> {
  const { dataset, fairSubprinciples, cyber } = params;

  const { store, prefixes } = await parseTurtleToStore(dataset);
  const subject = findDatasetSubject(store);
  if (!subject) {
    console.warn("Dataset subject (dcat:Dataset) não encontrado.");
    return dataset;
  }

  // FAIR subprincípios -> 0..100 int
  if (fairSubprinciples) {
    Object.entries(FAIR_SUBPRED_MAP).forEach(([key, predIri]) => {
      const v = toPercentInt(fairSubprinciples[key]);
      if (typeof v === "number") {
        upsertInteger(store, subject, predIri, v);
      }
    });
  }

  // Cyber -> 0..100 int
  if (cyber) {
    Object.entries(CYBER_PRED_MAP).forEach(([k, predIri]) => {
      const v = toPercentInt((cyber as Record<string, number | undefined>)[k]);
      if (typeof v === "number") {
        upsertInteger(store, subject, predIri, v);
      }
    });
  }

  return storeToTurtle(store, prefixes);
}
