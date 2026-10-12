from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class RefundFundsTransferRequest(SdkBaseModel):
    amount: Amount
    """The amount to be transferred."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """A value that can be supplied at the discretion of the executing user in order to link multiple transactions to
    one another."""

    original_reference: str = Field(alias="originalReference")
    """A PSP reference of the original fund transfer."""


class RefundFundsTransferRequestDict(TypedDict):
    amount: AmountDict
    merchant_reference: NotRequired[str]
    original_reference: str
