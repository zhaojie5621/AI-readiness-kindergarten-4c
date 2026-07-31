# Reproducibility Guide

## Recommended execution order

1. Create the software environment.
2. Place permitted input files according to `data/README.md`.
3. Run `01_airpac_analysis.ipynb`.
4. Run `02_vietnam_ece_analysis.ipynb`.
5. Run `03_china_evidence_synthesis.ipynb`.
6. Run `04_cross_study_synthesis.ipynb`.
7. Compare generated outputs with the manuscript and Supplementary Material.

## Reproducibility controls

- Fixed random seeds
- Documented package versions
- Explicit input and output paths
- Saved model diagnostics
- Fold-level predictive results
- Machine-readable output tables
- No respondent-level pooling
- Non-identifying public outputs

## Environment creation

Using pip:

```bash
pip install -r requirements.txt
```

Using Conda:

```bash
conda env create -f environment.yml
conda activate ai-readiness-4c
```
