from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount17 import Amount17, Amount17Dict
from .enums.balance_transfer_type2 import BalanceTransferType2OrStr


class BalanceTransferRequest(SdkBaseModel):
    amount: Amount17
    """The amount of the transfer."""

    from_merchant: str = Field(alias="fromMerchant")
    """The unique identifier of the source merchant account from which funds are deducted."""

    reference: Optional[str] = UNSET
    """A reference for the balance transfer. Maximum length: 80 characters."""

    to_merchant: str = Field(alias="toMerchant")
    """The unique identifier of the destination merchant account to which funds are transferred."""

    type_: BalanceTransferType2OrStr = Field(alias="type")
    """The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and
    **adjustment**."""


class BalanceTransferRequestDict(TypedDict):
    amount: Amount17Dict
    from_merchant: str
    reference: NotRequired[str]
    to_merchant: str
    type_: BalanceTransferType2OrStr
