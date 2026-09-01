from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class OnboardingTheme(SdkBaseModel):
    created_at: RFC3339DateTime = Field(alias="createdAt")
    """The creation date of the theme."""

    description: Optional[str] = UNSET
    """The description of the theme."""

    id: str
    """The unique identifier of the theme."""

    properties: dict[str, str]
    """The properties of the theme."""

    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    """The date when the theme was last updated."""


class OnboardingThemeDict(TypedDict):
    created_at: RFC3339DateTime
    description: NotRequired[str]
    id: str
    properties: dict[str, str]
    updated_at: NotRequired[RFC3339DateTime]
