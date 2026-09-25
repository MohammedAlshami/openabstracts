// Usage: OPENABSTRACTS_KEY=isk_live_... npx tsx search.ts "your query"
interface Paper {
  id: string
  doi: string
  title: string
  authors: string[]
  year: number | null
  journal: string
  abstract: string
  pdfUrl: string
  url: string
  quartile: string
}

interface SearchResponse {
  success: boolean
  total: number
  references: Paper[]
}

async function search(q: string, opts: { mode?: "papers" | "content"; quartile?: string; limit?: number } = {}) {
  const params = new URLSearchParams({ q, limit: String(opts.limit ?? 5), mode: opts.mode ?? "papers" })
  if (opts.quartile) params.set("quartile", opts.quartile)
  const res = await fetch(`https://openabstracts.com/api/references-search?${params}`, {
    headers: { "x-api-key": process.env.OPENABSTRACTS_KEY! },
  })
  if (!res.ok) throw new Error(`${res.status} ${await res.text()}`)
  return (await res.json()) as SearchResponse
}

const { total, references } = await search(process.argv.slice(2).join(" ") || "machine learning", { quartile: "Q1,Q2" })
console.log(`${total} matches`)
references.forEach((p) => console.log(`- ${p.year} ${p.title} (${p.doi})`))
