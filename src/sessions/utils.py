from .sessions import abstract as session_abs
import asyncio
import typing


def get_json(response: session_abs.AnyResponse) -> dict[str, typing.Any]:
    if asyncio.iscoroutinefunction(response.json):
        return asyncio.run(response.json())
    return response.json()  # type: ignore
