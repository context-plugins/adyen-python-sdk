from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class DetailBalance3(SdkBaseModel):
    """Details of the balance held by the account."""

    balance: Optional[list[Amount]] = UNSET
    """The list of balances held by the account."""

    on_hold_balance: Optional[list[Amount]] = Field(default=UNSET, alias="onHoldBalance")
    """The list of on hold balances held by the account."""

    pending_balance: Optional[list[Amount]] = Field(default=UNSET, alias="pendingBalance")
    """The list of pending balances held by the account."""


class DetailBalance3Dict(TypedDict):
    balance: NotRequired[list[AmountDict]]
    on_hold_balance: NotRequired[list[AmountDict]]
    pending_balance: NotRequired[list[AmountDict]]
