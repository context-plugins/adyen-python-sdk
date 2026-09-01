from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BrowserInfo(SdkBaseModel):
    """The shopper's browser information.
    > For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the
        ``userAgent`` and ``acceptHeader`` fields to indicate that your integration can support a redirect in case a
        payment is routed to 3D Secure 2 redirect."""

    accept_header: str = Field(alias="acceptHeader")
    """The accept header value of the shopper's browser."""

    color_depth: int = Field(alias="colorDepth")
    """The color depth of the shopper's browser in bits per pixel. This should be obtained by using the browser's
    ``screen.colorDepth`` property. Accepted values: 1, 4, 8, 15, 16, 24, 30, 32 or 48 bit color depth."""

    java_enabled: bool = Field(alias="javaEnabled")
    """Boolean value indicating if the shopper's browser is able to execute Java."""

    java_script_enabled: Optional[bool] = Field(default=UNSET, alias="javaScriptEnabled")
    """Boolean value indicating if the shopper's browser is able to execute JavaScript. A default 'true' value is
    assumed if the field is not present."""

    language: str
    """The ``navigator.language`` value of the shopper's browser (as defined in IETF BCP 47)."""

    screen_height: int = Field(alias="screenHeight")
    """The total height of the shopper's device screen in pixels."""

    screen_width: int = Field(alias="screenWidth")
    """The total width of the shopper's device screen in pixels."""

    time_zone_offset: int = Field(alias="timeZoneOffset")
    """Time difference between UTC time and the shopper's browser local time, in minutes."""

    user_agent: str = Field(alias="userAgent")
    """The user agent value of the shopper's browser."""


class BrowserInfoDict(TypedDict):
    accept_header: str
    color_depth: int
    java_enabled: bool
    java_script_enabled: NotRequired[bool]
    language: str
    screen_height: int
    screen_width: int
    time_zone_offset: int
    user_agent: str
