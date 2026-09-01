from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalSettings(SdkBaseModel):
    include_event_codes: Optional[list[str]] = Field(default=UNSET, alias="includeEventCodes")
    """Object containing list of event codes for which the notification will be sent."""

    properties: Optional[dict[str, bool]] = UNSET
    """Object containing boolean key-value pairs. The key can be any `standard webhook additional setting
    <https://docs.adyen.com/development-resources/webhooks/additional-settings>`__, and the value indicates if the
    setting is enabled. For example, ``includeCaptureDelayHours``: **true** means the standard notifications you get
    will contain the number of hours remaining until the payment will be captured."""


class AdditionalSettingsDict(TypedDict):
    include_event_codes: NotRequired[list[str]]
    properties: NotRequired[dict[str, bool]]
