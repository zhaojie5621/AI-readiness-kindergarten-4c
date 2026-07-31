"""Execute the four analysis notebooks in the documented order.

Use only after verified analytical code and permitted local input files have
been added. By default, executed notebooks are written to outputs/executed_notebooks.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


NOTEBOOKS = [
    "01_airpac_analysis.ipynb",
    "02_vietnam_ece_analysis.ipynb",
    "03_china_evidence_synthesis.ipynb",
    "04_cross_study_synthesis.ipynb",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    notebook_dir = root / "notebooks"
    output_dir = root / "outputs" / "executed_notebooks"
    output_dir.mkdir(parents=True, exist_ok=True)

    for name in NOTEBOOKS:
        source = notebook_dir / name
        if not source.exists():
            raise FileNotFoundError(f"Missing notebook: {source}")

        command = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            str(source),
            "--output",
            str(output_dir / name),
            "--ExecutePreprocessor.timeout=1200",
        ]

        print(f"Executing {name}")
        subprocess.run(command, cwd=root, check=True)

    print("All notebooks executed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
