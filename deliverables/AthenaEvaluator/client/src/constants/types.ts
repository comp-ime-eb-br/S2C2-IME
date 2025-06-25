export type PrincipleScores = {
  [key: string]: {
    total: number;
    passed: number;
  };
};

export interface ResponseItem {
  id: string | null;
  test: string | null;
  principle: string | null;
  type: string | null;
  score: number | null;
  date: string | null;
  softwareVersion: string | null;
  relatedUri: string | null;
  comments: string | null;
}

export interface ApiResponseItem {
  "@id"?: string;
  "@type"?: string[];
  "http://semanticscience.org/resource/SIO_000300"?: { "@value": string }[];
  "http://purl.obolibrary.org/obo/date"?: { "@value": string }[];
  "http://schema.org/softwareVersion"?: { "@value": string }[];
  "http://semanticscience.org/resource/SIO_000332"?: { "@id": string }[];
  "http://schema.org/comment"?: { "@value": string }[];
}
