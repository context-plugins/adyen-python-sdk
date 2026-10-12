from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .party_identification3 import PartyIdentification3, PartyIdentification3Dict
from .unions.account_identification2 import AccountIdentification2, AccountIdentification2Dict


class BankAccountV31(SdkBaseModel):
    """Contains information about the counterparty bank account."""

    account_holder: PartyIdentification3 = Field(alias="accountHolder")
    """Information about the owner of the bank account."""

    account_identification: AccountIdentification2 = Field(alias="accountIdentification")
    """Contains the bank account details. The fields required in this object depend on the country of the bank account
    and the currency of the transfer."""

    stored_payment_method_id: Optional[str] = Field(default=UNSET, alias="storedPaymentMethodId")
    """The unique token that identifies the stored bank account details of the counterparty for a payout."""


class BankAccountV31Dict(TypedDict):
    account_holder: PartyIdentification3Dict
    account_identification: AccountIdentification2Dict
    stored_payment_method_id: NotRequired[str]
