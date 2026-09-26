<p align="center"><img src="logo.png" alt="OpenAbstracts" width="120"></p>

# OpenAbstracts

**Paper search API and MCP server** for 10M+ academic papers from 100,000+ journals.

Keyword search over titles and abstracts, or full-text search inside the PDFs with highlighted snippets. Every result includes title, authors, year, journal, DOI, abstract, journal quartile and links to the PDF and publisher page.

- 🔎 One REST endpoint: `GET /api/references-search`
- 🤖 Remote **MCP server** for Claude, Cursor and other assistants: `https://openabstracts.com/mcp`
- ✅ A **Claude Skill** that makes an assistant verify citations before using them
- 💸 **100 free searches every month**, then $1.50 per 1,000 searches. Empty searches are never billed.

Website: <https://openabstracts.com> · Docs: <https://openabstracts.com/docs> · OpenAPI: [`openapi.json`](openapi.json)

> This repository holds documentation, samples and the Skill. The service itself is hosted at openabstracts.com.

## Quickstart

1. Create a free account and an API key at <https://openabstracts.com/api-keys> (keys start with `isk_live_`).
2. Search:

```bash
curl "https://openabstracts.com/api/references-search?q=marketing&limit=3" \
  -H "x-api-key: isk_live_YOUR_KEY"
```

### Parameters

| Parameter | Description |
|---|---|
| `q` | Search query |
| `mode` | `papers` (titles, abstracts, keywords, authors — default) or `content` (full PDF text, returns `highlights`) |
| `category` | Subject filter, e.g. `business`, `medicine`, `engineering`, `physics`, `law` |
| `yearFrom`, `yearTo` | Inclusive publication years |
| `quartile` | Comma-separated journal quartiles, e.g. `Q1,Q2` |
| `page`, `limit` | Pagination (max 100 per page) |

### Response

```json
{
  "success": true,
  "total": 21742,
  "page": 1,
  "limit": 3,
  "mode": "papers",
  "references": [
    {
      "id": "6aafc30105cf5ce509d69aa6",
      "doi": "10.12775/EQUIL.2009.011",
      "title": "Market basket analysis in marketing research",
      "authors": ["Małgorzata Śniegocka - Łusiewicz"],
      "year": 2009,
      "journal": "Equilibrium. Quarterly Journal of Economics and Economic Policy",
      "abstract": "…",
      "category": "business",
      "pdfUrl": "https://economic-policy.pl/index.php/eq/article/download/567/531",
      "url": "https://economic-policy.pl/index.php/eq/article/view/567",
      "quartile": "",
      "score": 32.97
    }
  ]
}
```

### Other endpoints

- `GET /api/health` — service health, no authentication

Errors: `401` missing/invalid key · `402` free allowance used and balance too low · `403` key expired or limit reached · `500` internal error.

## Samples

| Language | File |
|---|---|
| Python | [`examples/search.py`](examples/search.py) |
| Node.js | [`examples/search.mjs`](examples/search.mjs) |
| TypeScript | [`examples/search.ts`](examples/search.ts) |
| Citation checker (Python) | [`examples/verify_citation.py`](examples/verify_citation.py) |

```python
import requests

r = requests.get(
    "https://openabstracts.com/api/references-search",
    params={"q": "supply chain resilience", "yearFrom": 2021, "limit": 5},
    headers={"x-api-key": "isk_live_YOUR_KEY"},
    timeout=30,
)
for p in r.json()["references"]:
    print(p["year"], p["title"], p["doi"])
```

## MCP server

Give an AI assistant direct access to the search. The server exposes one tool, `search_papers`, with the same parameters as the REST endpoint.

**Claude:** Settings → Connectors → *Add custom connector* → URL `https://openabstracts.com/mcp` → **Connect**. You'll sign in on an OpenAbstracts page and choose which API key to authorise (standard OAuth with PKCE — Claude never sees your key).

**Other MCP clients** that support static headers:

```json
{
  "mcpServers": {
    "openabstracts": {
      "url": "https://openabstracts.com/mcp",
      "headers": { "x-api-key": "isk_live_YOUR_KEY" }
    }
  }
}
```

MCP calls are billed exactly like REST calls.

## Claude Skill: verify citations

[`skills/openabstracts-citations/SKILL.md`](skills/openabstracts-citations/SKILL.md) teaches an assistant to **search before it cites**, never to invent a DOI or author, and to say so when the index has nothing. It needs the MCP connector above.

- **Claude Code:** copy the `openabstracts-citations` folder into `~/.claude/skills/`.
- **Claude apps:** upload the folder as a custom Skill from the Skills settings.

## Guides

- [Search 10 million papers with one curl call](https://openabstracts.com/blogs/search-10m-papers-with-one-curl-call)
- [Add real citations to an AI chatbot](https://openabstracts.com/blogs/add-real-citations-to-an-ai-chatbot)
- [Citation verification for AI writing tools](https://openabstracts.com/blogs/citation-verification-for-ai-essay-tools)
- [RAG over academic literature](https://openabstracts.com/blogs/rag-over-academic-literature)
- [Connect OpenAbstracts to Claude with MCP](https://openabstracts.com/mcp/doc)

## What it is not

OpenAbstracts is a search API. It doesn't provide citation graphs, embeddings or generated text, and the index covers registered journals rather than every paper ever published.

## Support

contact@openabstracts.com · [Terms](https://openabstracts.com/terms) · [Privacy](https://openabstracts.com/privacy)

## License

The samples and documentation in this repository are MIT licensed. The hosted service is governed by its [Terms of Service](https://openabstracts.com/terms).
