from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.behavior import BehaviorOrStr


class PlatformChargebackLogic(SdkBaseModel):
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    behavior: Optional[BehaviorOrStr] = UNSET
    """The method of handling the chargeback.

    Possible values: **deductFromLiableAccount**, **deductFromOneBalanceAccount**, **deductAccordingToSplitRatio**."""

    cost_allocation_account: Optional[str] = Field(default=UNSET, alias="costAllocationAccount")
    """The unique identifier of the balance account to which the chargeback fees are booked. By default, the chargeback
    fees are booked to your liable balance account."""

    target_account: Optional[str] = Field(default=UNSET, alias="targetAccount")
    """The unique identifier of the balance account against which the disputed amount is booked.

    Required if ``behavior`` is **deductFromOneBalanceAccount**."""


class PlatformChargebackLogicDict(TypedDict):
    behavior: NotRequired[BehaviorOrStr]
    cost_allocation_account: NotRequired[str]
    target_account: NotRequired[str]
