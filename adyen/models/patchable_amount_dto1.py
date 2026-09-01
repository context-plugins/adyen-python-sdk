from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PatchableAmountDto1(SdkBaseModel):
    """The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated."""

    currency: Optional[str] = UNSET
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""

    value: Optional[int] = UNSET
    """The amount of the transaction, in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__."""


class PatchableAmountDto1Dict(TypedDict):
    currency: NotRequired[str]
    value: NotRequired[int]
