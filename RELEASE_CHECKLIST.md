# Repository Release Checklist

Use this checklist before creating the public `v1.0.0` release.

## Manuscript alignment

- [ ] Manuscript title matches `README.md` and `CITATION.cff`.
- [ ] Final author order is confirmed.
- [ ] All ORCID identifiers are verified.
- [ ] Corresponding-author details are correct.
- [ ] Journal, year, volume, pages, and article DOI are added when available.
- [ ] Statistical terminology matches the final manuscript.
- [ ] Vietnam analysis is consistently described as observed-variable path analysis.
- [ ] All numerical checkpoints match the manuscript and Supplementary Material.
- [ ] Leading zeros and statistical notation are consistent.

## Data governance

- [ ] No restricted respondent-level data are publicly available.
- [ ] No direct identifiers are present.
- [ ] Data licences and redistribution permissions are documented.
- [ ] Expected filenames and local placement instructions are complete.
- [ ] Public outputs are non-identifying.
- [ ] File metadata have been checked for sensitive information.

## Reproducibility

- [ ] All notebooks run in the documented order.
- [ ] Fixed random seeds are used.
- [ ] Package versions are frozen.
- [ ] All manuscript tables are reproducible.
- [ ] All manuscript figures are reproducible.
- [ ] Supplementary tables are machine-readable.
- [ ] Figure-source data are provided.
- [ ] Model diagnostics are preserved.
- [ ] Cross-validation outputs are preserved.
- [ ] Sensitivity analyses are reproducible.

## Repository quality

- [ ] `.gitignore` is correctly named and active.
- [ ] No temporary Office files are present.
- [ ] No credentials, API keys, or local paths are exposed.
- [ ] GitHub Actions validation passes.
- [ ] README links work.
- [ ] Repository structure matches the documented layout.
- [ ] `CITATION.cff` passes GitHub validation.
- [ ] Licence scope is clear.

## Archiving and release

- [ ] Create a GitHub release tagged `v1.0.0`.
- [ ] Connect the repository to Zenodo.
- [ ] Archive the final release.
- [ ] Add the Zenodo DOI to `README.md` and `CITATION.cff`.
- [ ] Cite the repository DOI in the manuscript data/code availability statement.
