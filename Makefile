.PHONY: install audit run clean

install:
	python -m pip install -r requirements.txt

audit:
	python scripts/audit_repository.py

run:
	python scripts/run_all.py

clean:
	python -c "from pathlib import Path; import shutil; p=Path('outputs/executed_notebooks'); shutil.rmtree(p) if p.exists() else None"
