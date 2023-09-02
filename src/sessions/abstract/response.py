import typing


class ResponseProxyProtocol(typing.Protocol):
    """Interface for any session HTTP response."""

    status_code: int

    def json(self) -> dict[str, typing.Any]:
        """Return body as dict."""
        ...

    def raise_for_status(self):
        """Raise an error if status is not 2xx."""
        ...


ResponseT = typing.TypeVar(
    "ResponseT",
    bound=ResponseProxyProtocol,
)
