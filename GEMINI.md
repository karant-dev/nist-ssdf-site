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
- Built a professional `README.md` containing instructions for deployment natively on Cloudflare Pages and setting up MkDocs for immediate local iterations.
- Established rigorous Git hygiene (`.gitignore`) ignoring `venv` and the statically generated `/site` builds.
- Initialized local Git repository, created initial commit mapping, removed the legacy Github actions folder, and established the remote integration targeting `karant-dev/nist-ssdf-site`.
- Included an assumed structure of the `ssdf_v1.1.json` input data mapped from the script constraints.
- Optimized `scripts/ingest_ssdf.py` to support version-agnostic ingestion with smart navigation merging in `mkdocs.yml`.
- Integrated SSDF v1.2 via `scripts/convert_csv_to_json.py` handling PDF-extracted CSV data and cross-version reference hydration.
- Implemented version status labels (`(current)`, `(upcoming)`) dynamically visible in both navigation and the root hub page.
- Configured automatic descending version sorting (newest first) for both the navigation tree and the root documentation hub.
- Refined the visual design system:
    - Replaced the light mode indigo/emerald gradients with solid, premium colors (Indigo for Light, Blue for Dark).
    - Established a high-contrast yet eye-friendly Blue palette for Dark Mode (Slate scheme).
    - Custom-aligned the header bar color with the document typography for a unified flat aesthetic.
- Implemented robust "Task Moved" stubs for SSDF v1.2 that anchor directly to the new task locations.
- Finalized a clean, production-ready build pipeline that preserves Git hygiene while supporting iterative updates.

## Next steps
- The user can parse the latest data via `python scripts/convert_xlsx_to_json.py`.
- The user can start the script manually via `python scripts/ingest_ssdf.py` to compile the docs folder and preview locally using `mkdocs serve`.
