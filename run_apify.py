#!/usr/bin/env python3
"""
NETS-Drive: Live Apify Decision-Maker Enrichment Engine
======================================================
Reads companies from nets-drive.html.
Queries Apify's Google Search Scraper for live LinkedIn personal profiles (linkedin.com/in/...).
Parses real names, titles, and exact LinkedIn URLs.

Outputs clean 5-column format:
company_name,contact_name,email,phone,linkedin
"""

import os
import re
import csv
import json
import urllib.request
import urllib.error
import urllib.parse
import argparse
import time
import subprocess

BASE_DIR = "/Users/ifeanyifelix/Desktop/ReedBreedCC/nets-drive"

def get_apify_token():
    env_path = os.path.join(BASE_DIR, ".env")
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if line.startswith("APIFY_TOKEN="):
                    return line.strip().split("=", 1)[1].strip()
    return os.environ.get("APIFY_TOKEN", "")

def load_companies():
    html_path = os.path.join(BASE_DIR, "nets-drive.html")
    with open(html_path, "r", encoding="utf-8") as f:
        text = f.read()
    m = re.search(r'const allCompanies = (\[.*?\]);', text)
    if not m:
        raise ValueError("allCompanies array not found in nets-drive.html")
    return json.loads(m.group(1))

def clean_company_name(raw_name):
    cleaned = re.sub(r'\(.*?\)', '', raw_name).strip()
    cleaned = re.sub(r'\b(Plc|Limited|Ltd|LLC|Corporation|Enterprises)\b', '', cleaned, flags=re.IGNORECASE).strip()
    cleaned = re.sub(r'[-–,.]+$', '', cleaned).strip()
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    cleaned = re.sub(r'\b(of|in|at|and|the|for|&)\s*$', '', cleaned, flags=re.IGNORECASE).strip()
    return cleaned if len(cleaned) > 2 else raw_name

CLUSTER_ROLES = {
    "Cluster 1": '("Plant Manager" OR "Factory Manager" OR "Operations Director" OR "Head of Operations")',
    "Cluster 2": '("Logistics Manager" OR "HSE Manager" OR "Journey Management" OR "Procurement")',
    "Cluster 3": '("Head of Human Resources" OR "HR Director" OR "Head of Admin" OR "Facilities Manager")',
    "Cluster 4": '("Operations Director" OR "Security Manager" OR "Night Operations" OR "Admin")',
    "Cluster 5": '("Protocol" OR "Fleet Manager" OR "Procurement" OR "Managing Partner" OR "Director")'
}

CLUSTER_METAS = {
    1: {"slug": "cluster_1", "title": "Cluster 1: Industrial Shift Workers & Factory Lines", "subtitle": "High-Volume Workforce Transit for 24/7 Manufacturing, Processing Mills & Heavy Plants"},
    2: {"slug": "cluster_2", "title": "Cluster 2: High-HSE Field Crews & Energy Operations", "subtitle": "Compliant Journey Management for Oil & Gas, Upstream Services, Mining & Infrastructure"},
    3: {"slug": "cluster_3", "title": "Cluster 3: Corporate White-Collar Commuter Networks", "subtitle": "Premium Daily Commute Shuttles for Commercial Banks, Fintechs & Professional Services"},
    4: {"slug": "cluster_4", "title": "Cluster 4: Night Shift Safe Dispersal & 24/7 Lines", "subtitle": "Duty-of-Care Late-Night & Early-Morning Transit for Hospitals, BPOs & Media Broadcasts"},
    5: {"slug": "cluster_5", "title": "Cluster 5: Executive VIP, Protocol & Multi-City Fleets", "subtitle": "On-Demand Chauffeur & Armored Escort Services for Embassies, Conglomerates & Multinationals"}
}

def parse_serp_title(title):
    if not title:
        return "", ""
    cleaned = re.sub(r'\s*[-|]\s*LinkedIn.*$', '', title, flags=re.IGNORECASE).strip()
    parts = [p.strip() for p in cleaned.split(" - ") if p.strip()]
    if len(parts) >= 2:
        name = parts[0]
        if not any(w in name.lower() for w in ["overview", "about", "jobs", "careers", "hiring"]):
            return name, parts[1]
    elif len(parts) == 1:
        sub = [p.strip() for p in parts[0].split(" – ") if p.strip()]
        if len(sub) >= 2:
            return sub[0], sub[1]
    return parts[0] if parts else "", ""

