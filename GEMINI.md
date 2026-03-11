# Current State
A fast, text-first, version-controlled static documentation website for the NIST Secure Software Development Framework (SSDF) was initialized.

## Done
- Initialized core repository structure `/docs` and `/.github/workflows` and `/scripts`
- Synthesized the `requirements.txt` for the mkdocs plugins dependencies, including `pandas` and `openpyxl`.
- Wrote an ingestion data script `scripts/ingest_ssdf.py` mapping `.json` to Markdown docs natively matching the `/v1.1/po/po-1/` url structure dynamically.
- Wrote an ingestion data script `scripts/convert_xlsx_to_json.py` to natively parse the original NIST `nist.sp.800-218.ssdf-table.xlsx` file.
  - Generates cross-references by mapping citation identifiers in `References` sheet to physical hyperlinks!
- Parameterized the Markdown script frontmatter to use proper properties including nested arrays (e.g references, implementation examples).
- Wrote MkDocs core settings, themes, plugin additions in `mkdocs.yml` (e.g. Navigation omitted to respect the natively built folder navigation mapping implicitly).
- Enhanced `scripts/ingest_ssdf.py` to systematically assign Markdown frontmatter titles to index files, natively updating the table of contents navigation handles to readable formats (e.g `PO: Prepare the Organization`).
- Configured dynamic generation of sub-practices hyperlinks for each index page to form an actionable table of contents at the hierarchy top level.
- Re-formatted Markdown ingestion string interpolations to wrap lists into custom Mkdocs Material Admonition directives for an upgraded look.
- Injected custom Material CSS overrides with gradients (indigo/emerald), hover interactions, and neumorphic cards for a premium interface (with left-alignment kept flat and pills made roomier to preserve side-nav hierarchy).
- Configured native OS-level theme auto-detection (Light/Dark mode) in `mkdocs.yml`.
- Re-coded the root repository index page mapping script to systematically assemble an actionable dashboard layout listing each major SSDF practice grouping.
- Upgraded the navigation auto-generation script to structurally nest practices implicitly under an un-keyed version folder header (e.g `V1.1`).
- Disabled `navigation.sections` in config to render top-level hierarchy as natively collapsible containers instead of sticky category headings.
- Configured a github-actions run template to update and deploy via gh-pages securely.
- Included an assumed structure of the `ssdf_v1.1.json` input data mapped from the script constraints.

## Next steps
- The user can parse the latest data via `python scripts/convert_xlsx_to_json.py`.
- The user can start the script manually via `python scripts/ingest_ssdf.py` to compile the docs folder and preview locally using `mkdocs serve`.
