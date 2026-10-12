from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_bank_identification11 import AdditionalBankIdentification11, AdditionalBankIdentification11Dict


class NumberAndBicAccountIdentification1(SdkBaseModel):
    """All Of BankAccountIdentification, NumberAndBicAccountIdentification1."""

    type_: str = Field(default="numberAndBic", alias="type")
    """**numberAndBic**"""

    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace. The length and format depends on the bank or
    country."""

    additional_bank_identification: Optional[AdditionalBankIdentification11] = Field(
        default=UNSET, alias="additionalBankIdentification"
    )
    """Additional identification codes of the bank. Some banks may require these identifiers for cross-border
    transfers."""

    bic: str
    """The bank's 8- or 11-character BIC or SWIFT code."""


class NumberAndBicAccountIdentification1Dict(TypedDict):
    type_: str
    account_number: str
    additional_bank_identification: NotRequired[AdditionalBankIdentification11Dict]
    bic: str
