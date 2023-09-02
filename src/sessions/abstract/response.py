import typing


class AwaitableJsonResponseProtocol(typing.Protocol):
    """Interface for any session HTTP response with awaitable json."""

    status_code: int

    async def json(self) -> dict[str, typing.Any]:
        """Return body as dict."""
        ...

    def raise_for_status(self):
        """Raise an error if status is not 2xx."""
        ...


class ResponseProtocol(typing.Protocol):
    """Interface for any session HTTP response."""

    status_code: int

    def json(self) -> dict[str, typing.Any]:
        """Return body as dict."""
        ...

    def raise_for_status(self):
        """Raise an error if status is not 2xx."""
        ...


ResponseT_co = typing.TypeVar(
    "ResponseT_co",
    AwaitableJsonResponseProtocol,
    ResponseProtocol,
    covariant=True,
)

AnyResponse = ResponseProtocol | AwaitableJsonResponseProtocol