def extract_contact_details(organic_results, clean_name):
    extracted_email = ""
    extracted_phone = ""
    
    texts = []
    for r in organic_results:
        t = r.get("title", "")
        d = r.get("description", "")
        texts.append(f"{t} {d}")
    combined = " ".join(texts)
    
    # 1. Phone numbers
    phones = re.findall(r'(?:\+?234[\s.-]?(?:\(0\))?[\s.-]?\d{1,4}[\s.-]?\d{3,4}[\s.-]?\d{3,4}|0[789][01]\d{8}|01[\s.-]?\d{7})', combined)
    valid_phones = []
    for p in phones:
        p_clean = re.sub(r'[^\d+]', '', p)
        if len(p_clean) >= 9 and not any(p_clean.startswith(x) for x in ['000', '111', '1234']):
            valid_phones.append(p.strip())
    if valid_phones:
        extracted_phone = valid_phones[0]
        
    # 2. Email addresses
    emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', combined)
    ignored = ['sentry', 'wixpress', 'example', 'domain.com', 'google', 'yahoo', 'gmail', 'outlook.com', 'visascheduling', 'scv.va', 'ethics-line', 'fixmail', 'noackgroup', 'cloudns', 'nigeriaphonebook', 'eximpedia', 'gulfyp', 'ptad.gov.ng', 'carlsberg.asia', 'greatnigeriaplc', 'servicebreeder', 'nafdac.gov.ng', 'supermart.ng', 'company.com', 'tip-offs.com', 'businessday.ng', 'oshinowostudio.com', 'pmgman.com', 'thewingscomplex.com', 'all.biz', 'semfirms']
    ignored_prefixes = ['first.last', 'first_last', 'firstname.lastname', 'firstname', 'lastname', 'jane.doe', 'john.doe', 'jsmith', 'user', 'yourname', 'last', 'example']
    valid_emails = []
    for em in emails:
        em_clean = re.sub(r'^(?:Email|contact|CONTACTS\d*|email:?)\s*', '', em, flags=re.IGNORECASE)
        em_clean = re.sub(r'(?:Read|Readmore|\.html|\.php|\.aspx)[a-zA-Z]*$', '', em_clean.strip('.,; \t\n\r'), flags=re.IGNORECASE).rstrip('.,;')
        em_clean = re.sub(r'(\.(?:com\.ng|com|org|net|ng|biz|info))(?:Read|more|[a-zA-Z]{5,})$', r'\1', em_clean, flags=re.IGNORECASE).rstrip('.,;')
        parts = em_clean.lower().split('@')
        if len(parts) == 2:
            user_part, dom = parts
            if not any(ign in dom for ign in ignored) and not any(ign == user_part for ign in ignored_prefixes) and not em_clean.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.css', '.js')):
                valid_emails.append(em_clean)
            
    # Prefer email containing part of the company name
    slug = re.sub(r'[^a-zA-Z]', '', clean_name).lower()[:5]
    for em in valid_emails:
        if slug in em.lower():
            extracted_email = em
            break
    if not extracted_email and valid_emails:
        extracted_email = valid_emails[0]
        
    return extracted_email, extracted_phone

