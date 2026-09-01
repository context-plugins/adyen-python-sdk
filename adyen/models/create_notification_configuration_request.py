from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .notification_configuration_details4 import (
    NotificationConfigurationDetails4,
    NotificationConfigurationDetails4Dict,
)


class CreateNotificationConfigurationRequest(SdkBaseModel):
    configuration_details: NotificationConfigurationDetails4 = Field(alias="configurationDetails")
    """Details of the prospective notification subscription configuration."""


class CreateNotificationConfigurationRequestDict(TypedDict):
    configuration_details: NotificationConfigurationDetails4 | NotificationConfigurationDetails4Dict
