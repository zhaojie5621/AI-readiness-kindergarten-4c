# AI Readiness in Kindergarten Education: 4C Framework

This repository contains the reproducibility materials for the manuscript:

**Artificial Intelligence Readiness and Professional Development Priorities in Chinese Kindergarten Education: Triangulating Evidence with SEM and Explainable Machine Learning**

## Evidence streams

The project integrates three independent evidence streams:

1. Five Chinese empirical studies, with a combined descriptive sample of 2,564 participants;
2. AIRPAC-Q data from 528 Chinese pre-service teachers;
3. Vietnam ECE data from 426 in-service early-childhood teachers.

Respondent-level datasets are analysed separately and are never pooled.

## 4C framework

- **Competence:** AI literacy, capability, knowledge, and skills;
- **Confidence:** confidence, acceptance, and intention-related readiness;
- **Caution:** risk, privacy, security, and responsible-use considerations;
- **Context:** prior experience, institutional conditions, platforms, and professional development.

## Repository structure

```text
.github/          GitHub Actions workflow
data/             Codebooks, templates, and data-placement instructions
docs/             Analytical decisions and reproducibility documentation
inputs/           Study-level evidence and construct-mapping templates
notebooks/        Main analytical notebooks
outputs/          Tables, figures, workbooks, and diagnostics
scripts/          Execution and repository-audit utilities
src/              Reusable analytical modules
supplementary/    Supplementary tables and figure-source data
```

## Notebook order

1. `01_airpac_analysis.ipynb`
2. `02_vietnam_ece_analysis.ipynb`
3. `03_china_evidence_synthesis.ipynb`
4. `04_cross_study_synthesis.ipynb`

The Vietnam explanatory model is described as **observed-variable path analysis**, not latent-variable SEM.

## Environment

Install dependencies with:

```bash
pip install -r requirements.txt
```

or:

```bash
conda env create -f environment.yml
```

Run the repository audit with:

```bash
python scripts/audit_repository.py
```

## Data availability

Restricted respondent-level records are not included in the public repository. Public materials are limited to non-identifying codebooks, templates, aggregate outputs, analytical code, and reproducibility documentation.

## Release status

The repository currently contains controlled templates and placeholders. A public `v1.0.0` release and Zenodo DOI should be created only after all notebooks, codebooks, analytical outputs, tables, figures, and supplementary files are verified against the final manuscript.

## Licence

Code is released under the MIT License. Dataset access and reuse remain subject to the licences, consent conditions, and permissions of the original data sources.
