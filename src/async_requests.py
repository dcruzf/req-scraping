import asyncio
from typing import List

import httpx

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}


async def get_async(url: str):
    """Send a asynchronous `GET` request."""
    try:
        async with httpx.AsyncClient(
            headers=HEADERS, follow_redirects=True
        ) as client:
            res = await client.get(url)
            res.original_url = url
        return res
    except httpx.RequestError as error:

        class Res:
            status_code = "error"
            e = error

        return Res


def run_requests(urls):
    """Run the event loop until all requests are done."""

    async def main():
        responses = await asyncio.gather(*[get_async(url) for url in urls])
        return responses

    loop = asyncio.get_event_loop()
    responses = loop.run_until_complete(main())
    return responses


def divide_chunks(items: list, n):
    """Divide a list in chunks."""
    for i in range(0, len(items), n):
        yield items[i : i + n]


def chunk_requests(urls, chunksize=10) -> List[httpx.Response]:
    """Run event loops with chunks of asynchronous `GET` request."""
    result = []
    for chunk in divide_chunks(urls, chunksize):
        result.extend(run_requests(chunk))
    return result
