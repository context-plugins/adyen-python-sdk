from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Provider2(SdkBaseModel):
    """Metadata about the selected provider, including the name and company logo. You can use this information to inform
    the user about the provider they will be redirected to when they select the link."""

    logo_url: str = Field(alias="logoURL")
    """The URL of the organization's or brand's logo. This URL typically points to an image file (e.g., .png, .jpg,
    .svg) that can be displayed to visually represent the entity."""

    name: str
    """The official or commonly used name of the organization, brand, or entity."""


class Provider2Dict(TypedDict):
    logo_url: str
    name: str
