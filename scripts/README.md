# Execution and Audit Scripts

## Repository audit

Run:

```bash
python scripts/audit_repository.py
```

The script checks required files, notebook structure, `.gitignore`, and filenames that may require privacy or licence review.

## Execute all notebooks

After the verified analytical code and permitted local inputs are available, run:

```bash
python scripts/run_all.py
```

Executed copies are written to `outputs/executed_notebooks/`.

## Make commands

On systems with `make`:

```bash
make install
make audit
make run
```
