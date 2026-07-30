# AI Readiness in Kindergarten Education: 4C Framework

Reproducible analyses, source code, and supporting resources for the study:

**Artificial Intelligence Readiness and Professional Development Priorities in Chinese Kindergarten Education: Triangulating Evidence with SEM and Explainable Machine Learning**

## Project overview

This repository supports a multi-source investigation of artificial intelligence readiness and professional-development priorities in early-childhood education. The study introduces the **Competence–Confidence–Caution–Context (4C) framework** and integrates three independent evidence streams:

1. Five empirical studies of Chinese preschool/kindergarten personnel.
2. The AIRPAC-Q dataset of 528 Chinese pre-service teachers.
3. A dataset of 426 in-service early-childhood teachers in Vietnam.

The respondent-level datasets were analyzed independently. No row-level pooling was conducted, and no cross-dataset measurement invariance was assumed.

## Main objectives

- Examine competence, confidence, caution, and contextual factors associated with AI readiness.
- Compare model-based explanatory results with out-of-sample machine-learning prediction.
- Identify readiness and support profiles within each respondent-level dataset.
- Map recurring profile archetypes across independent evidence streams.
- Derive differentiated professional-development and policy priorities.
- Provide transparent, reproducible, and non-identifying analytical outputs.

## Evidence architecture

| Evidence stream | Population | Main analytical role |
|---|---|---|
| Direct Chinese evidence | Four teacher studies and one principal study; 2,564 analyzed participants | Population-specific evidence synthesis |
| AIRPAC-Q | 528 Chinese pre-service teachers | China-context analysis of AI literacy, risk perception, academic confidence, and future AI-use intention |
| Vietnam ECE | 426 in-service early-childhood teachers | Occupational-context analysis of platform value, professional-development benefit, privacy, barriers, and AI acceptance |

## Analytical methods

The repository documents the following methods:

- construct harmonization and structured evidence synthesis;
- reliability analysis;
- confirmatory factor analysis;
- structural equation modeling;
- bootstrap mediation;
- observed-variable path analysis;
- Gaussian mixture modeling;
- cross-validated machine learning;
- permutation importance;
- profile mapping;
- evidence-convergence scoring;
- Borda rank aggregation;
- sensitivity analysis.

## Repository structure

```text
ai-readiness-kindergarten-4c/
│
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── environment.yml
├── .gitignore
│
├── notebooks/
│   ├── 01_airpac_analysis.ipynb
│   ├── 02_vietnam_ece_analysis.ipynb
│   ├── 03_china_evidence_synthesis.ipynb
│   └── 04_cross_study_synthesis.ipynb
│
├── src/
│   ├── airpac_analysis.py
│   ├── vietnam_analysis.py
│   ├── profile_analysis.py
│   ├── machine_learning.py
│   └── cross_study_synthesis.py
│
├── data/
│   ├── README.md
│   ├── codebooks/
│   ├── templates/
│   └── processed/
│
├── inputs/
│   ├── china_evidence_register/
│   └── construct_crosswalk/
│
├── outputs/
│   ├── tables/
│   ├── figures/
│   ├── excel/
│   └── diagnostics/
│
├── supplementary/
│   ├── supplementary_tables/
│   └── figure_source_data/
│
└── docs/
    ├── construct_crosswalk.md
    ├── analysis_decisions.md
    ├── data_dictionary.md
    └── reproducibility_guide.md
```

## Reproduction order

Run the notebooks in the following order:

1. `01_airpac_analysis.ipynb`
2. `02_vietnam_ece_analysis.ipynb`
3. `03_china_evidence_synthesis.ipynb`
4. `04_cross_study_synthesis.ipynb`

The first two notebooks reproduce the respondent-level analyses. The third reconstructs the direct Chinese evidence register and construct mapping. The fourth integrates study-level outputs without pooling respondent records.

## Data availability and restrictions

This repository does **not** automatically redistribute all source datasets.

- AIRPAC-Q materials may be included or linked according to their repository licence.
- Vietnam respondent-level files will not be uploaded unless redistribution permission is confirmed.
- When redistribution is restricted, the repository will provide source links, file-provenance information, checksums where feasible, expected filenames, and scripts that operate on locally supplied files.
- Public outputs exclude direct identifiers.
- The repository does not contain names, email addresses, institutional identifiers, authentication credentials, or other sensitive information.

See `data/README.md` for acquisition and placement instructions.

## Reproducibility

The analytical workflow uses:

- fixed random seeds;
- documented package versions;
- explicit file paths;
- saved model diagnostics;
- fold-level predictive results;
- machine-readable tables;
- non-identifying processed outputs;
- versioned releases.

The Python environment can be recreated using either:

```bash
pip install -r requirements.txt
```

or:

```bash
conda env create -f environment.yml
```

## Main outputs

The repository will reproduce:

- measurement and structural-model results;
- mediation estimates;
- AIRPAC-Q readiness profiles;
- Vietnam ECE readiness and support profiles;
- machine-learning performance comparisons;
- predictor-importance results;
- cross-study effect register;
- evidence-convergence matrix;
- professional-development priority ranking;
- manuscript and supplementary figures;
- machine-readable supplementary tables.

## Important interpretation boundaries

- The three evidence streams are complementary but not population-equivalent.
- Respondent records were not pooled.
- Cross-source profile mappings are conceptual analogies, not statistically equivalent latent classes.
- Cross-sectional associations do not establish causality.
- The 4C framework is an integrative organizing structure, not a validated cross-national measurement instrument.
- The professional-development priority index is exploratory.
- Domain-specific Vietnam barrier and training items should not be generalized to all forms of kindergarten AI implementation.

## Citation

A machine-readable citation file will be provided in `CITATION.cff`.

Until the final bibliographic details and DOI are available, cite the associated manuscript as:

> Kumar, R., et al. (2026). *Artificial intelligence readiness and professional development priorities in Chinese kindergarten education: Triangulating evidence with SEM and explainable machine learning*. Manuscript under preparation.

The citation will be updated when the article and repository receive permanent identifiers.

## Licence

The code licence will be specified in the `LICENSE` file. Dataset licences remain separate and must be respected independently.

## Repository status

**Current status:** Private analytical preparation.

Planned release stages:

- `v0.1.0` — repository structure and documentation;
- `v0.2.0` — notebooks, source code, and non-identifying outputs;
- `v0.9.0` — submission-ready reproducibility package;
- `v1.0.0` — public archived release.

## Contact

For questions regarding the analytical workflow or repository materials, contact:

**Raman Kumar**  
Assistant Professor, Department of Mechanical and Production Engineering  
Guru Nanak Dev Engineering College, Ludhiana, India  

Email: `[ADD PUBLIC CORRESPONDING-AUTHOR EMAIL BEFORE RELEASE]`

---

This repository should be cited together with the associated article once the final publication and archive DOI become available.
