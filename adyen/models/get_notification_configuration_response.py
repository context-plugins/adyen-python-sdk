from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error_field_type import ErrorFieldType, ErrorFieldTypeDict
from .notification_configuration_details2 import (
    NotificationConfigurationDetails2,
    NotificationConfigurationDetails2Dict,
)


class GetNotificationConfigurationResponse(SdkBaseModel):
    configuration_details: NotificationConfigurationDetails2 = Field(alias="configurationDetails")
    """Details of the notification subscription configuration."""

    invalid_fields: Optional[list[ErrorFieldType]] = Field(default=UNSET, alias="invalidFields")
    """Contains field validation errors that would prevent requests from being processed."""

    psp_reference: Optional[str] = Field(default=UNSET, alias="pspReference")
    """The reference of a request. Can be used to uniquely identify the request."""

    result_code: Optional[str] = Field(default=UNSET, alias="resultCode")
    """The result code."""


class GetNotificationConfigurationResponseDict(TypedDict):
    configuration_details: NotificationConfigurationDetails2Dict
    invalid_fields: NotRequired[list[ErrorFieldTypeDict]]
    psp_reference: NotRequired[str]
    result_code: NotRequired[str]
