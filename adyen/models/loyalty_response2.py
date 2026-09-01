from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_result import LoyaltyResult, LoyaltyResultDict
from .payment_receipt import PaymentReceipt, PaymentReceiptDict
from .poidata1 import Poidata1, Poidata1Dict
from .response11 import Response11, Response11Dict
from .sale_data1 import SaleData1, SaleData1Dict


class LoyaltyResponse2(SdkBaseModel):
    """Content of the Loyalty Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    sale_data: SaleData1 = Field(alias="SaleData")
    """Data related to the Sale System."""

    poi_data: Poidata1 = Field(alias="POIData")
    """Data related to the POI System."""

    loyalty_result: Optional[list[LoyaltyResult]] = Field(default=UNSET, alias="LoyaltyResult")
    """Data related to the result of a processed loyalty transaction. If loyalty account identified."""

    payment_receipt: Optional[list[PaymentReceipt]] = Field(default=UNSET, alias="PaymentReceipt")


class LoyaltyResponse2Dict(TypedDict):
    response: Response11 | Response11Dict
    sale_data: SaleData1 | SaleData1Dict
    poi_data: Poidata1 | Poidata1Dict
    loyalty_result: NotRequired[list[LoyaltyResult | LoyaltyResultDict]]
    payment_receipt: NotRequired[list[PaymentReceipt | PaymentReceiptDict]]
