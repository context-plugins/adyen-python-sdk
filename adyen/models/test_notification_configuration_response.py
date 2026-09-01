from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.event_type1 import EventType1OrStr
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .exchange_message import ExchangeMessage, ExchangeMessageDict


class TestNotificationConfigurationResponse(SdkBaseModel):
    error_messages: Optional[list[str]] = Field(default=UNSET, alias="errorMessages")
    """Any error messages encountered."""

    event_types: Optional[list[EventType1OrStr]] = Field(default=UNSET, alias="eventTypes")
    """The event types that were tested. >Permitted values: ``ACCOUNT_HOLDER_CREATED``, ``ACCOUNT_CREATED``,
    ``ACCOUNT_UPDATED``, ``ACCOUNT_HOLDER_UPDATED``, ``ACCOUNT_HOLDER_STATUS_CHANGE``,
    ``ACCOUNT_HOLDER_STORE_STATUS_CHANGE`` ``ACCOUNT_HOLDER_VERIFICATION``, ``ACCOUNT_HOLDER_LIMIT_REACHED``,
    ``ACCOUNT_HOLDER_PAYOUT``, ``PAYMENT_FAILURE``, ``SCHEDULED_REFUNDS``, ``REPORT_AVAILABLE``, ``TRANSFER_FUNDS``,
    ``BENEFICIARY_SETUP``, ``COMPENSATE_NEGATIVE_BALANCE``."""

    exchange_messages: Optional[list[ExchangeMessage]] = Field(default=UNSET, alias="exchangeMessages")
    """The notification message and related response messages."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    notification_id: int = Field(alias="notificationId")
    """The ID of the notification subscription configuration."""

    ok_messages: Optional[list[str]] = Field(default=UNSET, alias="okMessages")
    """A list of messages describing the testing steps."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class TestNotificationConfigurationResponseDict(TypedDict):
    error_messages: NotRequired[list[str]]
    event_types: NotRequired[list[EventType1OrStr]]
    exchange_messages: NotRequired[list[ExchangeMessage | ExchangeMessageDict]]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    notification_id: int
    ok_messages: NotRequired[list[str]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
