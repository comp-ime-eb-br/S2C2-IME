// util/metrics.ts
export function timelinessMetric(year?: number, now = new Date()): number {
  if (!year) return 0;
  const current = now.getFullYear();

  // universo (inteiros)
  // const Umin = 1998;
  const Umax = current + 1;

  const tri = (x: number, [a, b, c]: [number, number, number]) => {
    if (x <= a || x >= c) return 0;
    if (x === b) return 1;
    return x < b ? (x - a) / (b - a) : (c - x) / (c - b);
  };

  const old = tri(year, [1998, 1998, 2007]);
  const medium = tri(year, [2003, 2012, 2019]);
  const recent = tri(year, [2016, Umax, Umax]);

  const maxv = Math.max(old, medium, recent);
  if (maxv === old) return 0;
  if (maxv === medium) return 0.5;
  return 1;
}

export function availabilityMetric(v?: "Yes" | "No" | "On request"): number {
  if (v === "Yes") return 1;
  if (v === "On request") return 0.5;
  return 0; // 'No' ou indefinido
}

export function labelMetric(
  v?: "Unlabeled" | "Partially-labeled" | "Fully-labeled"
): number {
  if (v === "Fully-labeled") return 1;
  if (v === "Partially-labeled") return 0.5;
  return 0; // Unlabeled/indef
}

export function anonymityMetric(
  anonymity?: boolean,
  kindOfTraffic?: "Real" | "Emulated" | "Syntethic"
): number {
  if (!kindOfTraffic || anonymity === undefined) return 0;
  if (kindOfTraffic === "Real") return anonymity ? 1 : 0;
  if (kindOfTraffic === "Emulated") return anonymity ? 0 : 1;
  if (kindOfTraffic === "Syntethic") return anonymity ? 0 : 1;
  return 0;
}

export function attackDiversityMetric(list?: string[]): number {
  if (!list || !list.length) return 0;
  const unique = Array.from(new Set(list.map((s) => s.toLowerCase())));
  return Math.min(1, unique.length / 6); // STRIDE: 6 categorias
}

export function normalAndAttackMetric(
  normalTraffic?: boolean,
  attackTraffic?: boolean
): number {
  const nt = normalTraffic ? 1 : 0;
  const at = attackTraffic ? 1 : 0;
  return (nt + at) / 2;
}

// networkCompleteness (0..3) -> 0..1
export function networkCompletenessMetric(v?: number): number {
  if (typeof v !== "number") return 0;
  return Math.max(0, Math.min(1, v / 3));
}

export function relevanceMetric(
  citations: number | undefined,
  yearScore: number,
  reference = 4000,
  W = 0.3
): number {
  const c = typeof citations === "number" ? citations : 0;
  const partC = Math.min(c / reference, 1);
  return W * partC + (1 - W) * yearScore;
}
