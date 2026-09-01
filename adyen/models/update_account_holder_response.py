from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_details3 import AccountHolderDetails3, AccountHolderDetails3Dict
from .account_holder_status7 import AccountHolderStatus7, AccountHolderStatus7Dict
from .enums.legal_entity2 import LegalEntity2OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .kycverification_result1 import KycverificationResult1, KycverificationResult1Dict


class UpdateAccountHolderResponse(SdkBaseModel):
    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the account holder."""

    account_holder_details: Optional[AccountHolderDetails3] = Field(default=UNSET, alias="accountHolderDetails")
    """Details of the account holder."""

    account_holder_status: Optional[AccountHolderStatus7] = Field(default=UNSET, alias="accountHolderStatus")
    """The new status of the account holder."""

    description: Optional[str] = UNSET
    """The description of the account holder."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """in case the account holder has not been updated, contains account holder fields, that did not pass the
    validation."""

    legal_entity: Optional[LegalEntity2OrStr] = Field(default=UNSET, alias="legalEntity")
    """The legal entity of the account holder."""

    primary_currency: Optional[str] = Field(default=UNSET, alias="primaryCurrency")
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__, with
    which the prospective account holder primarily deals."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""

    verification: Optional[KycverificationResult1] = UNSET
    """The details of KYC Verification of the account holder."""

    verification_profile: Optional[str] = Field(default=UNSET, alias="verificationProfile")
    """The identifier of the profile that applies to this entity."""


class UpdateAccountHolderResponseDict(TypedDict):
    account_holder_code: NotRequired[str]
    account_holder_details: NotRequired[AccountHolderDetails3 | AccountHolderDetails3Dict]
    account_holder_status: NotRequired[AccountHolderStatus7 | AccountHolderStatus7Dict]
    description: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    legal_entity: NotRequired[LegalEntity2OrStr]
    primary_currency: NotRequired[str]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
    verification: NotRequired[KycverificationResult1 | KycverificationResult1Dict]
    verification_profile: NotRequired[str]
