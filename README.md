# Shodan JARM Hunter

An active cyber threat intelligence (CTI) reconnaissance tool that leverages the Shodan API and JARM TLS fingerprinting to map adversary infrastructure, track Command and Control (C2) frameworks, and cluster typosquatting campaigns.

## The Use Case: Pivoting Beyond Basic IP IOCs

Traditional infrastructure hunting often relies on reactive, surface-level Indicators of Compromise (IOCs) like IP addresses and domain names. The limitation of this approach is that IP addresses are highly ephemeral—threat actors can rotate domains and spin up new virtual private servers (VPS) in minutes to evade blocklists.

**JARM fingerprinting shifts the hunt from surface indicators to underlying behaviors.**

Instead of asking *where* the server is hosted, JARM asks *how* the server's TLS stack is configured. By actively sending modified TLS Client Hello packets to a target, JARM generates a unique hash based on the server's specific responses. 

This provides massive leverage for CTI analysts:

* **Durability Over Ephemerality:** Even when an adversary rotates their IP address or switches hosting providers, their underlying technology stack remains unchanged. The JARM hash travels with the infrastructure.
* **Proactive Campaign Clustering:** Starting with a single reactive IOC—like one typosquatted domain—an analyst can extract its JARM hash and pivot. Querying that hash across internet scanning engines instantly clusters the actor’s broader, unannounced fleet of servers sharing that exact TLS configuration.
* **TTP Tracking:** Monitoring changes in JARM signatures allows defenders to track shifts in adversary Tactics, Techniques, and Procedures.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/YOUR-REPO.git](https://github.com/YOUR-USERNAME/YOUR-REPO.git)
   cd YOUR-REPO
