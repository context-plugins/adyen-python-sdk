from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.account_identification2 import AccountIdentification2, AccountIdentification2Dict


class BankAccountInfo(SdkBaseModel):
    account_identification: Optional[AccountIdentification2] = Field(default=UNSET, alias="accountIdentification")
    """Identification of the bank account."""

    account_type: Optional[str] = Field(default=UNSET, alias="accountType")
    """The type of bank account."""

    bank_name: Optional[str] = Field(default=UNSET, alias="bankName")
    """The name of the banking institution where the bank account is held."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The two-character `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ country code where
    the bank account is registered. For example, **NL**."""

    trusted_source: Optional[bool] = Field(default=UNSET, alias="trustedSource")
    """Identifies if the bank account was created through `instant bank verification
    <https://docs.adyen.com/release-notes/platforms-and-financial-products#releaseNote=2023-05-08-hosted-onboarding>`__."""


class BankAccountInfoDict(TypedDict):
    account_identification: NotRequired[AccountIdentification2 | AccountIdentification2Dict]
    account_type: NotRequired[str]
    bank_name: NotRequired[str]
    country_code: NotRequired[str]
    trusted_source: NotRequired[bool]
