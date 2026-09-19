"""Minimal GreenGuru Signal API example using only Python's standard library."""

from __future__ import annotations

import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API = "https://www.greenguruai.com/api/v1/signals"


def fetch_signals(
    *,
    country: str = "uk",
    topic: str | None = None,
    since: str | None = None,
    limit: int = 5,
) -> dict:
    params: dict[str, str | int] = {
        "country": country,
        "limit": limit,
    }

    if topic:
        params["topic"] = topic
    if since:
        params["since"] = since

    request = Request(
        f"{API}?{urlencode(params)}",
        headers={
            "Accept": "application/json",
            "User-Agent": "greenguruai-signal-client/0.1",
        },
    )

    with urlopen(request, timeout=15) as response:
        return json.load(response)


def main() -> None:
    payload = fetch_signals(country="uk", limit=5)

    if not payload.get("ok"):
        raise RuntimeError(f"Unexpected API response: {payload!r}")

    for signal in payload.get("items", []):
        print(signal["headline"])
        print(f"  Event date:           {signal['eventDate']}")
        print(f"  Source page updated:  {signal.get('sourcePageUpdatedAt')}")
        print(f"  GreenGuruAI reviewed: {signal['reviewedAt']}")
        print(f"  Source:               {signal['sourceOrganisation']}")
        print(f"  Source URL:           {signal['sourceUrl']}")
        print()


if __name__ == "__main__":
    main()
