import json
import pandas as pd
import re

def convert_xlsx_to_json(xlsx_path, json_path):
    # Parse Groups (Practices)
    df_groups = pd.read_excel(xlsx_path, sheet_name='Groups', header=None)
    practices = {}
    
    for idx, row in df_groups.iterrows():
        text = str(row[0]).strip()
        if pd.isna(text) or not text or text == "nan": continue
        
        m = re.match(r'^(.*?) \(([A-Z]{2})\):\s*(.*)$', text)
        if m:
            name, pid, desc = m.groups()
            practices[pid] = {
                "identifier": pid,
                "name": name,
                "description": desc,
                "tasks": {}
            }
        else:
            print("Failed to match group:", text)

            
    # Parse References for hyperlinks
    df_refs = pd.read_excel(xlsx_path, sheet_name='References', header=None)
    ref_urls = {}
    for idx, row in df_refs.iterrows():
        ref_id_raw = str(row[0]).strip()
        if pd.isna(ref_id_raw) or not ref_id_raw or ref_id_raw == "nan": continue
        ref_id = ref_id_raw.strip('[]')
        ref_text = str(row[1]).strip()
        url_m = re.search(r'(https?://[^\s]+)', ref_text)
        if url_m:
            ref_urls[ref_id] = url_m.group(1).rstrip('.')
            
    # Parse SSDF sheet (Tasks and Implementations)
    df_ssdf = pd.read_excel(xlsx_path, sheet_name='SSDF')
    # Because 'Practices' cell is merged, we forward-fill to carry over the Task info to all Implementation rows
    df_ssdf['Practices'] = df_ssdf['Practices'].ffill()
    
    for idx, row in df_ssdf.iterrows():
        task_text = str(row['Practices']).strip()
        imp_text = str(row['Tasks']).strip()
        examples_text = str(row['Notional Implementation Examples']).strip()
        refs_text = str(row['References']).strip()
        
        if pd.isna(task_text) or task_text == "nan": continue
        
        # Parse Task
        m_task = re.match(r'^(.*?) \(([A-Z]{2}\.\d+)\):\s*(.*)$', task_text)
        if not m_task:
            continue
            
        task_name, task_id, task_desc = m_task.groups()
        practice_id = task_id.split('.')[0]
        
        if practice_id not in practices:
            practices[practice_id] = {
                "identifier": practice_id,
                "name": "Unknown Practice",
                "description": "",
                "tasks": {}
            }
            
        if task_id not in practices[practice_id]["tasks"]:
            practices[practice_id]["tasks"][task_id] = {
                "identifier": task_id,
                "name": task_name,
                "description": task_desc,
                "implementations": []
            }
            
        # Parse Implementation
        if pd.isna(imp_text) or imp_text == "nan": continue
        m_imp = re.match(r'^([A-Z]{2}\.\d+\.\d+):\s*(.*)$', imp_text)
        if not m_imp: continue
        
        imp_id, imp_desc = m_imp.groups()
        
        # Parse Examples
        examples = []
        if not pd.isna(examples_text) and examples_text != "nan":
            # split by '\n' or 'Example X:'
            examples = [e.strip() for e in examples_text.split('\n') if e.strip()]
            
        # Parse References
        refs = []
        if not pd.isna(refs_text) and refs_text != "nan":
            for ref_line in refs_text.split('\n'):
                ref_line = ref_line.strip()
                if not ref_line: continue
                # Add hyperlink if reference is found
                m_ref = re.match(r'^([a-zA-Z0-9_-]+)(:?\s*.*)$', ref_line)
                if m_ref and m_ref.group(1) in ref_urls:
                    ref_src = m_ref.group(1)
                    ref_rest = m_ref.group(2)
                    url = ref_urls[ref_src]
                    refs.append(f"[{ref_src}]({url}){ref_rest}")
                else:
                    refs.append(ref_line)
                    
        imp_obj = {
            "identifier": imp_id,
            "description": imp_desc,
            "examples": examples,
            "references": refs
        }
        
        practices[practice_id]["tasks"][task_id]["implementations"].append(imp_obj)
        
    final_output = {
        "framework": "Secure Software Development Framework (SSDF)",
        "version": "1.1",
        "practices": []
    }
    
    for p_id in sorted(practices.keys()):
        p_obj = practices[p_id]
        tasks_list = []
        for t_id in sorted(p_obj["tasks"].keys(), key=lambda x: int(x.split('.')[1])):
            tasks_list.append(p_obj["tasks"][t_id])
        p_obj["tasks"] = tasks_list
        final_output["practices"].append(p_obj)
        
    with open(json_path, 'w') as f:
        json.dump(final_output, f, indent=2)
        
if __name__ == "__main__":
    convert_xlsx_to_json('nist.sp.800-218.ssdf-table.xlsx', 'ssdf_v1.1.json')
    print("Conversion completed successfully.")
