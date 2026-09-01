from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .links1 import Links1, Links1Dict
from .name import Name, NameDict


class CreateUserResponse(SdkBaseModel):
    links: Optional[Links1] = Field(default=UNSET, alias="_links")
    """References to resources connected with this user."""

    account_groups: Optional[list[str]] = Field(default=UNSET, alias="accountGroups")
    """The list of `account groups <https://docs.adyen.com/account/account-structure#account-groups>`__ associated with
    this user."""

    active: Optional[bool] = UNSET
    """Indicates whether this user is active."""

    apps: Optional[list[str]] = UNSET
    """Set of apps available to this user"""

    email: str
    """The email address of the user."""

    id: str
    """The unique identifier of the user."""

    name: Optional[Name] = UNSET
    """The user's full name."""

    roles: list[str]
    """The list of `roles <https://docs.adyen.com/account/user-roles>`__ for this user."""

    time_zone_code: str = Field(alias="timeZoneCode")
    """The `tz database name <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`__ of the time zone of the
    user. For example, **Europe/Amsterdam**."""

    username: str
    """The username for this user."""


class CreateUserResponseDict(TypedDict):
    links: NotRequired[Links1 | Links1Dict]
    account_groups: NotRequired[list[str]]
    active: NotRequired[bool]
    apps: NotRequired[list[str]]
    email: str
    id: str
    name: NotRequired[Name | NameDict]
    roles: list[str]
    time_zone_code: str
    username: str
