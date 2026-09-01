from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .account_identification1 import AccountIdentification1, AccountIdentification1Dict


class BankAccountIdentificationValidationRequest(SdkBaseModel):
    account_identification: AccountIdentification1 = Field(alias="accountIdentification")
    """Bank account identification."""


class BankAccountIdentificationValidationRequestDict(TypedDict):
    account_identification: AccountIdentification1 | AccountIdentification1Dict
