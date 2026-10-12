from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .account_holder_capability import AccountHolderCapability, AccountHolderCapabilityDict
from .contact_details1 import ContactDetails1, ContactDetails1Dict


class AccountHolderInfo(SdkBaseModel):
    balance_platform: Optional[str] = Field(default=UNSET, alias="balancePlatform")
    """The unique identifier of the `balance platform
    <https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id>`__ to which
    the account holder belongs. Required in the request if your API credentials can be used for multiple balance
    platforms."""

    capabilities: Optional[dict[str, AccountHolderCapability]] = UNSET
    """Contains key-value pairs that specify the actions that an account holder can do in your platform. The key is a
    capability required for your integration. For example, **issueCard** for Issuing. The value is an object containing
    the settings for the capability."""

    contact_details: Optional[ContactDetails1] = Field(default=UNSET, alias="contactDetails")
    """Contact details of the account holder."""

    description: Optional[str] = UNSET
    """Your description for the account holder."""

    legal_entity_id: str = Field(alias="legalEntityId")
    """The unique identifier of the `legal entity
    <https://docs.adyen.com/api-explorer/legalentity/latest/post/legalEntities#responses-200-id>`__ associated with the
    account holder. Adyen performs a verification process against the legal entity of the account holder."""

    metadata: Optional[dict[str, str]] = UNSET
    """A set of key and value pairs for general use. The keys do not have specific names and may be used for storing
    miscellaneous data as desired.
    > Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of
        those key-value pairs."""

    migrated_account_holder_code: Optional[str] = Field(default=UNSET, alias="migratedAccountHolderCode")
    """The unique identifier of the migrated account holder in the classic integration."""

    reference: Optional[str] = UNSET
    """Your reference for the account holder."""

    time_zone: Optional[str] = Field(default=UNSET, alias="timeZone")
    """The time zone of the account holder. For example, **Europe/Amsterdam**. Defaults to the time zone of the balance
    platform if no time zone is set. For possible values, see the `list of time zone codes
    <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__."""


class AccountHolderInfoDict(TypedDict):
    balance_platform: NotRequired[str]
    capabilities: NotRequired[dict[str, AccountHolderCapabilityDict]]
    contact_details: NotRequired[ContactDetails1Dict]
    description: NotRequired[str]
    legal_entity_id: str
    metadata: NotRequired[dict[str, str]]
    migrated_account_holder_code: NotRequired[str]
    reference: NotRequired[str]
    time_zone: NotRequired[str]
