try:
    import shodan  # type: ignore[import-not-found]
except ImportError:
    print("[-] Missing dependency: 'shodan' is not installed. Install it with: pip install shodan")
    sys.exit(1)

import sys
import json

SHODAN_API_KEY = "YOUR_SHODAN_API_KEY_HERE"  # Replace with your actual Shodan API key

try:
    api = shodan.Shodan(SHODAN_API_KEY)
except Exception as e:
    print(f"[-] Failed to initialize Shodan API: {e}")
    sys.exit(1)

def hunt_and_dump_certs(jarm_hash, limit=5):
    """
    Queries Shodan for a JARM fingerprint, extracts specific SSL 
    certificate details, and dumps the raw JSON to a file.
    """
    query = f"ssl.jarm:{jarm_hash}"
    print(f"[*] Executing query: {query}")
    
    try:
        results = api.search(query, limit=limit)
        print(f"[*] Found {results['total']} matches. Processing top {limit}...\n")
        
        for result in results['matches']:
            ip = result['ip_str']
            
            # 1. Safely extract the nested SSL/Cert data
            ssl_data = result.get('ssl', {})
            cert_data = ssl_data.get('cert', {})
            
            subject = cert_data.get('subject', {})
            issuer = cert_data.get('issuer', {})
            serial = cert_data.get('serial', 'N/A')
            
            print(f"[+] Target: {ip}")
            print(f"    Subject: {subject}")
            print(f"    Issuer:  {issuer}")
            print(f"    Serial:  {serial}")
            print("-" * 50)
            
            # 2. Dump the full raw JSON to a file for this specific IP
            # We use json.dumps() with an indent for readability
            raw_json_string = json.dumps(result, indent=4)
            filename = f"{ip.replace('.', '_')}_shodan.json"
            
            with open(filename, "w") as f:
                f.write(raw_json_string)
                
    except shodan.APIError as e:
        print(f"[-] Shodan API Error: {e}")

if __name__ == "__main__":
    target_jarm = "YOUR_JARM_HASH_HERE"  # Replace with the actual JARM hash you want to search for
    hunt_and_dump_certs(target_jarm, limit=10)