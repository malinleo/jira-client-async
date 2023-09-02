import asyncio
import typing

import aiohttp

from .. import abstract


class AioHTTPResponseProxy(abstract.ResponseProxyProtocol):
    """Proxy class for aiohttp response."""

    def __init__(self, response: aiohttp.ClientResponse) -> None:
        self._response = response
        self.status_code = response.status

    def json(self) -> dict[str, typing.Any]:
        """Return response body as json."""
        return asyncio.run(self._response.json())

    def raise_for_status(self):
        """Raise error if status in not 2xx."""
        return self._response.raise_for_status()
