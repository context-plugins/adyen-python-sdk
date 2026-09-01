from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .account import Account, AccountDict
from .account_holder_details3 import AccountHolderDetails3, AccountHolderDetails3Dict
from .account_holder_status3 import AccountHolderStatus3, AccountHolderStatus3Dict
from .enums.legal_entity2 import LegalEntity2OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .kycverification_result1 import KycverificationResult1, KycverificationResult1Dict
from .migration_data2 import MigrationData2, MigrationData2Dict


class GetAccountHolderResponse(SdkBaseModel):
    account_holder_code: Optional[str] = Field(default=UNSET, alias="accountHolderCode")
    """The code of the account holder."""

    account_holder_details: Optional[AccountHolderDetails3] = Field(default=UNSET, alias="accountHolderDetails")
    """Details of the account holder."""

    account_holder_status: Optional[AccountHolderStatus3] = Field(default=UNSET, alias="accountHolderStatus")
    """The status of the account holder."""

    accounts: Optional[list[Account]] = UNSET
    """A list of the accounts under the account holder."""

    description: Optional[str] = UNSET
    """The description of the account holder."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    legal_entity: Optional[LegalEntity2OrStr] = Field(default=UNSET, alias="legalEntity")
    """The legal entity of the account holder."""

    migration_data: Optional[MigrationData2] = Field(default=UNSET, alias="migrationData")
    """Details of the account holder migrated to the balance platform."""

    primary_currency: Optional[str] = Field(default=UNSET, alias="primaryCurrency")
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__, with
    which the prospective account holder primarily deals."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""

    system_up_to_date_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="systemUpToDateTime")
    """The time that shows how up to date is the information in the response."""

    verification: Optional[KycverificationResult1] = UNSET
    """The details of KYC Verification of the account holder."""

    verification_profile: Optional[str] = Field(default=UNSET, alias="verificationProfile")
    """The identifier of the profile that applies to this entity."""


class GetAccountHolderResponseDict(TypedDict):
    account_holder_code: NotRequired[str]
    account_holder_details: NotRequired[AccountHolderDetails3 | AccountHolderDetails3Dict]
    account_holder_status: NotRequired[AccountHolderStatus3 | AccountHolderStatus3Dict]
    accounts: NotRequired[list[Account | AccountDict]]
    description: NotRequired[str]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    legal_entity: NotRequired[LegalEntity2OrStr]
    migration_data: NotRequired[MigrationData2 | MigrationData2Dict]
    primary_currency: NotRequired[str]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
    system_up_to_date_time: NotRequired[RFC3339DateTime]
    verification: NotRequired[KycverificationResult1 | KycverificationResult1Dict]
    verification_profile: NotRequired[str]
