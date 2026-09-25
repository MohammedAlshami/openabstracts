---
name: openabstracts-citations
description: Find real academic papers and verify citations using the OpenAbstracts journal-search index (300,000+ papers, 700+ registered journals). Use this whenever the user asks you to find a source, check whether a citation is real, fix a fabricated or vague reference, or needs a properly formatted citation for a claim.
---

# OpenAbstracts citation verification

You have access to an OpenAbstracts MCP connector when this Skill is invoked (the user must have added `https://openabstracts.com/mcp` as a connector — if its tool isn't available, tell the user to connect it first at https://openabstracts.com/docs). It exposes one tool, `search_papers` (possibly prefixed with the connector name, e.g. `openabstracts_search_papers` — look for a tool matching that shape among what's currently connected):

- **search_papers** — keyword search over titles/abstracts/full-text across 700+ registered journals. Takes `q` (required), plus optional `category`, `yearFrom`/`yearTo`, `quartile`, `mode` ("papers" or "content"), `page`, `limit`. Each result includes the title, authors, year, journal, DOI, abstract, and PDF/landing page links.

## When to use this Skill

- The user cites a paper, statistic, or claim and you're not certain it's real — search for it before repeating it as fact.
- The user asks "is this a real paper?" or "find the source for X."
- The user needs a citation (APA, MLA, or similar) for a claim in something they're writing.
- You are about to state a specific finding, author, or statistic from academic literature and don't already have a verified source in the conversation.

## How to use it

1. Call `search_papers` with the claim's key terms as `q`. Don't guess author names or DOIs — search first.
2. If nothing plausible comes back, say so plainly. Do **not** invent a citation, author, journal name, or DOI that didn't come from a real search result — a fabricated-but-plausible-looking citation is worse than admitting you couldn't verify one.
3. If a result matches, check its returned fields (title, authors, year, journal, DOI, abstract) against the claim before citing it. If several results are close, narrow with `yearFrom`/`yearTo` or a more specific query.
4. Format the citation from the real, returned fields only — never from memory or inference.

## Example

**User:** "Didn't a 2019 paper show the day-of-the-week effect disappears in African stock markets during bull regimes?"

1. Call `search_papers` with `q: "day-of-the-week effect African stock markets"`.
2. Read the matching result's year, authors, journal, and abstract to confirm it supports the claim.
3. Answer using only what the record actually says, and cite it: *Obalade, A. A., & Muzindutsi, P. F. (2019). The Adaptive Market Hypothesis and the Day-of-the-Week Effect in African Stock Markets: the Markov Switching Model. Comparative Economic Research.*

## Guidelines

- Never fabricate a DOI, author name, or journal — every citation must trace back to a real `search_papers` result.
- If the index doesn't have something, say it wasn't found rather than filling the gap with a plausible-sounding guess.
