from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DeleteNotificationConfigurationRequest(SdkBaseModel):
    notification_ids: list[int] = Field(alias="notificationIds")
    """A list of IDs of the notification subscription configurations to be deleted."""


class DeleteNotificationConfigurationRequestDict(TypedDict):
    notification_ids: list[int]
