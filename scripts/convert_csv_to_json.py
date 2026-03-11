import csv
import json
import re


# ── Reference URL lookup table extracted from ssdf_v1.1.json ─────────────────
# Maps reference identifiers (without brackets) to their known hyperlinks.
# Used to hyperlink shared references that appear in v1.2 CSV without URLs.
REF_URL_MAP = {
    "BSAFSS":    "https://www.bsa.org/files/reports/bsa_framework_secure_software_update_2020.pdf",
    "BSIMM":     "https://www.bsimm.com/content/dam/bsimm/reports/bsimm12-foundations.pdf",
    "CNCFSSCP":  "https://github.com/cncf/tag-security/tree/main/supply-chain-security/supply-chain-security-paper",
    "EO14028":   "https://www.govinfo.gov/app/details/DCPD-202100401",
    "IDASOAR":   "https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016",
    "IDASoar":   "https://www.ida.org/research-and-publications/publications/all/s/st/stateoftheart-resources-soar-for-software-vulnerability-detection-test-and-evaluation-2016",
    "IEC62443":  "https://webstore.iec.ch/publication/33615",
    "IR8397":    "https://doi.org/10.6028/NIST.IR.8397",
    "ISO27034":  "https://www.iso.org/standard/44378.html",
    "ISO29147":  "https://www.iso.org/standard/72311.html",
    "ISO30111":  "https://www.iso.org/standard/53231.html",
    "MSSDL":     "https://www.microsoft.com/en-us/securityengineering/sdl/",
    "NISTCSF":   "https://doi.org/10.6028/NIST.CSWP.04162018",
    "NISTCSF20": "https://doi.org/10.6028/NIST.CSWP.29",
    "NISTLABEL": "https://www.nist.gov/itl/executive-order-improving-nations-cybersecurity",
    "NTIASBOM":  "https://www.ntia.doc.gov/report/2021/minimum-elements-software-bill-materials-sbom",
    "OWASPASVS": "https://github.com/OWASP/ASVS",
    "OWASPMASVS": "https://github.com/OWASP/owasp-masvs/releases",
    "OWASPSAMM": "https://www.owasp.org/index.php/OWASP_SAMM_Project",
    "OWASPSCVS": "https://github.com/OWASP/Software-Component-Verification-Standard",
    "PCISSLC":   "https://www.pcisecuritystandards.org/document_library?category=sware_sec#results",
    "SCAGILE":   "http://www.safecode.org/publication/SAFECode_Agile_Dev_Security0712.pdf",
    "SCFPSSD":   "https://safecode.org/wp-content/uploads/2018/03/SAFECode_Fundamental_Practices_for_Secure_Software_Development_March_2018.pdf",
    "SCSIC":     "http://www.safecode.org/publication/SAFECode_Software_Integrity_Controls0610.pdf",
    "SCTTM":     "https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TM_Whitepaper.pdf",
    "SCTPC":     "https://www.safecode.org/wp-content/uploads/2017/05/SAFECode_TPC_Whitepaper.pdf",
    "SP80053":   "https://doi.org/10.6028/NIST.SP.800-53r5",
    "SP800160":  "https://doi.org/10.6028/NIST.SP.800-160v1",
    "SP800161":  "https://doi.org/10.6028/NIST.SP.800-161r1-draft2",
    "SP800181":  "https://doi.org/10.6028/NIST.SP.800-181",
    "SP800216":  "https://doi.org/10.6028/NIST.SP.800-216",
}

# Top-level practice group descriptions extracted from the CSV header rows
PRACTICE_GROUP_META = {}


def normalize_ref(ref_line):
    """
    Normalize a raw reference string from the CSV into a hyperlinked Markdown
    format matching the v1.1 schema: [REFID](url): sections
    Handles both bracketed [REF] and unbracketed REF formats.
    """
    ref_line = ref_line.strip()
    if not ref_line:
        return None

    # Try to extract the reference identifier (with or without brackets)
    m = re.match(r'^\[?([A-Za-z0-9_-]+)\]?:\s*(.*)', ref_line)
    if not m:
        return ref_line  # Return as-is if we can't parse it

    ref_id = m.group(1)
    ref_rest = m.group(2).strip()

    if ref_id in REF_URL_MAP:
        url = REF_URL_MAP[ref_id]
        return f"[{ref_id}]({url}): {ref_rest}"
    else:
        # Keep bracketed format for unknown references
        return f"[{ref_id}]: {ref_rest}"


