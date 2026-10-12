from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .additional_bank_identification1 import AdditionalBankIdentification1, AdditionalBankIdentification1Dict


class NumberAndBicAccountIdentification(SdkBaseModel):
    account_number: str = Field(alias="accountNumber")
    """The bank account number, without separators or whitespace. The length and format depends on the bank or
    country."""

    additional_bank_identification: Optional[AdditionalBankIdentification1] = Field(
        default=UNSET, alias="additionalBankIdentification"
    )
    """Additional identification codes of the bank. Some banks may require these identifiers for cross-border
    transfers."""

    bic: str
    """The bank's 8- or 11-character BIC or SWIFT code."""

    type_: Literal["numberAndBic"] = Field(default="numberAndBic", alias="type")
    """**numberAndBic**"""


class NumberAndBicAccountIdentificationDict(TypedDict):
    account_number: str
    additional_bank_identification: NotRequired[AdditionalBankIdentification1Dict]
    bic: str
    type_: Literal["numberAndBic"]
