from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AppIdentifierInfo1(SdkBaseModel):
    """The app identifier information containing iOS scheme and Android package ID."""

    android_package_id: Optional[str] = Field(default=UNSET, alias="androidPackageId")
    """The Android package identifier for this app."""

    ios_scheme: Optional[str] = Field(default=UNSET, alias="iosScheme")
    """The iOS URL scheme for this app."""


class AppIdentifierInfo1Dict(TypedDict):
    android_package_id: NotRequired[str]
    ios_scheme: NotRequired[str]
