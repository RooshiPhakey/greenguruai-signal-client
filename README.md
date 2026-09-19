# GreenGuruAI Signal Client

Tiny, dependency-light Python and JavaScript examples for the free **GreenGuru Signal API v1**.

GreenGuruAI publishes source-linked, human-reviewed cannabis regulatory and policy Signals across the **UK, Spain and the Netherlands**. This repository shows the simplest way to consume that public data without requiring an API key or a full SDK.

> **v0.1.0 is now available**  
> Initial public release with Python and JavaScript examples, API filtering, source attribution, date-field handling and RSS guidance.

## Quick start

### Python

Uses Python's standard library only.

```bash
python python/example.py
```

### JavaScript

Requires Node.js 18+ and uses the built-in `fetch` API.

```bash
node javascript/example.mjs
```

## Public API

Base endpoint:

```text
https://www.greenguruai.com/api/v1/signals
```

Example request:

```text
https://www.greenguruai.com/api/v1/signals?country=uk&limit=10
```

Supported filters include:

| Parameter | Example | Purpose |
| --- | --- | --- |
| `country` | `uk` | Filter by jurisdiction |
| `topic` | `cbd-regulation` | Filter by Signal topic |
| `sort` | `reviewed` | Sort by event or review date |
| `since` | `2026-09-01` | Filter by GreenGuruAI review date |
| `limit` | `10` | Limit returned records |

No API key is required for the public v1 endpoint.

## API resources

**Developer & Media documentation**  
https://www.greenguruai.com/developers

**Signal API**  
https://www.greenguruai.com/api/v1/signals

**RSS feed**  
https://www.greenguruai.com/signal/feed.xml

**Public Signals**  
https://www.greenguruai.com/signal

## Example Signal

```json
{
  "id": "example-signal-id",
  "country": "United Kingdom",
  "countrySlug": "uk",
  "topic": "cbd-regulation",
  "eventDate": "2026-09-09",
  "sourcePageUpdatedAt": null,
  "reviewedAt": "2026-09-12",
  "headline": "Example headline",
  "summary": "Example summary",
  "sourceOrganisation": "Example regulator",
  "sourceUrl": "https://example.org/source",
  "contextUrl": "/pulse"
}
```

### Date handling matters

The API deliberately keeps three dates separate:

- `eventDate` — when the underlying event occurred
- `sourcePageUpdatedAt` — when the source page says it was updated, when a reliable date exists
- `reviewedAt` — when GreenGuruAI reviewed the Signal for public publication

`sourcePageUpdatedAt` can legitimately be `null`.

Do not treat `reviewedAt` as the date the underlying event happened.

## Python example

```python
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json

API = "https://www.greenguruai.com/api/v1/signals"

query = urlencode({
    "country": "uk",
    "limit": 5,
})

request = Request(
    f"{API}?{query}",
    headers={"User-Agent": "greenguruai-signal-client/0.1"},
)

with urlopen(request, timeout=15) as response:
    payload = json.load(response)

for signal in payload["items"]:
    print(signal["headline"])
    print("Event:", signal["eventDate"])
    print("Source page updated:", signal["sourcePageUpdatedAt"])
    print("Reviewed:", signal["reviewedAt"])
    print("Source:", signal["sourceUrl"])
    print()
```

## JavaScript example

```js
const API = 'https://www.greenguruai.com/api/v1/signals'

const url = new URL(API)
url.searchParams.set('country', 'uk')
url.searchParams.set('limit', '5')

const response = await fetch(url)

if (!response.ok) {
  throw new Error(`GreenGuruAI API returned ${response.status}`)
}

const payload = await response.json()

for (const signal of payload.items) {
  console.log(signal.headline)
  console.log('Event:', signal.eventDate)
  console.log('Source page updated:', signal.sourcePageUpdatedAt)
  console.log('Reviewed:', signal.reviewedAt)
  console.log('Source:', signal.sourceUrl)
  console.log()
}
```

## RSS alternative

If you do not need JSON, subscribe directly to the public RSS 2.0 feed:

```text
https://www.greenguruai.com/signal/feed.xml
```

This is useful for newsrooms, monitoring tools, internal intelligence workflows and lightweight publishing integrations.

## Attribution

If you display or republish a GreenGuruAI-authored Signal projection, retain GreenGuruAI attribution and the original source trail.

Suggested short credit:

> Source: GreenGuruAI Signal — [headline], reviewed [date]. Original source: [organisation].

Where practical, link **GreenGuruAI Signal** to the relevant public Signal or GreenGuruAI context URL.

## v0.1.0

**Initial public release**

Includes Python and JavaScript examples, supported API filters, source attribution, RSS guidance and explicit handling of `eventDate`, `sourcePageUpdatedAt` and `reviewedAt`.

Release documentation:  
https://www.greenguruai.com/developers

## Scope

This repository is intentionally small. It is an example client rather than a full SDK.

The public API is designed for lightweight discovery and interoperability. It is rate-bounded and is not presented as a bulk-extraction service or SLA-backed commercial feed.

## Reuse and evidence boundaries

GreenGuruAI provides informational intelligence, not medical or legal advice.

When using the public data, preserve original-source attribution, keep event and review dates distinct, and do not present GreenGuruAI evidence states as legal certification, regulatory approval, clinical endorsement or medical advice.

Third-party source material remains subject to the rights and restrictions of its original publishers.

## License

The example client code in this repository is available under the **MIT License**.

GreenGuruAI API data and third-party source material remain subject to GreenGuruAI's terms and any rights attached to the original sources.

---

**GreenGuruAI**  
Regulatory intelligence for a more accessible tomorrow.

https://www.greenguruai.com