def parse_practice_header(practice_cell):
    """
    Parses the 'Practices' column cell which may be:
    - A full header: "Name (XX.N): Description..."
    - A short repeat:  "Name (XX.N)"
    Returns (task_group_id, task_group_name, description_or_none)
    """
    # Full header pattern: "Name (PO.1): Description..."
    m_full = re.match(r'^(.*?)\s+\(([A-Z]{2}\.\d+)\):\s*(.+)$', practice_cell, re.DOTALL)
    if m_full:
        return m_full.group(2), m_full.group(1).strip(), m_full.group(3).strip()

    # Short repeat pattern: "Name (PO.1)"
    m_short = re.match(r'^(.*?)\s+\(([A-Z]{2}\.\d+)\)\s*$', practice_cell)
    if m_short:
        return m_short.group(2), m_short.group(1).strip(), None

    return None, None, None


def parse_top_level_group(practice_cell):
    """
    From a full practice header cell, extract the top-level group identifier
    (e.g. 'PO' from 'PO.1'), name, and description for the group index page.
    The first row for each top-level group contains the full description.
    """
    m = re.match(r'^(.*?)\s+\(([A-Z]{2})\.\d+\):\s*(.+)$', practice_cell, re.DOTALL)
    if m:
        return m.group(2), m.group(1).strip()
    return None, None


def is_moved_stub(task_cell):
    """Detect stub rows like 'PW.3.1: Moved to PO.1.3'"""
    return bool(re.search(r':\s*Moved to', task_cell, re.IGNORECASE))


