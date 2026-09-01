from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Provider(SdkBaseModel):
    logo_url: str = Field(alias="logoURL")
    """The URL of the organization's or brand's logo. This URL typically points to an image file (e.g., .png, .jpg,
    .svg) that can be displayed to visually represent the entity."""

    name: str
    """The official or commonly used name of the organization, brand, or entity."""


class ProviderDict(TypedDict):
    logo_url: str
    name: str
