from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.account_identification11 import AccountIdentification11, AccountIdentification11Dict


class BankAccountIdentificationValidationRequest(SdkBaseModel):
    account_identification: AccountIdentification11 = Field(alias="accountIdentification")
    """Bank account identification."""


class BankAccountIdentificationValidationRequestDict(TypedDict):
    account_identification: AccountIdentification11Dict
