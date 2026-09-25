// Usage: OPENABSTRACTS_KEY=isk_live_... node search.mjs "your query"
const q = process.argv.slice(2).join(" ") || "supply chain resilience"
const url = new URL("https://openabstracts.com/api/references-search")
url.search = new URLSearchParams({ q, limit: "5", yearFrom: "2020" }).toString()

const res = await fetch(url, { headers: { "x-api-key": process.env.OPENABSTRACTS_KEY } })
if (!res.ok) throw new Error(`${res.status} ${await res.text()}`)
const { total, references } = await res.json()
console.log(`${total} matches`)
for (const p of references) console.log(`- ${p.year}  ${p.title}  (${p.journal})  ${p.doi}`)
