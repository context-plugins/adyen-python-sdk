from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_product import TerminalProduct, TerminalProductDict


class TerminalProductsResponse(SdkBaseModel):
    data: Optional[list[TerminalProduct]] = UNSET
    """Terminal products that can be ordered."""


class TerminalProductsResponseDict(TypedDict):
    data: NotRequired[list[TerminalProduct | TerminalProductDict]]
