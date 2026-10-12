from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.type71 import Type71, Type71OrStr


class UninstallAndroidAppDetails(SdkBaseModel):
    app_id: Optional[str] = Field(default=UNSET, alias="appId")
    """The unique identifier of the app to be uninstalled."""

    type_: Type71OrStr = Field(default=Type71.UNINSTALL_ANDROID_APP, alias="type")
    """Type of terminal action: Uninstall an Android app."""


class UninstallAndroidAppDetailsDict(TypedDict):
    app_id: NotRequired[str]
    type_: NotRequired[Type71OrStr]
