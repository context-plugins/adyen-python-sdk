from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.bank_account_identification_type import BankAccountIdentificationTypeOrStr


class BankAccountIdentificationTypeRequirement(SdkBaseModel):
    bank_account_identification_types: Optional[list[BankAccountIdentificationTypeOrStr]] = Field(
        default=UNSET, alias="bankAccountIdentificationTypes"
    )
    """List of bank account identification types: eg.; [iban , numberAndBic]"""

    description: Optional[str] = UNSET
    """Specifies the bank account details for a particular route per required field in this object depending on the
    country of the bank account and the currency of the transfer."""

    type_: Literal["bankAccountIdentificationTypeRequirement"] = Field(
        default="bankAccountIdentificationTypeRequirement", alias="type"
    )
    """**bankAccountIdentificationTypeRequirement**"""


class BankAccountIdentificationTypeRequirementDict(TypedDict):
    bank_account_identification_types: NotRequired[list[BankAccountIdentificationTypeOrStr]]
    description: NotRequired[str]
    type_: NotRequired[Literal["bankAccountIdentificationTypeRequirement"]]
