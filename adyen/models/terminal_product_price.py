from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class TerminalProductPrice(SdkBaseModel):
    currency: Optional[str] = UNSET
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""

    value: Optional[float] = UNSET
    """The price of the item."""


class TerminalProductPriceDict(TypedDict):
    currency: NotRequired[str]
    value: NotRequired[float]
