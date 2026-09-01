from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Localization1(SdkBaseModel):
    """Settings for localization."""

    language: Optional[str] = UNSET
    """Language of the terminal."""

    secondary_language: Optional[str] = Field(default=UNSET, alias="secondaryLanguage")
    """Secondary language of the terminal."""

    timezone: Optional[str] = UNSET
    """The time zone of the terminal."""


class Localization1Dict(TypedDict):
    language: NotRequired[str]
    secondary_language: NotRequired[str]
    timezone: NotRequired[str]