def convert_csv_to_json(csv_path, json_path):
    practices = {}       # top-level group id → {identifier, name, description, tasks: {}}
    task_groups = {}     # task_group_id (e.g. 'PO.1') → task group dict
    current_task_group_id = None

    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)  # Skip header row

        for row in reader:
            if len(row) < 4:
                continue

            practice_cell = row[0].strip()
            task_cell = row[1].strip()
            examples_cell = row[2].strip()
            refs_cell = row[3].strip()

            if not practice_cell and not task_cell:
                continue

            # ── Parse practice group header ───────────────────────────────
            task_group_id, task_group_name, task_group_desc = parse_practice_header(practice_cell)

            if task_group_id:
                current_task_group_id = task_group_id
                top_level_id = task_group_id.split('.')[0]  # e.g. 'PO'

                # Register top-level group if new
                if top_level_id not in practices:
                    practices[top_level_id] = {
                        "identifier": top_level_id,
                        "name": "",
                        "description": "",
                        "tasks": {}
                    }

                # First full header row for this top-level group has the group name
                if not practices[top_level_id]["name"] and task_group_name:
                    # Extract just the top-level group name from the task group name
                    # e.g. "Define Security Requirements for Software Development" → 
                    # we use the task group name as a fallback; the group name is set 
                    # from the first task's practice name prefix
                    top_lvl_name, _ = parse_top_level_group(practice_cell)
                    if top_lvl_name:
                        # Build the group name from the top-level acronym's known mapping
                        pass  # Name will be set from GROUP_NAMES below

                # Register task group if new
                if task_group_id not in task_groups:
                    task_groups[task_group_id] = {
                        "identifier": task_group_id,
                        "name": task_group_name,
                        "description": task_group_desc or "",
                        "implementations": []
                    }
                elif task_group_desc and not task_groups[task_group_id]["description"]:
                    task_groups[task_group_id]["description"] = task_group_desc

                # Associate task group with its parent
                practices[top_level_id]["tasks"][task_group_id] = task_groups[task_group_id]

            # Use last seen task group if this is a continuation row
            effective_task_group_id = task_group_id or current_task_group_id
            if not effective_task_group_id:
                continue

            top_level_id = effective_task_group_id.split('.')[0]

            # ── Parse the implementation (task row) ───────────────────────
            if not task_cell:
                continue

            m_imp = re.match(r'^([A-Z]{2}\.\d+\.\d+):\s*(.*)$', task_cell, re.DOTALL)
            if not m_imp:
                continue

            imp_id = m_imp.group(1)
            imp_desc = m_imp.group(2).strip()

            # ── Handle moved/deprecated stubs ─────────────────────────────
            if is_moved_stub(task_cell):
                redirect_target = re.search(r'Moved to\s+([A-Z]{2}\.\d+(?:\.\d+)?)', task_cell, re.IGNORECASE)
                target_str = redirect_target.group(1) if redirect_target else "another task"
                imp_obj = {
                    "identifier": imp_id,
                    "description": f"This task has been moved. See [{target_str}](../{target_str.replace('.', '-').lower()}/) for the current content.",
                    "examples": [],
                    "references": [],
                    "deprecated": True,
                    "moved_to": target_str
                }
                task_groups[effective_task_group_id]["implementations"].append(imp_obj)
                continue

            # ── Parse examples ────────────────────────────────────────────
            examples = []
            if examples_cell and examples_cell.upper() != "N/A":
                # Split on newline boundaries between examples
                raw_examples = re.split(r'\n(?=Example\s+\d+:)', examples_cell)
                for ex in raw_examples:
                    ex = ex.strip()
                    if ex:
                        examples.append(ex)

            # ── Parse and normalize references ────────────────────────────
            refs = []
            if refs_cell and refs_cell.upper() != "N/A":
                # Split on actual newlines OR literal \n strings (from PDF-extracted CSVs)
                for ref_line in re.split(r'\n|\\n', refs_cell):
                    normalized = normalize_ref(ref_line)
                    if normalized:
                        refs.append(normalized)

            imp_obj = {
                "identifier": imp_id,
                "description": imp_desc,
                "examples": examples,
                "references": refs
            }
            task_groups[effective_task_group_id]["implementations"].append(imp_obj)

    # ── Assemble top-level group names from known mapping ─────────────────────
    GROUP_NAMES = {
        "PO": ("Prepare the Organization",
               "Organizations should ensure that their people, processes, and technology are "
               "prepared to perform secure software development at the organization level."),
        "PS": ("Protect the Software",
               "Organizations should protect all components of their software from tampering "
               "and unauthorized access."),
        "PW": ("Produce Well-Secured Software",
               "Organizations should produce well-secured software with minimal security "
               "vulnerabilities in its releases."),
        "RV": ("Respond to Vulnerabilities",
               "Organizations should identify residual vulnerabilities in their software "
               "releases and respond appropriately to address those vulnerabilities and "
               "prevent similar ones from occurring in the future."),
    }

    for gid, (gname, gdesc) in GROUP_NAMES.items():
        if gid in practices:
            practices[gid]["name"] = gname
            if not practices[gid]["description"]:
                practices[gid]["description"] = gdesc

    # ── Build final ordered output ────────────────────────────────────────────
    final_output = {
        "framework": "Secure Software Development Framework (SSDF)",
        "version": "1.2",
        "practices": []
    }

    for p_id in sorted(practices.keys()):
        p_obj = practices[p_id]
        tasks_list = sorted(
            p_obj["tasks"].values(),
            key=lambda t: [int(x) if x.isdigit() else x for x in t["identifier"].split('.')]
        )
        # Convert task implementations structure to match v1.1 schema
        # In v1.1: practice has 'tasks' list, each task has 'implementations' list
        # In our intermediate: task_groups have implementations directly
        # We need to wrap each task_group as a "task" with implementations
        formatted_tasks = []
        for tg in tasks_list:
            formatted_tasks.append({
                "identifier": tg["identifier"],
                "name": tg["name"],
                "description": tg["description"],
                "implementations": tg["implementations"]
            })

        p_obj["tasks"] = formatted_tasks
        final_output["practices"].append({
            "identifier": p_obj["identifier"],
            "name": p_obj["name"],
            "description": p_obj["description"],
            "tasks": formatted_tasks
        })

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=2, ensure_ascii=False)

    print(f"Conversion complete: {len(final_output['practices'])} practice groups written to {json_path}")
    for p in final_output["practices"]:
        task_count = sum(len(t["implementations"]) for t in p["tasks"])
        stub_count = sum(
            1 for t in p["tasks"]
            for imp in t["implementations"]
            if imp.get("deprecated")
        )
        print(f"  {p['identifier']}: {len(p['tasks'])} task groups, "
              f"{task_count} implementations ({stub_count} stubs)")


if __name__ == "__main__":
    convert_csv_to_json("SSDF_v1.2.csv", "ssdf_v1.2.json")
