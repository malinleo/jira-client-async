import http
import typing

from . import response


class AsyncSessionAdapterProtocol(typing.Protocol):
    """Adapter protocol for any async session object."""

    _session: typing.Any

    async def request(
        self,
        method: http.HTTPMethod,
        url: str,
        headers: dict[str, str] | None = None,
        data: dict[str, typing.Any] | None = None,
        query_params: dict[str, str] | None = None,
        **kwargs: typing.Any,
    ) -> response.ResponseProxyProtocol:
        """Perform request with given method."""
        ...


class SyncSessionAdapterProtocol(typing.Protocol):
    """Adapter protocol for any sync session object."""

    _session: typing.Any

    def request(
        self,
        method: http.HTTPMethod,
        url: str,
        headers: dict[str, str] | None = None,
        data: dict[str, typing.Any] | None = None,
        query_params: dict[str, str] | None = None,
        **kwargs: typing.Any,
    ) -> response.ResponseProxyProtocol:
        """Perform request with given method."""
        ...


SessionT_co = typing.TypeVar(
    "SessionT_co",
    AsyncSessionAdapterProtocol,
    SyncSessionAdapterProtocol,
    covariant=True,
)
