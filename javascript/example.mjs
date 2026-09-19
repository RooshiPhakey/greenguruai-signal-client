// Minimal GreenGuru Signal API example for Node.js 18+.

const API = 'https://www.greenguruai.com/api/v1/signals'

async function fetchSignals({
  country = 'uk',
  topic,
  since,
  limit = 5,
} = {}) {
  const url = new URL(API)

  url.searchParams.set('country', country)
  url.searchParams.set('limit', String(limit))

  if (topic) url.searchParams.set('topic', topic)
  if (since) url.searchParams.set('since', since)

  const response = await fetch(url, {
    headers: {
      Accept: 'application/json',
      'User-Agent': 'greenguruai-signal-client/0.1',
    },
  })

  if (!response.ok) {
    throw new Error(`GreenGuruAI API returned ${response.status}`)
  }

  return response.json()
}

const payload = await fetchSignals({
  country: 'uk',
  limit: 5,
})

if (!payload.ok) {
  throw new Error(`Unexpected API response: ${JSON.stringify(payload)}`)
}

for (const signal of payload.items ?? []) {
  console.log(signal.headline)
  console.log('  Event date:           ', signal.eventDate)
  console.log('  Source page updated:  ', signal.sourcePageUpdatedAt)
  console.log('  GreenGuruAI reviewed: ', signal.reviewedAt)
  console.log('  Source:               ', signal.sourceOrganisation)
  console.log('  Source URL:           ', signal.sourceUrl)
  console.log()
}
