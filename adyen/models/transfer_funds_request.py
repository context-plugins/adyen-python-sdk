from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict


class TransferFundsRequest(SdkBaseModel):
    amount: Amount
    """The amount to be transferred."""

    destination_account_code: str = Field(alias="destinationAccountCode")
    """The code of the account to which the funds are to be credited. >The state of the Account Holder of this account
    must be Active."""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """A value that can be supplied at the discretion of the executing user in order to link multiple transactions to
    one another."""

    source_account_code: str = Field(alias="sourceAccountCode")
    """The code of the account from which the funds are to be debited. >The state of the Account Holder of this account
    must be Active and allow payouts."""

    transfer_code: str = Field(alias="transferCode")
    """The code related to the type of transfer being performed. >The permitted codes differ for each platform account
    and are defined in their service level agreement."""


class TransferFundsRequestDict(TypedDict):
    amount: AmountDict
    destination_account_code: str
    merchant_reference: NotRequired[str]
    source_account_code: str
    transfer_code: str
