import pandas as pd
import re
import json

df_groups = pd.read_excel('nist.sp.800-218.ssdf-table.xlsx', sheet_name='Groups', header=None)
practices_info = {}
for idx, row in df_groups.iterrows():
    text = str(row[0]).strip()
    if pd.isna(text) or not text: continue
    m = re.match(r'^(.*?) \(([A-Z]{2})\): (.*)$', text)
    if m:
        name, pid, desc = m.groups()
        practices_info[pid] = {"identifier": pid, "name": name, "description": desc, "tasks": []}
    else:
        print("Failed to match group:", text)

df_refs = pd.read_excel('nist.sp.800-218.ssdf-table.xlsx', sheet_name='References', header=None)
ref_urls = {}
for idx, row in df_refs.iterrows():
    ref_id_raw = str(row[0]).strip()
    if pd.isna(ref_id_raw) or not ref_id_raw: continue
    ref_id = ref_id_raw.strip('[]')
    ref_text = str(row[1]).strip()
    url_m = re.search(r'(https?://[^\s]+)', ref_text)
    if url_m:
        ref_urls[ref_id] = url_m.group(1).rstrip('.')
    else:
        ref_urls[ref_id] = None

df_ssdf = pd.read_excel('nist.sp.800-218.ssdf-table.xlsx', sheet_name='SSDF')
df_ssdf = df_ssdf.ffill(axis=0) # Forward fill Tasks (which are in Practices column)

# print(practices_info)
# print(ref_urls)

