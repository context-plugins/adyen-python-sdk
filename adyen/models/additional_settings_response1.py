from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AdditionalSettingsResponse1(SdkBaseModel):
    """Additional shopper and transaction information to be included in your `standard webhooks
    <https://docs.adyen.com/development-resources/webhooks/webhook-types/#event-codes>`__. Find out more about the
    available `additional settings <https://docs.adyen.com/development-resources/webhooks/additional-settings>`__."""

    exclude_event_codes: Optional[list[str]] = Field(default=UNSET, alias="excludeEventCodes")
    """Object containing list of event codes for which the notification will not be sent."""

    include_event_codes: Optional[list[str]] = Field(default=UNSET, alias="includeEventCodes")
    """Object containing list of event codes for which the notification will be sent."""

    properties: Optional[dict[str, bool]] = UNSET
    """Object containing boolean key-value pairs. The key can be any `standard webhook additional setting
    <https://docs.adyen.com/development-resources/webhooks/additional-settings>`__, and the value indicates if the
    setting is enabled. For example, ``includeCaptureDelayHours``: **true** means the standard notifications you get
    will contain the number of hours remaining until the payment will be captured."""


class AdditionalSettingsResponse1Dict(TypedDict):
    exclude_event_codes: NotRequired[list[str]]
    include_event_codes: NotRequired[list[str]]
    properties: NotRequired[dict[str, bool]]
