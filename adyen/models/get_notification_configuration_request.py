from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GetNotificationConfigurationRequest(SdkBaseModel):
    notification_id: int = Field(alias="notificationId")
    """The ID of the notification subscription configuration whose details are to be retrieved."""


class GetNotificationConfigurationRequestDict(TypedDict):
    notification_id: int
