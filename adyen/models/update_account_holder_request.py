from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_details4 import AccountHolderDetails4, AccountHolderDetails4Dict
from .enums.legal_entity import LegalEntityOrStr


class UpdateAccountHolderRequest(SdkBaseModel):
    account_holder_code: str = Field(alias="accountHolderCode")
    """The code of the Account Holder to be updated."""

    account_holder_details: Optional[AccountHolderDetails4] = Field(default=UNSET, alias="accountHolderDetails")
    """The details to which the Account Holder should be updated.

    Required if a processingTier is not provided."""

    description: Optional[str] = UNSET
    """A description of the account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9),
    white spaces, and underscores ``_``."""

    legal_entity: Optional[LegalEntityOrStr] = Field(default=UNSET, alias="legalEntity")
    """The legal entity type of the account holder. This determines the information that should be provided in the
    request.

    Possible values: **Business**, **Individual**, or **NonProfit**.

    * If set to **Business** or **NonProfit**, then ``accountHolderDetails.businessDetails`` must be provided, with at
        least one entry in the ``accountHolderDetails.businessDetails.shareholders`` list.

    * If set to **Individual**, then ``accountHolderDetails.individualDetails`` must be provided."""

    primary_currency: Optional[str] = Field(default=UNSET, alias="primaryCurrency")
    """The primary three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__,
    to which the account holder should be updated."""

    processing_tier: Optional[int] = Field(default=UNSET, alias="processingTier")
    """The processing tier to which the Account Holder should be updated. >The processing tier can not be lowered
    through this request.

    >Required if accountHolderDetails are not provided."""

    verification_profile: Optional[str] = Field(default=UNSET, alias="verificationProfile")
    """The identifier of the profile that applies to this entity."""


class UpdateAccountHolderRequestDict(TypedDict):
    account_holder_code: str
    account_holder_details: NotRequired[AccountHolderDetails4 | AccountHolderDetails4Dict]
    description: NotRequired[str]
    legal_entity: NotRequired[LegalEntityOrStr]
    primary_currency: NotRequired[str]
    processing_tier: NotRequired[int]
    verification_profile: NotRequired[str]
