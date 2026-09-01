from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount22 import Amount22, Amount22Dict
from .amount34 import Amount34, Amount34Dict


class CalculateRateResponseItem(SdkBaseModel):
    """The response parameters returned when you calculate an amount in a different currency."""

    applied_exchange_rate: Optional[float] = Field(default=UNSET, alias="appliedExchangeRate")
    """The exchange rate to convert the source currency to the target currency. This includes Adyen's markup."""

    exchange_side: Optional[str] = Field(default=UNSET, alias="exchangeSide")
    """The operation performed on the source amount. Possible values:
    * **buy**
    * **sell**"""

    source_amount: Optional[Amount22] = Field(default=UNSET, alias="sourceAmount")
    """The currency of the amount you converted (the source amount)."""

    target_amount: Optional[Amount34] = Field(default=UNSET, alias="targetAmount")
    """An object specifying the currency and value to which you want to convert the source amount (the target
    amount)."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """The type of transaction. Possible values:
    * **splitPayment**: for payments
    * **splitRefund**: for refunds"""


class CalculateRateResponseItemDict(TypedDict):
    applied_exchange_rate: NotRequired[float]
    exchange_side: NotRequired[str]
    source_amount: NotRequired[Amount22 | Amount22Dict]
    target_amount: NotRequired[Amount34 | Amount34Dict]
    type_: NotRequired[str]
