"""Check whether a cited paper exists in the index.

Usage: OPENABSTRACTS_KEY=isk_live_... python verify_citation.py "Paper title" [year]
Prints the matching record (with its real DOI) or says it wasn't found.
"""
import difflib
import os
import sys

import requests

title = sys.argv[1]
year = int(sys.argv[2]) if len(sys.argv) > 2 else None

params = {"q": title, "limit": 5}
if year:
    params.update(yearFrom=year - 1, yearTo=year + 1)

hits = requests.get(
    "https://openabstracts.com/api/references-search",
    params=params,
    headers={"x-api-key": os.environ["OPENABSTRACTS_KEY"]},
    timeout=30,
).json().get("references", [])

best, score = None, 0.0
for h in hits:
    s = difflib.SequenceMatcher(None, title.lower(), h["title"].lower()).ratio()
    if s > score:
        best, score = h, s

if best and score >= 0.85:
    print(f"FOUND ({score:.0%} title match)")
    print(f"  {best['title']} — {', '.join(best['authors'][:3])} ({best['year']}), {best['journal']}")
    print(f"  DOI: {best['doi']}")
else:
    print("NOT FOUND in the index (absence here is not proof the paper doesn't exist).")
