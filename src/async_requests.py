import asyncio
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

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

    def status(self):
        """returns the status if there is a reponse."""
        if self.response is None:
            return None
        return self.response


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
    except httpx.RequestError as error:
        result.error = error

    return result


def run_requests(
    urls: List[str], client_kwargs: Dict[str, Any] = None
) -> List[Result]:
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


def run_request_attempts(
    urls: List[str], *, attempts=1, client_kwargs: Dict[str, Any] = None
) -> List[Result]:
    """Run the requests many times."""

    results = run_requests(urls, client_kwargs=client_kwargs)
    while attempts > 1:
        attempts -= 1
        # urls_attempts = [
        #     result.url for result in results if result.status != 200
        # ]
        results_attempt = run_requests(urls, client_kwargs=client_kwargs)
        results.extend(results_attempt)
    return results
