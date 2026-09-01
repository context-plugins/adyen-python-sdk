from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.webhook_setting import WebhookSetting, WebhookSettingDict


class WebhookSettings(SdkBaseModel):
    webhook_settings: Optional[list[WebhookSetting]] = Field(default=UNSET, alias="webhookSettings")
    """The list of webhook settings."""


class WebhookSettingsDict(TypedDict):
    webhook_settings: NotRequired[list[WebhookSetting | WebhookSettingDict]]
