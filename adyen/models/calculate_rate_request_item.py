from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .amount19 import Amount19, Amount19Dict
from .enums.exchange_side2 import ExchangeSide2OrStr
from .enums.rate_type2 import RateType2OrStr


class CalculateRateRequestItem(SdkBaseModel):
    """The request parameters required to calculate an amount in a different currency."""

    exchange_side: ExchangeSide2OrStr = Field(alias="exchangeSide")
    """The operation performed on the source amount. Possible values:
    * **buy**
    * **sell**"""

    source_amount: Amount19 = Field(alias="sourceAmount")
    """An object specifying the currency and value for which you want to perform an exchange calculation."""

    target_currency: str = Field(alias="targetCurrency")
    """The currency to which you want to convert the source amount."""

    type_: RateType2OrStr = Field(alias="type")
    """The type of transaction. Possible values:
    * **splitPayment**: for payments
    * **splitRefund**: for refunds"""


class CalculateRateRequestItemDict(TypedDict):
    exchange_side: ExchangeSide2OrStr
    source_amount: Amount19 | Amount19Dict
    target_currency: str
    type_: RateType2OrStr
