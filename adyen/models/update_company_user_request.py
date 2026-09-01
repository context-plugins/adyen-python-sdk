from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name22 import Name22, Name22Dict


class UpdateCompanyUserRequest(SdkBaseModel):
    account_groups: Optional[list[str]] = Field(default=UNSET, alias="accountGroups")
    """The list of `account groups <https://docs.adyen.com/account/account-structure#account-groups>`__ associated with
    this user."""

    active: Optional[bool] = UNSET
    """Indicates whether this user is active."""

    associated_merchant_accounts: Optional[list[str]] = Field(default=UNSET, alias="associatedMerchantAccounts")
    """The list of `merchant accounts <https://docs.adyen.com/account/account-structure#merchant-accounts>`__ to
    associate the user with."""

    email: Optional[str] = UNSET
    """The email address of the user."""

    login_method: Optional[str] = Field(default=UNSET, alias="loginMethod")
    """The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before
    creating the user.

    Possible values: **Email** or **SSO**"""

    name: Optional[Name22] = UNSET
    """The user's full name."""

    roles: Optional[list[str]] = UNSET
    """The list of `roles <https://docs.adyen.com/account/user-roles>`__ for this user."""

    time_zone_code: Optional[str] = Field(default=UNSET, alias="timeZoneCode")
    """The `tz database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__ of the time zone of the
    user. For example, **Europe/Amsterdam**."""


class UpdateCompanyUserRequestDict(TypedDict):
    account_groups: NotRequired[list[str]]
    active: NotRequired[bool]
    associated_merchant_accounts: NotRequired[list[str]]
    email: NotRequired[str]
    login_method: NotRequired[str]
    name: NotRequired[Name22 | Name22Dict]
    roles: NotRequired[list[str]]
    time_zone_code: NotRequired[str]
