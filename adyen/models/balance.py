from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Balance(SdkBaseModel):
    available: int
    """The balance available for use."""

    balance: int
    """The sum of the transactions that have already been settled."""

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__ of the
    balance."""

    pending: Optional[int] = UNSET
    """The sum of the transactions that will be settled in the future."""

    pending_available: Optional[int] = Field(default=UNSET, alias="pendingAvailable")
    """The balance that will become the available balance after the pending balance is settled.

    The pending available balance is equal to the lower of the following:
    - The ``pending`` balance
    - The ``pending`` balance plus the ``available`` balance."""

    reserved: int
    """The balance currently held in reserve."""


class BalanceDict(TypedDict):
    available: int
    balance: int
    currency: str
    pending: NotRequired[int]
    pending_available: NotRequired[int]
    reserved: int
