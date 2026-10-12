from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .terminal_product_price2 import TerminalProductPrice2, TerminalProductPrice2Dict


class TerminalProduct(SdkBaseModel):
    description: Optional[str] = UNSET
    """Information about items included and integration options."""

    id: Optional[str] = UNSET
    """The unique identifier of the product."""

    items_included: Optional[list[str]] = Field(default=UNSET, alias="itemsIncluded")
    """A list of parts included in the terminal package."""

    name: Optional[str] = UNSET
    """The descriptive name of the product."""

    price: Optional[TerminalProductPrice2] = UNSET
    """The price of the product."""


class TerminalProductDict(TypedDict):
    description: NotRequired[str]
    id: NotRequired[str]
    items_included: NotRequired[list[str]]
    name: NotRequired[str]
    price: NotRequired[TerminalProductPrice2Dict]
