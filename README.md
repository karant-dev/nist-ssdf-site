# NIST SSDF Documentation Hub

A fast, text-first, version-controlled static documentation website for the **NIST Secure Software Development Framework (SSDF)**.

## Architecture

This project maps the original SSDF metadata (`.xlsx`) to a beautiful, static Markdown structure compiled by MkDocs matching deterministic, deeply linkable URLs (e.g. `v1.1/po/po-1/`).

- **Core Builder:** [MkDocs](https://www.mkdocs.org/)
- **Theme Interface:** [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- **Mapping Logic:** Python (`pandas`, `openpyxl`)

## Setup & Local Development

This project uses Python scripts to generate a markdown repository (`docs/`) structurally from a root JSON mapping constraint (`ssdf_v1.1.json`), which is generated directly from an Excel sheet. 

**1. Create a Python Virtual Environment & Install Dependencies:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Hydrate JSON from NIST Excel Dataset:**
```bash
python scripts/convert_xlsx_to_json.py
```

**3. Transcribe mapping to nested Markdown Structure:**
```bash
python scripts/ingest_ssdf.py
```

**4. Preview Locally:**
```bash
mkdocs serve
```
Your documentation will instantly be hosted locally at `http://127.0.0.1:8000`.

## Deployment

This repository is optimized for direct continuous deployment natively onto **Cloudflare Pages**. Pushes to `main` branch will automatically compile via MkDocs' core build command and serve globally. 
