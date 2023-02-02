import asyncio
from dataclasses import dataclass
from typing import List, Optional

import httpx

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}


@dataclass
class Result:
    """Class for keeping track of responses and errors."""

    url: str
    response: Optional[httpx.Response] = None
    error: Optional[httpx.RequestError] = None
    status: Optional[int] = None


async def get_async(
    url: str, *, follow_redirects=True, headers=HEADERS, **kwargs
) -> Result:
    """Send a asynchronous `GET` request."""
    result = Result(url=url)
    try:
        async with httpx.AsyncClient(
            headers=headers, follow_redirects=follow_redirects, **kwargs
        ) as client:
            res = await client.get(url)
            result.response = res
            result.status = res.status_code
    except httpx.RequestError as error:
        result.error = error

    return result


def run_requests(urls: List[str], **client_kwargs) -> List[Result]:
    """Run the event loop until all requests are done."""

    client_kwargs = client_kwargs or {}

    async def main():
        results = await asyncio.gather(
            *[get_async(url, **client_kwargs) for url in urls]
        )
        return results

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(main())
    return results


def make_chunck(list_of_urls, chunck_size=10):
    start, end, chunck_size = 0, len(list_of_urls), max(chunck_size, 1)
    while start < end:
        stop = min(start + chunck_size, end)
        yield list_of_urls[start:stop]
        start = stop


def get_results(urls_servicos, follow_redirects=False, chunck_size=20):
    results_200 = {}
    results_not200 = {}
    for urls_chunk in make_chunck(urls_servicos, chunck_size):
        results = run_requests(urls_chunk, follow_redirects=follow_redirects)
        for r in results:
            if r.status == 200:
                results_200[r.url] = r
            else:
                results_not200[r.url] = r
    return results_200, results_not200


def run_async_requests(
    urls_servicos: List,
    attenpts: int = 5,
    chunck_size: int = 20,
    follow_redirects=False,
):
    result200 = []
    history = []

    for n in range(attenpts):
        r200, rnot200 = get_results(
            urls_servicos,
            follow_redirects=follow_redirects,
            chunck_size=chunck_size,
        )
        result200.append(r200)
        history.append(rnot200)
        urls_servicos = list(rnot200.keys())
