from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.account_verification_country1 import AccountVerificationCountry1OrStr
from .verified_account import VerifiedAccount, VerifiedAccountDict


class AccountVerificationReportResponse(SdkBaseModel):
    accounts: list[VerifiedAccount]
    """A list of bank accounts with their respective information."""

    country: AccountVerificationCountry1OrStr
    """The location where the third-party individual's bank account is registered."""

    id: str
    """The unique identifier for the specific report."""


class AccountVerificationReportResponseDict(TypedDict):
    accounts: list[VerifiedAccount | VerifiedAccountDict]
    country: AccountVerificationCountry1OrStr
    id: str
