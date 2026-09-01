from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Field

from ..balance_webhook_setting import BalanceWebhookSetting, BalanceWebhookSettingDict

WebhookSetting: TypeAlias = Annotated[BalanceWebhookSetting, Field(discriminator="type_")]

WebhookSettingDict: TypeAlias = BalanceWebhookSettingDict
