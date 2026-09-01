from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Standalone1(SdkBaseModel):
    """Settings for `standalone
    <https://docs.adyen.com/point-of-sale/standalone/standalone-build/set-up-standalone#set-up-standalone-using-an-api-call>`__
    features."""

    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    """The default currency of the standalone payment terminal as an `ISO 4217
    <https://en.wikipedia.org/wiki/ISO_4217>`__ currency code."""

    enable_gratuities: Optional[bool] = Field(default=UNSET, alias="enableGratuities")
    """Indicates whether the tipping options specified in ``gratuities`` are enabled on the standalone terminal."""

    enable_standalone: Optional[bool] = Field(default=UNSET, alias="enableStandalone")
    """Enable standalone mode."""


class Standalone1Dict(TypedDict):
    currency_code: NotRequired[str]
    enable_gratuities: NotRequired[bool]
    enable_standalone: NotRequired[bool]
