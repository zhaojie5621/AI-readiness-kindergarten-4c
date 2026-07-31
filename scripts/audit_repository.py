"""Audit the repository before a public release.

This script checks structure, common sensitive-file patterns, notebook validity,
and basic citation/configuration consistency. It does not inspect restricted raw
datasets and does not replace a manual privacy review.
"""

from __future__ import annotations

from pathlib import Path
import json
import sys


REQUIRED_PATHS = [
    "README.md",
    "LICENSE",
    "CITATION.cff",
    "requirements.txt",
    "environment.yml",
    ".gitignore",
    "docs/reproducibility_guide.md",
    "docs/analysis_decisions.md",
    "docs/data_dictionary.md",
    "docs/construct_crosswalk.md",
    "data/README.md",
    "notebooks/README.md",
    "src/README.md",
]

SENSITIVE_PATTERNS = [
    "respondent",
    "participant",
    "confidential",
    "private",
    "restricted",
    "credential",
    "secret",
    "token",
    "turnitin",
    "reviewer_comment",
    "response_to_reviewer",
]

ALLOWED_SENSITIVE_LOCATIONS = {
    "data/codebooks/airpac_codebook_template.csv",
    "data/codebooks/vietnam_codebook_template.csv",
    "data/templates/expected_files_template.csv",
    "DATA_TEMPLATE_README.md",
    "RELEASE_CHECKLIST.md",
}


def repository_root() -> Path:
    current = Path.cwd().resolve()
    if current.name == "scripts":
        return current.parent
    return current


def check_required_paths(root: Path) -> list[str]:
    return [path for path in REQUIRED_PATHS if not (root / path).exists()]


def check_notebooks(root: Path) -> list[str]:
    errors: list[str] = []
    notebook_dir = root / "notebooks"

    for notebook in sorted(notebook_dir.glob("*.ipynb")):
        try:
            with notebook.open("r", encoding="utf-8") as handle:
                content = json.load(handle)
            if content.get("nbformat") != 4:
                errors.append(f"{notebook}: unexpected notebook format")
            if not isinstance(content.get("cells"), list):
                errors.append(f"{notebook}: missing cells list")
        except Exception as exc:
            errors.append(f"{notebook}: {exc}")

    if not list(notebook_dir.glob("*.ipynb")):
        errors.append("No Jupyter notebooks were found.")

    return errors


def find_suspicious_files(root: Path) -> list[str]:
    findings: list[str] = []

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue

        relative = path.relative_to(root).as_posix()
        if relative in ALLOWED_SENSITIVE_LOCATIONS:
            continue

        lowered = relative.lower()
        if any(pattern in lowered for pattern in SENSITIVE_PATTERNS):
            findings.append(relative)

        if path.suffix.lower() in {".enl", ".enlx", ".pem", ".key", ".p12", ".pfx"}:
            findings.append(relative)

        if path.name.startswith("~$"):
            findings.append(relative)

    return sorted(set(findings))


def check_gitignore(root: Path) -> list[str]:
    errors: list[str] = []
    correct = root / ".gitignore"
    incorrect = root / "gitignore"

    if not correct.exists():
        errors.append(".gitignore is missing.")
    if incorrect.exists():
        errors.append("An incorrectly named 'gitignore' file is still present.")

    return errors


def main() -> int:
    root = repository_root()

    missing = check_required_paths(root)
    notebook_errors = check_notebooks(root)
    gitignore_errors = check_gitignore(root)
    suspicious = find_suspicious_files(root)

    print("Repository audit")
    print("================")
    print(f"Root: {root}")

    if missing:
        print("\nMissing required paths:")
        for item in missing:
            print(f"  - {item}")

    if notebook_errors:
        print("\nNotebook issues:")
        for item in notebook_errors:
            print(f"  - {item}")

    if gitignore_errors:
        print("\nGit-ignore issues:")
        for item in gitignore_errors:
            print(f"  - {item}")

    if suspicious:
        print("\nFiles requiring manual privacy/licence review:")
        for item in suspicious:
            print(f"  - {item}")

    failures = missing or notebook_errors or gitignore_errors

    if failures:
        print("\nAudit result: FAILED")
        return 1

    if suspicious:
        print("\nAudit result: PASSED WITH MANUAL-REVIEW ITEMS")
        return 0

    print("\nAudit result: PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
