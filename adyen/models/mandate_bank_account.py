from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .mandate_account_identification2 import MandateAccountIdentification2, MandateAccountIdentification2Dict
from .mandate_party_identification2 import MandatePartyIdentification2, MandatePartyIdentification2Dict


class MandateBankAccount(SdkBaseModel):
    account_holder: MandatePartyIdentification2 = Field(alias="accountHolder")
    """Contains information about the owner of the counterparty bank account."""

    account_identification: MandateAccountIdentification2 = Field(alias="accountIdentification")
    """Contains the bank account details of the counterparty. The fields required in this object depend on the country
    of the bank account and the currency of the transfer."""


class MandateBankAccountDict(TypedDict):
    account_holder: MandatePartyIdentification2Dict
    account_identification: MandateAccountIdentification2Dict
