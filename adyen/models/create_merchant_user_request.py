from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .name import Name, NameDict


class CreateMerchantUserRequest(SdkBaseModel):
    account_groups: Optional[list[str]] = Field(default=UNSET, alias="accountGroups")
    """The list of `account groups <https://docs.adyen.com/account/account-structure#account-groups>`__ associated with
    this user."""

    email: str
    """The email address of the user."""

    login_method: Optional[str] = Field(default=UNSET, alias="loginMethod")
    """The requested login method for the user. To use SSO, you must already have SSO configured with Adyen before
    creating the user.

    Possible values: **Email** or **SSO**"""

    name: Name
    """The user's full name.

    Allowed length: 1—80 characters."""

    roles: Optional[list[str]] = UNSET
    """The list of `roles <https://docs.adyen.com/account/user-roles>`__ for this user."""

    time_zone_code: Optional[str] = Field(default=UNSET, alias="timeZoneCode")
    """The `tz database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__ of the time zone of the
    user. For example, **Europe/Amsterdam**."""

    username: str
    """The user's email address that will be their username. Must be the same as the one in the ``email`` field."""


class CreateMerchantUserRequestDict(TypedDict):
    account_groups: NotRequired[list[str]]
    email: str
    login_method: NotRequired[str]
    name: Name | NameDict
    roles: NotRequired[list[str]]
    time_zone_code: NotRequired[str]
    username: str