def run_apify_batch(token, queries, max_results=3):
    actor_id = "apify~google-search-scraper"
    
    start_url = f"https://api.apify.com/v2/acts/{actor_id}/runs?token={token}"
    payload = {
        "queries": "\n".join(queries),
        "maxPagesPerQuery": 1,
        "resultsPerPage": max_results,
        "countryCode": "ng",
        "includeUnfilteredResults": False,
        "saveHtml": False,
        "saveHtmlToKeyValueStore": False
    }
    
    req_data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        start_url,
        data=req_data,
        headers={"Content-Type": "application/json"}
    )
    
    with urllib.request.urlopen(req, timeout=60) as resp:
        run_data = json.loads(resp.read().decode("utf-8"))
        run_id = run_data["data"]["id"]
        dataset_id = run_data["data"]["defaultDatasetId"]
        
    print(f"[*] Started Apify Actor Run ID: {run_id}. Waiting for completion...")
    
    status_url = f"https://api.apify.com/v2/actor-runs/{run_id}?token={token}"
    while True:
        time.sleep(5)
        try:
            req_status = urllib.request.Request(status_url)
            with urllib.request.urlopen(req_status, timeout=30) as resp:
                s_data = json.loads(resp.read().decode("utf-8"))
                status = s_data["data"]["status"]
                if status == "SUCCEEDED":
                    print(f"[+] Apify Run {run_id} succeeded! Fetching dataset...")
                    break
                elif status in ("FAILED", "ABORTED", "TIMED-OUT"):
                    raise RuntimeError(f"Apify run {run_id} finished with status: {status}")
                else:
                    pass
        except (urllib.error.URLError, TimeoutError, OSError) as e:
            print(f"[!] Polling network notice: {e}. Retrying in 5s...")
            continue

    dataset_url = f"https://api.apify.com/v2/datasets/{dataset_id}/items?token={token}&format=json"
    for attempt in range(5):
        try:
            cmd = ["curl", "-s", "--retry", "3", "--retry-delay", "2", dataset_url]
            out = subprocess.check_output(cmd)
            return json.loads(out.decode("utf-8"))
        except Exception as e:
            if attempt == 4:
                raise
            time.sleep(3)

