"""Search OpenAbstracts. Usage: OPENABSTRACTS_KEY=isk_live_... python search.py "your query" """
import os
import sys

import requests

query = " ".join(sys.argv[1:]) or "supply chain resilience"
resp = requests.get(
    "https://openabstracts.com/api/references-search",
    params={"q": query, "limit": 5, "yearFrom": 2020},
    headers={"x-api-key": os.environ["OPENABSTRACTS_KEY"]},
    timeout=30,
)
resp.raise_for_status()
data = resp.json()
print(f"{data['total']} matches")
for p in data["references"]:
    print(f"- {p['year']}  {p['title']}  ({p['journal']})  https://doi.org/{p['doi']}" if p["doi"] else f"- {p['year']}  {p['title']}")
