from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GetTerminalDetailsRequest(SdkBaseModel):
    terminal: str
    """The unique terminal ID in the format ``[Device model]-[Serial number]``.

    For example, **V400m-324689776**."""


class GetTerminalDetailsRequestDict(TypedDict):
    terminal: str
