from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount import Amount, AmountDict
from .enums.payout_speed import PayoutSpeedOrStr


class PayoutAccountHolderRequest(SdkBaseModel):
    account_code: str = Field(alias="accountCode")
    """The code of the account from which the payout is to be made."""

    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder who owns the account from which the payout is to be made. The Account Holder is
    the party to which the payout will be made."""

    amount: Optional[Amount] = UNSET
    """An object containing the currency and value of the payout. If the account has multiple currencies, specify the
    currency to be used. If the ``bankAccountUUID`` is provided in the request, the currency supported by the bank is
    used. If the ``payoutMethodCode`` is provided in the request, the specified payout method is selected."""

    bank_account_uuid: Optional[str] = Field(default=UNSET, alias="bankAccountUUID")
    """The unique ID of the Bank Account held by the Account Holder to which the payout is to be made. If left blank, a
    bank account is automatically selected."""

    description: Optional[str] = UNSET
    """A description of the payout. Maximum 200 characters. Allowed:
    **abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/?:().,'+ ";**"""

    merchant_reference: Optional[str] = Field(default=UNSET, alias="merchantReference")
    """A value that can be supplied at the discretion of the executing user in order to link multiple transactions to
    one another."""

    payout_method_code: Optional[str] = Field(default=UNSET, alias="payoutMethodCode")
    """The unique ID of the payout method held by the Account Holder to which the payout is to be made. If left blank, a
    payout instrument is automatically selected."""

    payout_speed: Optional[PayoutSpeedOrStr] = Field(default=UNSET, alias="payoutSpeed")
    """Speed with which payouts for this account are processed. Permitted values: ``STANDARD``, ``SAME_DAY``."""


class PayoutAccountHolderRequestDict(TypedDict):
    account_code: str
    account_holder_code: str
    amount: NotRequired[Amount | AmountDict]
    bank_account_uuid: NotRequired[str]
    description: NotRequired[str]
    merchant_reference: NotRequired[str]
    payout_method_code: NotRequired[str]
    payout_speed: NotRequired[PayoutSpeedOrStr]
