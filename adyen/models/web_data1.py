from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WebData1(SdkBaseModel):
    """The website and app URL of the legal entity."""

    web_address: Optional[str] = Field(default=UNSET, alias="webAddress")
    """The URL of the website or the app store URL."""

    web_address_id: Optional[str] = Field(default=UNSET, alias="webAddressId")
    """The unique identifier of the web address."""


class WebData1Dict(TypedDict):
    web_address: NotRequired[str]
    web_address_id: NotRequired[str]
