import http
import typing
from . import abstract, exceptions
import aiohttp
from aiohttp.client_exceptions import ClientError


class AioHTTPAdapter(abstract.AsyncSessionAdapterProtocol):
    """Adapter for aiohttp session."""

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self._session: aiohttp.ClientSession = session

    async def request(
        self,
        method: http.HTTPMethod,
        url: str,
        headers: dict[str, str] | None = None,
        data: dict[str, typing.Any] | None = None,
        query_params: dict[str, str] | None = None,
        **kwargs: typing.Any,
    ) -> aiohttp.ClientResponse:
        async with self._session.request(
            method=method.value,
            url=url,
            headers=headers or {},
            data=data or {},
            query_params=query_params or {},
            **kwargs,
        ) as response:
            return response
