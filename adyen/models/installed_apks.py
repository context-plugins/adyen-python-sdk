from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class InstalledApks(SdkBaseModel):
    confirmation_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="confirmationDate")
    """The date and time when the app was installed."""

    package_name: Optional[str] = Field(default=UNSET, alias="packageName")
    """The package name of the app."""

    version_name: Optional[str] = Field(default=UNSET, alias="versionName")
    """The version name of the app."""


class InstalledApksDict(TypedDict):
    confirmation_date: NotRequired[RFC3339DateTime]
    package_name: NotRequired[str]
    version_name: NotRequired[str]
