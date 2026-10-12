from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .condition import Condition, ConditionDict
from .enums.status6 import Status6OrStr
from .target1 import Target1, Target1Dict


class BalanceWebhookSettingInfo(SdkBaseModel):
    conditions: Optional[list[Condition]] = UNSET
    """The array of conditions a balance change must meet for Adyen to send the webhook."""

    currency: str
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__ of the
    balance."""

    status: Status6OrStr
    """The status of the webhook setting. Possible values:

    * **active**: You receive a balance webhook if any of the conditions in this setting are met.
    * **inactive**: You do not receive a balance webhook even if the conditions in this settings are met."""

    target: Target1
    """The type and ID of the resource about whose balance changes you want to be notified."""

    type_: Literal["balance"] = Field(default="balance", alias="type")
    """The type of the webhook you are configuring. Set to **balance**."""


class BalanceWebhookSettingInfoDict(TypedDict):
    conditions: NotRequired[list[ConditionDict]]
    currency: str
    status: Status6OrStr
    target: Target1Dict
    type_: Literal["balance"]
