from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .condition import Condition, ConditionDict
from .enums.status6 import Status6OrStr
from .enums.type201 import Type201OrStr
from .target_update2 import TargetUpdate2, TargetUpdate2Dict


class BalanceWebhookSettingInfoUpdate(SdkBaseModel):
    conditions: OptionalNullable[list[Condition]] = UNSET
    """The array of conditions a balance change must meet for Adyen to send the webhook."""

    currency: Optional[str] = UNSET
    """The three-character `ISO currency code <https://docs.adyen.com/development-resources/currency-codes>`__ of the
    balance."""

    status: Optional[Status6OrStr] = UNSET
    """The status of the webhook setting. Possible values:

    * **active**: You receive a balance webhook if any of the conditions in this setting are met.
    * **inactive**: You do not receive a balance webhook even if the conditions in this settings are met."""

    target: Optional[TargetUpdate2] = UNSET
    """The type and ID of the resource about whose balance changes you want to be notified."""

    type_: Optional[Type201OrStr] = Field(default=UNSET, alias="type")
    """The type of the webhook you are configuring. Set to **balance**."""


class BalanceWebhookSettingInfoUpdateDict(TypedDict):
    conditions: NotRequired[list[ConditionDict] | None]
    currency: NotRequired[str]
    status: NotRequired[Status6OrStr]
    target: NotRequired[TargetUpdate2Dict]
    type_: NotRequired[Type201OrStr]
