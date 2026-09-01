from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_details1 import AccountHolderDetails1, AccountHolderDetails1Dict
from .enums.legal_entity import LegalEntityOrStr


class CreateAccountHolderRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """Your unique identifier for the prospective account holder. The length must be between three (3) and fifty (50)
    characters long. Only letters, digits, and hyphens (-) are allowed."""

    account_holder_details: AccountHolderDetails1 = Field(alias="accountHolderDetails")
    """The details of the prospective account holder."""

    create_default_account: Optional[bool] = Field(default=UNSET, alias="createDefaultAccount")
    """If set to **true**, an account with the default options is automatically created for the account holder. By
    default, this field is set to **true**."""

    description: Optional[str] = UNSET
    """A description of the prospective account holder, maximum 256 characters. You can use alphanumeric characters
    (A-Z, a-z, 0-9), white spaces, and underscores ``_``."""

    legal_entity: LegalEntityOrStr = Field(alias="legalEntity")
    """The legal entity type of the account holder. This determines the information that should be provided in the
    request.

    Possible values: **Business**, **Individual**, or **NonProfit**.

    * If set to **Business** or **NonProfit**, then ``accountHolderDetails.businessDetails`` must be provided, with at
        least one entry in the ``accountHolderDetails.businessDetails.shareholders`` list.

    * If set to **Individual**, then ``accountHolderDetails.individualDetails`` must be provided."""

    primary_currency: Optional[str] = Field(default=UNSET, alias="primaryCurrency")
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__, with
    which the prospective account holder primarily deals."""

    processing_tier: Optional[int] = Field(default=UNSET, alias="processingTier")
    """The starting `processing tier
    <https://docs.adyen.com/classic-platforms/onboarding-and-verification/precheck-kyc-information>`__ for the
    prospective account holder."""

    verification_profile: Optional[str] = Field(default=UNSET, alias="verificationProfile")
    """The identifier of the profile that applies to this entity."""


class CreateAccountHolderRequestDict(TypedDict):
    account_holder_code: str
    account_holder_details: AccountHolderDetails1 | AccountHolderDetails1Dict
    create_default_account: NotRequired[bool]
    description: NotRequired[str]
    legal_entity: LegalEntityOrStr
    primary_currency: NotRequired[str]
    processing_tier: NotRequired[int]
    verification_profile: NotRequired[str]
