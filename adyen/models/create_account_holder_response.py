from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_details2 import AccountHolderDetails2, AccountHolderDetails2Dict
from .account_holder_status2 import AccountHolderStatus2, AccountHolderStatus2Dict
from .enums.legal_entity1 import LegalEntity1OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .kycverification_result1 import KycverificationResult1, KycverificationResult1Dict


class CreateAccountHolderResponse(SdkBaseModel):
    account_code: Optional[str] = Field(default=UNSET, alias="accountCode")
    """The code of a new account created for the account holder."""

    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the new account holder."""

    account_holder_details: Optional[AccountHolderDetails2] = Field(default=UNSET, alias="accountHolderDetails")
    """Details of the new account holder."""

    account_holder_status: Optional[AccountHolderStatus2] = Field(default=UNSET, alias="accountHolderStatus")
    """The status of the new account holder."""

    description: Optional[str] = UNSET
    """The description of the new account holder."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """A list of fields that caused the ``/createAccountHolder`` request to fail."""

    legal_entity: Optional[LegalEntity1OrStr] = Field(default=UNSET, alias="legalEntity")
    """The type of legal entity of the new account holder."""

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


class CreateAccountHolderResponseDict(TypedDict):
    account_code: NotRequired[str]
    account_holder_code: NotRequired[str]
    account_holder_details: NotRequired[AccountHolderDetails2Dict]
    account_holder_status: NotRequired[AccountHolderStatus2Dict]
    description: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    legal_entity: NotRequired[LegalEntity1OrStr]
    primary_currency: NotRequired[str]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
    verification: NotRequired[KycverificationResult1Dict]
    verification_profile: NotRequired[str]
