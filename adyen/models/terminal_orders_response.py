from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_order import TerminalOrder, TerminalOrderDict


class TerminalOrdersResponse(SdkBaseModel):
    data: Optional[list[TerminalOrder]] = UNSET
    """List of orders for payment terminal packages and parts."""


class TerminalOrdersResponseDict(TypedDict):
    data: NotRequired[list[TerminalOrder | TerminalOrderDict]]
