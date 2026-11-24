// util/extractDatasetProps.ts
import { Parser, Quad } from "n3";

const P = {
  yearOfCreation: "http://www.w3.org/2006/time#yearOfCreation",
  availability: "https://csrc.nist.gov/glossary/termpublicAvailability", // "Yes" | "No" | "On request"
  hasLabel: "http://purl.org/athena-o#hasLabel", // "Unlabeled" | "Partially-labeled" | "Fully-labeled"
  anonymity: "https://csrc.nist.gov/glossary/termanonymity", // true | false
  kindOfTraffic: "http://purl.org/athena-o#kindOfTraffic", // "Real" | "Emulated" | "Syntethic"
  normalTraffic: "http://purl.org/athena-o#normalTraffic", // true | false (string "true"/"false")
  attackTraffic: "http://purl.org/athena-o#attackTraffic", // true | false (string "true"/"false")
  attackType: "https://csrc.nist.gov/glossary/termattackType", // "Spoofing", "DDoS, SQLi", ...
  networkConfigurationCompleteness:
    "http://fairdatapoint.org/networkConfigurationCompleteness", // num (0..3)
  doi: "http://fairdatapoint.org/doi",
};

export type DatasetProps = {
  year?: number;
  availability?: "Yes" | "No" | "On request";
  hasLabel?: "Unlabeled" | "Partially-labeled" | "Fully-labeled";
  anonymity?: boolean;
  kindOfTraffic?: "Real" | "Emulated" | "Syntethic";
  normalTraffic?: boolean;
  attackTraffic?: boolean;
  attackList?: string[];
  networkCompleteness?: number; // 0..3
  doi?: string;
};

function sameResource(a: string, b: string) {
  const norm = (u: string) => u.replace(/\/+$/, "");
  return norm(a) === norm(b);
}

export async function extractDatasetProps(
  datasetUri: string
): Promise<DatasetProps> {
  const res = await fetch(datasetUri, { headers: { Accept: "text/turtle" } });
  if (!res.ok) return {};
  const ttl = await res.text();

  const parser = new Parser();
  const quads: Quad[] = parser.parse(ttl);

  // Só considerar triples do próprio dataset
  const S = quads.filter((q) => sameResource(q.subject.value, datasetUri));

  const getLiteral = (pred: string) =>
    S.find((q) => q.predicate.value === pred && q.object.termType === "Literal")
      ?.object.value;

  const getBool = (pred: string): boolean | undefined => {
    const v = getLiteral(pred);
    if (typeof v !== "string") return undefined;
    if (/^true$/i.test(v)) return true;
    if (/^false$/i.test(v)) return false;
    return undefined;
  };

  const yearStr = getLiteral(P.yearOfCreation);
  const availability = getLiteral(P.availability) as
    | DatasetProps["availability"]
    | undefined;
  const hasLabel = getLiteral(P.hasLabel) as
    | DatasetProps["hasLabel"]
    | undefined;
  const anonymity = getBool(P.anonymity);
  const kindOfTraffic = getLiteral(P.kindOfTraffic) as
    | DatasetProps["kindOfTraffic"]
    | undefined;
  const normalTraffic = getLiteral(P.normalTraffic);
  const attackTraffic = getLiteral(P.attackTraffic);
  const attackType = getLiteral(P.attackType);
  const networkCompletenessStr = getLiteral(P.networkConfigurationCompleteness);
  const doi = getLiteral(P.doi);

  // lista de ataques: aceita separado por vírgula/; ou único
  const attackList = attackType
    ? attackType
        .split(/[;,]/)
        .map((s) => s.trim())
        .filter(Boolean)
    : undefined;

  return {
    year: yearStr ? Number(yearStr) : undefined,
    availability,
    hasLabel,
    anonymity,
    kindOfTraffic,
    normalTraffic:
      typeof normalTraffic === "string"
        ? !/^false$/i.test(normalTraffic)
        : undefined,
    attackTraffic:
      typeof attackTraffic === "string"
        ? !/^false$/i.test(attackTraffic)
        : undefined,
    attackList,
    networkCompleteness: networkCompletenessStr
      ? Number(networkCompletenessStr)
      : undefined,
    doi,
  };
}