def save_cluster_files(cluster_num, records):
    meta = CLUSTER_METAS[cluster_num]
    csv_file = os.path.join(BASE_DIR, f"{meta['slug']}.csv")
    md_file = os.path.join(BASE_DIR, f"{meta['slug']}.md")
    
    fieldnames = ["company_name", "contact_name", "email", "phone", "linkedin"]
    
    # Write CSV
    with open(csv_file, "w", encoding="utf-8", newline="") as f_csv:
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
        
    # Write Markdown
    with open(md_file, "w", encoding="utf-8") as f_md:
        f_md.write(f"# {meta['title']}\n")
        f_md.write(f"### {meta['subtitle']}\n\n")
        f_md.write(f"**Total Records**: {len(records)} Organizations\n\n")
        f_md.write("---\n\n")
        f_md.write("| company_name | contact_name | email | phone | linkedin |\n")
        f_md.write("| :--- | :--- | :--- | :--- | :--- |\n")
        for r in records:
            li_link = f"[{r['contact_name']}]({r['linkedin']})" if r.get('linkedin') else ""
            f_md.write(f"| {r['company_name']} | {r['contact_name']} | {r.get('email', '')} | {r.get('phone', '')} | {li_link} |\n")
            
    print(f"[+] Saved {csv_file} ({len(records)} rows) and {md_file}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cluster", type=int, default=1, help="Cluster number (1-5)")
    parser.add_argument("--limit", type=int, default=10, help="Number of companies to process")
    parser.add_argument("--offset", type=int, default=0, help="Start offset")
    args = parser.parse_args()

    token = get_apify_token()
    if not token:
        print("[ERROR] Apify Token not found in .env or environment!")
        return

    all_companies = load_companies()
    cl_key = f"Cluster {args.cluster}"
    cl_companies = [c for c in all_companies if c["cluster"] == cl_key]
    
    batch = cl_companies[args.offset : args.offset + args.limit]
    print(f"[*] Processing Cluster {args.cluster}: {len(batch)} companies (offset {args.offset} to {args.offset + len(batch)})")

    queries = []
    company_li_map = {}
    company_info_map = {}
    for c in batch:
        clean_name = clean_company_name(c["name"])
        role_filter = CLUSTER_ROLES.get(cl_key, CLUSTER_ROLES["Cluster 1"])
        
        # 1. LinkedIn decision maker query
        q_li = f'site:linkedin.com/in/ "{clean_name}" {role_filter} "Nigeria"'
        queries.append(q_li)
        company_li_map[q_li] = c
        
        # 2. Official company phone and email query
        q_info = f'{clean_name} official email contact Nigeria'
        queries.append(q_info)
        company_info_map[q_info] = c
        
        print(f"  -> [{c['id']}] {c['name']} (LinkedIn + Contact queries queued)")

    print(f"[*] Dispatching {len(queries)} queries ({len(batch)} LinkedIn + {len(batch)} Contact) to Apify...")
    results = run_apify_batch(token, queries)
    print(f"[*] Received {len(results)} items from Apify. Parsing results...")

    company_results = {c["id"]: {"company": c, "contact_name": "", "linkedin": "", "email": "", "phone": ""} for c in batch}

    for item in results:
        q_term = item.get("searchQuery", {}).get("term", "")
        organic = item.get("organicResults", [])
        
        is_li = "site:linkedin.com/in/" in q_term
        matched_company = None
        for c in batch:
            clean_name = clean_company_name(c["name"]).lower()
            if clean_name in q_term.lower():
                matched_company = c
                break
        if not matched_company:
            matched_company = company_li_map.get(q_term) or company_info_map.get(q_term)
        if not matched_company:
            continue
            
        cid = matched_company["id"]

        if is_li:
            best_profile = None
            # Preference 1: Explicit Nigerian LinkedIn profile (ng.linkedin.com/in/)
            for res in organic:
                url = res.get("url", "")
                if "ng.linkedin.com/in/" in url:
                    best_profile = res
                    break
                    
            # Preference 2: linkedin.com/in/ mentioning Nigeria without a foreign country subdomain
            if not best_profile:
                for res in organic:
                    url = res.get("url", "")
                    desc = res.get("description", "")
                    title = res.get("title", "")
                    if "linkedin.com/in/" in url and "nigeria" in (desc + title).lower():
                        m = re.match(r'https?://([a-z]{2})\.linkedin\.com/in/', url)
                        if not m or m.group(1) == "ng":
                            best_profile = res
                            break

            # Preference 3: Any linkedin.com/in/ mentioning Nigeria
            if not best_profile:
                for res in organic:
                    url = res.get("url", "")
                    desc = res.get("description", "")
                    title = res.get("title", "")
                    if "linkedin.com/in/" in url and "nigeria" in (desc + title).lower():
                        best_profile = res
                        break

            # Preference 4: Any linkedin.com/in/
            if not best_profile:
                for res in organic:
                    url = res.get("url", "")
                    if "linkedin.com/in/" in url:
                        best_profile = res
                        break

            if best_profile:
                name, _ = parse_serp_title(best_profile.get("title", ""))
                company_results[cid]["contact_name"] = re.sub(r'\(.*?\)', '', name).strip()
                company_results[cid]["linkedin"] = best_profile.get("url", "")

                snippet_text = f"{best_profile.get('description', '')} {best_profile.get('title', '')}"
                em_m = re.search(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', snippet_text)
                if em_m:
                    company_results[cid]["email"] = em_m.group(0).rstrip('.,;')
                ph_m = re.search(r'(?:\+?234|0)[789][01]\d{8}', snippet_text)
                if ph_m:
                    company_results[cid]["phone"] = ph_m.group(0).strip()
                    
        else:
            c = matched_company
            cid = c["id"]
            clean_name = clean_company_name(c["name"])
            info_email, info_phone = extract_contact_details(organic, clean_name)
            if not company_results[cid]["email"] and info_email:
                company_results[cid]["email"] = info_email
            if not company_results[cid]["phone"] and info_phone:
                company_results[cid]["phone"] = info_phone

    enriched_records = []
    for c in batch:
        r = company_results[c["id"]]
        enriched_records.append({
            "company_name": c["name"],
            "contact_name": r["contact_name"],
            "email": r["email"],
            "phone": r["phone"],
            "linkedin": r["linkedin"]
        })

    # Read existing CSV if exists, update or append
    csv_file = os.path.join(BASE_DIR, f"{CLUSTER_METAS[args.cluster]['slug']}.csv")
    existing_records = []
    if os.path.exists(csv_file):
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            existing_records = list(reader)

    # Merge by company_name
    record_dict = {r["company_name"]: r for r in existing_records}
    for r in enriched_records:
        record_dict[r["company_name"]] = r

    # Sort in order of original companies
    final_records = []
    for c in cl_companies:
        if c["name"] in record_dict:
            final_records.append(record_dict[c["name"]])

    save_cluster_files(args.cluster, final_records)

    print("\n--- ENRICHED BATCH RESULTS ---")
    for r in enriched_records:
        print(f"{r['company_name']} | {r['contact_name']} | {r['email']} | {r['phone']} | {r['linkedin']}")

if __name__ == "__main__":
    main()
