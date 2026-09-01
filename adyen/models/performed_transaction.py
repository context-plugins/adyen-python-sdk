from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_result import LoyaltyResult, LoyaltyResultDict
from .payment_result1 import PaymentResult1, PaymentResult1Dict
from .poidata import Poidata, PoidataDict
from .response1 import Response1, Response1Dict
from .sale_data import SaleData, SaleDataDict


class PerformedTransaction(SdkBaseModel):
    response: Response1 = Field(alias="Response")
    """Result of a message request processing. If Result is Success, ``ErrorCondition`` is absent or not used in the
    processing of the message. In the other cases, the ``ErrorCondition`` has to be present and can refine the
    processing of the message response. ``AdditionalResponse`` gives more information about the success or the failure
    of the message request processing, for logging without real time involvements."""

    sale_data: Optional[SaleData] = Field(default=UNSET, alias="SaleData")
    """Data associated with the Sale System, with a particular value during the processing of the payment by the POI,
    including the cards acquisition."""

    poi_data: Optional[Poidata] = Field(default=UNSET, alias="POIData")
    """Data related to the POI System. In the Message Response, identification of the POI transaction."""

    payment_result: Optional[PaymentResult1] = Field(default=UNSET, alias="PaymentResult")
    loyalty_result: Optional[list[LoyaltyResult]] = Field(default=UNSET, alias="LoyaltyResult")
    reversed_amount: Optional[float] = Field(default=UNSET, alias="ReversedAmount")


class PerformedTransactionDict(TypedDict):
    response: Response1 | Response1Dict
    sale_data: NotRequired[SaleData | SaleDataDict]
    poi_data: NotRequired[Poidata | PoidataDict]
    payment_result: NotRequired[PaymentResult1 | PaymentResult1Dict]
    loyalty_result: NotRequired[list[LoyaltyResult | LoyaltyResultDict]]
    reversed_amount: NotRequired[float]
