from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type32 import Type32OrStr


class InstallAndroidAppDetails(SdkBaseModel):
    app_id: Optional[str] = Field(default=UNSET, alias="appId")
    """The unique identifier of the app to be installed."""

    type_: Optional[Type32OrStr] = Field(default=UNSET, alias="type")
    """Type of terminal action: Install an Android app."""


class InstallAndroidAppDetailsDict(TypedDict):
    app_id: NotRequired[str]
    type_: NotRequired[Type32OrStr]
