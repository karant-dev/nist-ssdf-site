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
    nav_tree = [
        {"NIST SSDF Documentation Hub": "index.md"},
        {f"V{version}": [
            f"v{version}/index.md"
        ]}
    ]
    
    for practice in data.get("practices", []):
        practice_id = practice.get("identifier")
        practice_name = practice.get("name")
        practice_dir_name = practice_id.lower()
        
        practice_nav = [
            # In MkDocs Material w/ navigation.indexes, mapping an un-keyed index page right under the section 
            # turns the section parent itself into a clickable hyperlink!
            f"v{version}/{practice_dir_name}/index.md" 
        ]
        
        for task in practice.get("tasks", []):
            task_id = task.get("identifier")
            task_name = task.get("name", task.get("title", ""))
            task_file_name = task_id.replace(".", "-").lower() + ".md"
            practice_nav.append({
                f"{task_id}: {task_name}": f"v{version}/{practice_dir_name}/{task_file_name}"
            })
            
        nav_tree[1][f"V{version}"].append({
            f"{practice_id}: {practice_name}": practice_nav
        })
        
    mkdocs_yaml_path = os.path.join(output_dir, "..", "mkdocs.yml")
    mkdocs_yaml_path = os.path.normpath(mkdocs_yaml_path)
    if os.path.exists(mkdocs_yaml_path):
        with open(mkdocs_yaml_path, "r") as f:
            mkdocs_content = f.read()
            
        if "\nnav:\n" in mkdocs_content:
            mkdocs_content = mkdocs_content[:mkdocs_content.index("\nnav:\n")]
            
        nav_block = yaml.dump({"nav": nav_tree}, sort_keys=False)
        with open(mkdocs_yaml_path, "w") as f:
            f.write(mkdocs_content + "\n" + nav_block)
            
if __name__ == "__main__":
    # Assumes the script runs from the repository root
    input_json = "ssdf_v1.1.json"
    docs_dir = "docs"
    
    if not os.path.exists(input_json):
        print(f"Dataset {input_json} not found. Please provide the input JSON file.")
    else:
        process_ssdf_data(input_json, docs_dir)
        print("SSDF documentation structured and generated successfully.")
