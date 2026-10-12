from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..balance_webhook_setting import BalanceWebhookSetting, BalanceWebhookSettingDict

WebhookSetting: TypeAlias = Annotated[Annotated[BalanceWebhookSetting, Tag("balance")], WireDiscriminator("type")]

WebhookSettingDict: TypeAlias = BalanceWebhookSettingDict
