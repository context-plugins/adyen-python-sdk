from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .notification_configuration_details3 import (
    NotificationConfigurationDetails3,
    NotificationConfigurationDetails3Dict,
)


class UpdateNotificationConfigurationRequest(SdkBaseModel):
    configuration_details: NotificationConfigurationDetails3 = Field(alias="configurationDetails")
    """Details of the notification subscription configuration to be updated."""


class UpdateNotificationConfigurationRequestDict(TypedDict):
    configuration_details: NotificationConfigurationDetails3Dict
