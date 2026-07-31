# Reproducibility Guide

## Objective
This repository enables independent reproduction of the analytical workflow used in the associated manuscript.

## Recommended execution order

1. Install Python packages.
2. Create the Conda environment (optional).
3. Prepare the input datasets according to `data/README.md`.
4. Execute notebooks in numerical order.
5. Compare generated outputs with the manuscript tables and figures.

## Workflow

Input Data
→ Data preprocessing
→ Reliability analysis
→ CFA / Path modeling
→ Machine learning
→ Profile analysis
→ Evidence synthesis
→ Tables
→ Figures
→ Manuscript

## Reproducibility principles

- Fixed random seeds
- Version-controlled code
- Non-identifying outputs
- Documented software versions
- Transparent analytical decisions
