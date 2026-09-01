from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .condition import Condition, ConditionDict
from .target3 import Target3, Target3Dict


class BalanceWebhookSetting(SdkBaseModel):
    """All Of WebhookSetting, BalanceWebhookSetting."""

    type_: Literal["balance"] = Field(default="balance", alias="type")

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__ of the
    balance."""

    id: str
    """The unique identifier of the webhook setting."""

    status: str
    """The status of the webhook setting. Possible values:

    * **active**: You receive a balance webhook if any of the conditions in this setting are met.
    * **inactive**: You do not receive a balance webhook even if the conditions in this settings are met."""

    target: Target3
    """The resource about whose balance change you want to get notified."""

    conditions: Optional[list[Condition]] = UNSET
    """The list of settings and criteria for triggering the `balance webhook
    <https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated>`__."""


class BalanceWebhookSettingDict(TypedDict):
    type_: NotRequired[Literal["balance"]]
    currency: str
    id: str
    status: str
    target: Target3 | Target3Dict
    conditions: NotRequired[list[Condition | ConditionDict]]
