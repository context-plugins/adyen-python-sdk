from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .notification_configuration_details import NotificationConfigurationDetails, NotificationConfigurationDetailsDict


class GetNotificationConfigurationListResponse(SdkBaseModel):
    configurations: Optional[list[NotificationConfigurationDetails]] = UNSET
    """Details of the notification subscription configurations."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class GetNotificationConfigurationListResponseDict(TypedDict):
    configurations: NotRequired[list[NotificationConfigurationDetails | NotificationConfigurationDetailsDict]]
    invalid_fields: NotRequired[list[ErrorFieldType | ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
