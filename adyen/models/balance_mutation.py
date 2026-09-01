from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BalanceMutation(SdkBaseModel):
    balance: Optional[int] = UNSET
    """The amount in the payment's currency that is debited or credited on the balance accounting register."""

    currency: Optional[str] = UNSET
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__."""

    received: Optional[int] = UNSET
    """The amount in the payment's currency that is debited or credited on the received accounting register."""

    reserved: Optional[int] = UNSET
    """The amount in the payment's currency that is debited or credited on the reserved accounting register."""


class BalanceMutationDict(TypedDict):
    balance: NotRequired[int]
    currency: NotRequired[str]
    received: NotRequired[int]
    reserved: NotRequired[int]
