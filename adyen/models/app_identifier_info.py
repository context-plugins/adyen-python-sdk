from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AppIdentifierInfo(SdkBaseModel):
    android_package_id: Optional[str] = Field(default=UNSET, alias="androidPackageId")
    """The Android package identifier for this app."""

    ios_scheme: Optional[str] = Field(default=UNSET, alias="iosScheme")
    """The iOS URL scheme for this app."""


class AppIdentifierInfoDict(TypedDict):
    android_package_id: NotRequired[str]
    ios_scheme: NotRequired[str]
