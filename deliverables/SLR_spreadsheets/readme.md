# RSL_SoS_Data — Extraction Data for the Systematic Literature Review

> **Paper:** *Interoperability Mechanisms for System-of-Systems: A Systematic Literature Review*
> **Authors:** Thyago Ferreira Vieira, Ronaldo R. Goldschmidt, Maria C. R. Cavalcanti, Ricardo Choren
> **Institution:** Instituto Militar de Engenharia (IME), Rio de Janeiro, Brazil
> **Target venue:** IEEE Access (submitted 2026)

---

## Overview

This repository contains the structured data extraction spreadsheet produced during the Systematic Literature Review (SLR) on interoperability and integration mechanisms in Systems-of-Systems (SoS) architectures. The data supports full reproducibility of the quantitative results reported in the paper, including Tables 7, 8, and 9.

The SLR followed the methodological guidelines of Kitchenham and Charters and the PRISMA 2020 checklist. Searches were conducted across six digital libraries (ACM, IEEE Xplore, Scopus, SpringerLink, Web of Science, Wiley) covering the period from January 2016 to October 2025, yielding **56 primary studies** after screening and quality assessment.

---

## File: `RSL_SoS_Data.xlsx`

The spreadsheet contains three worksheets described below.

---

### Sheet 1 — Primary Studies

Contains the full classification of all 56 primary studies (P1–P56) extracted during the review.

| Column | Description |
|---|---|
| **ID** | Study identifier (P1 to P56) used throughout the paper |
| **First Author** | Last name of the first author followed by "et al." for multi-author works |
| **Year** | Publication year. "N/A" indicates year not available |
| **Domain** | Application domain of the SoS addressed in the study (see legend below) |
| **Mechanism** | Primary mediation mechanism proposed or employed (see legend below) |
| **Pattern** | Architectural organizational pattern identified in the study (see legend below) |
| **Validation** | Type of validation or evaluation presented in the study (see legend below) |
| **Notes** | Additional remarks, e.g., unpublished manuscripts or alternative titles |

Classifications were verified against the actual PDF content (abstracts and evaluation sections) of each primary study.

---

### Sheet 2 — Distribution

Marginal frequency distributions for each classification dimension, corresponding to **Table 8** of the paper.

| Section | Description |
|---|---|
| **Domain** | Count and percentage of studies per application domain |
| **Mechanism** | Count and percentage of studies per mediation mechanism family |
| **Pattern** | Count and percentage of studies per architectural pattern |
| **Validation** | Count and percentage of studies per validation type |

> **Note:** Domains with two or fewer studies (Space, Surveillance, Smart City, Robotics) are consolidated under "Other" in the paper's Table 8 for readability. The full breakdown is available in Sheet 3.

---

### Sheet 3 — Cross-tabulation

Domain × Mechanism cross-tabulation for all 10 domains and 5 mechanism families, corresponding to **Table 9** of the paper. Dominant mechanism per domain is highlighted in yellow.

Notable patterns identified:

- **Defense (n=10):** Agent/MAS dominates (8/10 = 80%), reflecting the need for autonomy and decentralized decision-making in tactical environments.
- **Energy (n=6):** Co-simulation dominates (3/6 = 50%), driven by the need to orchestrate pre-existing physics-based simulation tools.
- **Environment (n=5):** Semantic/Ontological dominates (3/5 = 60%), reflecting the heterogeneity of environmental data sources that requires vocabulary alignment before connectivity.
- **General SoS (n=15):** Model-based slightly exceeds Agent/MAS (7 vs. 6), as generic SoS studies tend to propose abstract architectural models before concrete implementations.

---

## Legends

### Domain

| Code | Full Name | Description |
|---|---|---|
| **Def** | Defense | Military, combat, surveillance, and national security systems |
| **En** | Energy | Power grids, smart grids, energy distribution and management |
| **Tra** | Transportation | Road, air, urban mobility, and vehicular networks |
| **Ind** | Industry | Manufacturing, Industry 4.0, industrial automation, IoT |
| **Gen** | General SoS | Studies proposing generic SoS models without a specific domain |
| **Env** | Environment | Environmental monitoring, water management, marine data |
| **Spa** | Space | Space systems, satellite architectures, aerospace |
| **Sur** | Surveillance | Multi-sensor surveillance and monitoring infrastructures |
| **SC** | Smart City | Urban management, city-scale CPS, smart infrastructure |
| **Rob** | Robotics | Human-robot teaming and robotic system integration |

---

### Mechanism (Mediation Mechanism Family)

| Code | Full Name | Description |
|---|---|---|
| **Ag** | Agent/MAS | Multi-Agent Systems used as mediators between constituent systems |
| **MB** | Model-based | Architectural or behavioral models as the integration backbone |
| **CS** | Co-simulation | Orchestration of independent simulation tools via standard interfaces |
| **Sem** | Semantic/Ontological | Ontologies and shared vocabularies for semantic alignment |
| **MW** | Middleware/Gateway | Protocol translators, ESB, and communication middleware |

---

### Pattern (Architectural Pattern)

| Code | Full Name | Description |
|---|---|---|
| **H** | Hierarchical | Explicit layered organization with local mediators and coordination layers above |
| **D** | Decentralized | Peer-to-peer, fully distributed mediator coordination |
| **Hy** | Hybrid | Combination of hierarchical and decentralized elements |
| **MB** | Model-based | Mediators organized around explicit architectural or behavioral models |

---

### Validation (Validation Type)

| Code | Full Name | Description |
|---|---|---|
| **Sim** | Simulation | Evaluated exclusively through simulation environments |
| **Pro** | Prototype/PoC | Evaluated through a physical or software prototype or proof-of-concept |
| **Con** | Conceptual | Proposed as a conceptual or theoretical contribution without empirical evaluation |

> **Key finding:** No study in the corpus (0/56) reported **field deployment** as its primary validation method. 54% rely on simulation and 23% on prototype evaluation, evidencing a persistent maturity gap between proposed mechanisms and operational environments.

---

## Methodology Summary

| Item | Detail |
|---|---|
| Protocol | Kitchenham & Charters + PRISMA 2020 |
| Search period | January 2016 – October 2025 |
| Databases | ACM (12), IEEE Xplore (144), Scopus (249), SpringerLink (142), Web of Science (132), Wiley (19) |
| Total retrieved | 698 records |
| After deduplication | 533 records |
| After title/abstract screening | 239 records |
| After full-text + QA | 51 studies |
| Added via snowballing | 5 studies |
| **Final corpus** | **56 primary studies** |
| Quality threshold | ≥ 5/8 on the quality assessment checklist |

---

## Citation

If you use this dataset, please cite the original paper:

```
Vieira, T. F., Goldschmidt, R. R., Cavalcanti, M. C. R., & Choren, R. (2026).
Interoperability Mechanisms for System-of-Systems: A Systematic Literature Review.
IEEE Access. (submitted)
```

---

**Corresponding author:** Thyago Ferreira Vieira — thyago.ferreira@ime.eb.br
