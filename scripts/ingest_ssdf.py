import json
import os
import yaml

def create_markdown_frontmatter(title, practice_identifier, task_identifier, version, references):
    """
    Generate YAML frontmatter to be placed at the top of MkDocs markdown files.
    """
    frontmatter = {
        "title": title,
        "practice_identifier": practice_identifier,
        "task_identifier": task_identifier,
        "version": version,
        "references": references
    }
    return f"---\n{yaml.dump(frontmatter, sort_keys=False)}---\n\n"

def process_ssdf_data(json_path, output_dir):
    """
    Ingests JSON SSDF data and builds the relevant documentation directory structure.
    """
    # Load JSON file mapping to our structural assumption
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    version = data.get("version", "1.1")
    base_dir = os.path.join(output_dir, f"v{version}")
    
    # Ensure our major version root directory exists
    os.makedirs(base_dir, exist_ok=True)
    
    # Create the root version index
    v_index_content = f"---\ntitle: SSDF Version {version}\n---\n\n"
    v_index_content += f"# SSDF Version {version}\n\n"
    v_index_content += "Welcome to the NIST Secure Software Development Framework (SSDF) documentation.\n\n"
    v_index_content += "The SSDF organizes security practices into the following high-level groups:\n\n"
    
    for practice in data.get("practices", []):
        p_id = practice.get("identifier")
        p_name = practice.get("name")
        p_desc = practice.get("description", "")
        p_url = f"{p_id.lower()}/index.md"
        
        v_index_content += f"## [{p_id}: {p_name}]({p_url})\n\n"
        v_index_content += f"{p_desc}\n\n"
        
    with open(os.path.join(base_dir, "index.md"), "w") as f:
        f.write(v_index_content)
    
    for practice in data.get("practices", []):
        practice_id = practice.get("identifier")
        
        # We want our URL structure clean as suggested e.g. /v1.1/po
        practice_dir_name = practice_id.lower()
        practice_dir = os.path.join(base_dir, practice_dir_name)
        
        os.makedirs(practice_dir, exist_ok=True)
        
        # Generate Practice index mapping to the Practice Overview (e.g., PO - Prepare the Organization)
        practice_title = f"{practice_id}: {practice.get('name')}"
        practice_index = f"---\ntitle: \"{practice_title}\"\n---\n\n"
        practice_index += f"# {practice_title}\n\n"
        practice_index += practice.get("description", "") + "\n\n"
        
        tasks_list = practice.get("tasks", [])
        if tasks_list:
            practice_index += "## Practices\n\n"
            for t in tasks_list:
                t_id = t.get("identifier")
                t_name = t.get("name", t.get("title", ""))
                t_file = t_id.replace(".", "-").lower() + ".md"
                practice_index += f"* [{t_id}: {t_name}]({t_file})\n"

        with open(os.path.join(practice_dir, "index.md"), "w") as f:
            f.write(practice_index)
            
        for task in practice.get("tasks", []):
            task_id = task.get("identifier")
            # Enforce clean filename formats (po-1.md)
            task_file_name = task_id.replace(".", "-").lower() + ".md"
            task_file_path = os.path.join(practice_dir, task_file_name)
            
            task_name = task.get("name", task.get("title", ""))
            
            # Aggregate references from implementations for frontmatter
            all_refs = []
            for imp in task.get("implementations", []):
                for ref in imp.get("references", []):
                    if ref not in all_refs:
                        all_refs.append(ref)

            # Generate the Frontmatter
            frontmatter = create_markdown_frontmatter(
                title=f"{task_id}: {task_name}",
                practice_identifier=practice_id,
                task_identifier=task_id,
                version=version,
                references=all_refs
            )
            
            # Form the Body Structure
            body = f"# {task_id}: {task_name}\n\n"
            body += f"{task.get('description', task.get('statement', ''))}\n\n"
            
            for imp in task.get("implementations", []):
                imp_id = imp.get('identifier', '')
                anchor_id = imp_id.replace('.', '-').lower()
                body += f"## {imp_id} {{: #{anchor_id} }}\n\n"
                
                # Render a warning admonition for deprecated/moved stubs
                if imp.get('deprecated'):
                    moved_to = imp.get('moved_to', 'another task')
                    moved_parts = moved_to.split('.')
                    # Implementations live as anchored sections within their parent task page.
                    # e.g. PO.1.3 is a section on v1.2/po/po-1.md with anchor #po-1-3
                    # e.g. PW.4.4 is a section on v1.2/pw/pw-4.md with anchor #pw-4-4
                    current_group = task_id.split('.')[0].lower()
                    target_group = moved_parts[0].lower()
                    if len(moved_parts) >= 3:
                        # e.g. PO.1.3 -> parent file is po-1.md, anchor is po-1-3
                        parent_file = f"{moved_parts[0].lower()}-{moved_parts[1]}.md"
                        anchor = moved_to.replace('.', '-').lower()
                        if target_group != current_group:
                            moved_link = f"../{target_group}/{parent_file}#{anchor}"
                        else:
                            moved_link = f"{parent_file}#{anchor}"
                    else:
                        # Fallback: just link to the group index if structure unclear
                        if target_group != current_group:
                            moved_link = f"../{target_group}/"
                        else:
                            moved_link = "./"
                    body += f'!!! warning "Task Moved"\n'
                    body += f'    This task has been relocated. Please refer to [{moved_to}]({moved_link}) for the current content.\n\n'
                    continue
                
                body += f"{imp.get('description', '')}\n\n"
                
                examples = imp.get("examples", [])
                if examples:
                    body += "???+ example \"Implementation Examples\"\n"
                    for example in examples:
                        body += f"    * {example}\n"
                    body += "\n"
                    
                refs = imp.get("references", [])
                if refs:
                    body += "??? info \"References\"\n"
                    for ref in refs:
                        body += f"    * {ref}\n"
                    body += "\n"
                
                # Write out individual `.md` file
            with open(task_file_path, "w") as f:
                f.write(frontmatter + body)

    # Re-build `mkdocs.yml` explicit navigation tree securely
    print("Generating explicit Navigation Tree for mkdocs.yml...")

    # Build this version's nav entry
    version_entry_key = f"V{version}"
    version_nav_items = [f"v{version}/index.md"]

    for practice in data.get("practices", []):
        practice_id = practice.get("identifier")
        practice_name = practice.get("name")
        practice_dir_name = practice_id.lower()

        practice_nav = [
            f"v{version}/{practice_dir_name}/index.md"
        ]

        for task in practice.get("tasks", []):
            task_id = task.get("identifier")
            task_name = task.get("name", task.get("title", ""))
            task_file_name = task_id.replace(".", "-").lower() + ".md"
            practice_nav.append({
                f"{task_id}: {task_name}": f"v{version}/{practice_dir_name}/{task_file_name}"
            })

        version_nav_items.append({f"{practice_id}: {practice_name}": practice_nav})

    new_version_entry = {version_entry_key: version_nav_items}

    mkdocs_yaml_path = os.path.join(output_dir, "..", "mkdocs.yml")
    mkdocs_yaml_path = os.path.normpath(mkdocs_yaml_path)
    if os.path.exists(mkdocs_yaml_path):
        with open(mkdocs_yaml_path, "r") as f:
            mkdocs_content = f.read()

        # Read existing nav so we can merge, preserving other versions
        existing_nav = []
        if "\nnav:\n" in mkdocs_content:
            nav_yaml_str = mkdocs_content[mkdocs_content.index("\nnav:\n") + 1:]
            try:
                existing_nav = yaml.safe_load(nav_yaml_str).get("nav", []) or []
            except Exception:
                existing_nav = []
            mkdocs_content = mkdocs_content[:mkdocs_content.index("\nnav:\n")]

        # Merge: keep hub entry, replace/add this version, keep all other versions
        hub_entry = {"NIST SSDF Documentation Hub": "index.md"}
        merged_nav = [hub_entry]
        version_added = False
        for entry in existing_nav:
            if not isinstance(entry, dict):
                continue
            key = list(entry.keys())[0]
            if key == "NIST SSDF Documentation Hub":
                continue  # Already prepended
            elif key == version_entry_key:
                merged_nav.append(new_version_entry)
                version_added = True
            else:
                merged_nav.append(entry)

        if not version_added:
            merged_nav.append(new_version_entry)

        nav_block = yaml.dump({"nav": merged_nav}, sort_keys=False)
        with open(mkdocs_yaml_path, "w") as f:
            f.write(mkdocs_content + "\n" + nav_block)

    # Update the root docs/index.md hub page to list this version
    root_index_path = os.path.join(output_dir, "index.md")
    version_label = f"SSDF Version {version}"
    version_link = f"[{version_label}](v{version}/index.md)"
    version_entry = f"* {version_link}"

    if os.path.exists(root_index_path):
        with open(root_index_path, "r") as f:
            root_content = f.read()

        # If this version is already listed, skip
        if f"v{version}/index.md" not in root_content:
            # Append the version entry before the end (after the last bullet if any)
            if "### Framework Iterations" in root_content:
                root_content = root_content.rstrip() + f"\n{version_entry}\n"
            else:
                root_content = root_content.rstrip() + "\n\n### Framework Iterations\n" + version_entry + "\n"
            with open(root_index_path, "w") as f:
                f.write(root_content)
            print(f"Updated root index.md with {version_label}")
    else:
        # Create from scratch
        root_content = (
            "# NIST SSDF Documentation Hub\n\n"
            "Welcome to the static documentation website for the NIST Secure Software Development Framework (SSDF).\n\n"
            "This documentation provides easily accessible framework components natively searchable and traversable.\n\n"
            "### Framework Iterations\n"
            f"{version_entry}\n"
        )
        with open(root_index_path, "w") as f:
            f.write(root_content)
        print(f"Created root index.md with {version_label}")
            
if __name__ == "__main__":
    import sys
    # Accepts optional input JSON path as first argument, defaults to v1.1
    input_json = sys.argv[1] if len(sys.argv) > 1 else "ssdf_v1.1.json"
    docs_dir = "docs"
    
    if not os.path.exists(input_json):
        print(f"Dataset {input_json} not found. Please provide the input JSON file.")
    else:
        process_ssdf_data(input_json, docs_dir)
        print("SSDF documentation structured and generated successfully.")
