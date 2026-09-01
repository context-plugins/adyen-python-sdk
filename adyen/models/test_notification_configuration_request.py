from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event_type1 import EventType1OrStr


class TestNotificationConfigurationRequest(SdkBaseModel):
    event_types: Optional[list[EventType1OrStr]] = Field(default=UNSET, alias="eventTypes")
    """The event types to test. If left blank, then all of the configured event types will be tested. >Permitted values:
    ``ACCOUNT_HOLDER_CREATED``, ``ACCOUNT_CREATED``, ``ACCOUNT_UPDATED``, ``ACCOUNT_HOLDER_UPDATED``,
    ``ACCOUNT_HOLDER_STATUS_CHANGE``, ``ACCOUNT_HOLDER_STORE_STATUS_CHANGE`` ``ACCOUNT_HOLDER_VERIFICATION``,
    ``ACCOUNT_HOLDER_LIMIT_REACHED``, ``ACCOUNT_HOLDER_PAYOUT``, ``PAYMENT_FAILURE``, ``SCHEDULED_REFUNDS``,
    ``REPORT_AVAILABLE``, ``TRANSFER_FUNDS``, ``BENEFICIARY_SETUP``, ``COMPENSATE_NEGATIVE_BALANCE``."""

    notification_id: int = Field(alias="notificationId")
    """The ID of the notification subscription configuration to be tested."""


class TestNotificationConfigurationRequestDict(TypedDict):
    event_types: NotRequired[list[EventType1OrStr]]
    notification_id: int
