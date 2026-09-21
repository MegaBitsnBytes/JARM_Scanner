Shodan JARM Hunter
A lightweight, active cyber threat intelligence (CTI) reconnaissance script that leverages the Shodan API and JARM TLS fingerprinting to map adversary infrastructure, track Command and Control (C2) frameworks, and cluster typosquatting campaigns.

The Use Case: Pivoting Beyond Ephemeral IOCs
Traditional infrastructure hunting often relies on reactive, surface-level Indicators of Compromise (IOCs) like IP addresses and domain names. The operational limitation of this approach is that IP addresses are highly ephemeral—threat actors can rotate domains and spin up new virtual private servers (VPS) in minutes to evade blocklists.

JARM fingerprinting shifts the hunt from surface indicators to underlying behaviors.

Instead of asking where the server is hosted, JARM asks how the server's TLS stack is configured. By actively sending modified TLS Client Hello packets to a target, JARM generates a unique hash based on the server's specific responses.

This provides massive leverage for CTI analysts:

Durability Over Ephemerality: Even when an adversary rotates their IP address or switches hosting providers, their underlying technology stack (e.g., a Go-based AiTM phishing proxy or a default Cobalt Strike team server) often remains unchanged. The JARM hash travels with the infrastructure.
Proactive Campaign Clustering: Starting with a single reactive IOC—like one typosquatted domain resolving to a single IP—an analyst can extract its JARM hash and pivot. Querying that hash across internet scanning engines (like Shodan) instantly clusters the actor’s broader, unannounced fleet of servers sharing that exact TLS configuration.
TTP Tracking: Monitoring changes in JARM signatures allows defenders to track shifts in adversary Tactics, Techniques, and Procedures (TTPs), such as migrating to a new C2 framework or updating backend evasion libraries.
Prerequisites
Python 3.x
A valid Shodan API Key (Free or Paid)
Quickstart / Installation
Clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
Install the required dependencies:

pip install -r requirements.txt
Add your API Key: Open the Python script (jarm_hunter.py) in your preferred text editor and replace the placeholder variable with your actual Shodan API key:

SHODAN_API_KEY = "YOUR_API_KEY_HERE"
(Note: Never commit your actual API key to a public GitHub repository!)

Usage
Run the script directly from your terminal. By default, it will query Shodan for the hardcoded JARM hash and print the results to the console.

python jarm_hunter.py
Advanced Usage (Customizing the Hunt)
To hunt for different threat actors or narrow down your results, you can edit the target_jarm variable inside the script, or append Shodan filters (like org or http.title) to the base query string to reduce false positives.

# Example: Hunting a specific JARM hash combined with a specific ASN/Hosting Provider
query = f'ssl.jarm:"{target_jarm}" org:"DigitalOcean, LLC"'
