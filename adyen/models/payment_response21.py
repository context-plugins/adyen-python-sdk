from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_result import LoyaltyResult, LoyaltyResultDict
from .payment_receipt import PaymentReceipt, PaymentReceiptDict
from .payment_result11 import PaymentResult11, PaymentResult11Dict
from .poidata1 import Poidata1, Poidata1Dict
from .response11 import Response11, Response11Dict
from .sale_data6 import SaleData6, SaleData6Dict


class PaymentResponse21(SdkBaseModel):
    """Content of the Payment Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    sale_data: SaleData6 = Field(alias="SaleData")
    """Data related to the Sale System. Copy."""

    poi_data: Poidata1 = Field(alias="POIData")
    """Data related to the POI System."""

    payment_result: Optional[PaymentResult11] = Field(default=UNSET, alias="PaymentResult")
    """Data related to the result of a processed payment transaction. If one data element is present."""

    loyalty_result: Optional[list[LoyaltyResult]] = Field(default=UNSET, alias="LoyaltyResult")
    """Data related to the result of a processed loyalty transaction. Loyalty cards used with the payment
    transaction."""

    payment_receipt: Optional[list[PaymentReceipt]] = Field(default=UNSET, alias="PaymentReceipt")
    """Customer or Merchant payment receipt. If the payment receipts are printed by the Sale system and the POI or the
    Sale does not implement the Print exchange (Basic profile)."""


class PaymentResponse21Dict(TypedDict):
    response: Response11 | Response11Dict
    sale_data: SaleData6 | SaleData6Dict
    poi_data: Poidata1 | Poidata1Dict
    payment_result: NotRequired[PaymentResult11 | PaymentResult11Dict]
    loyalty_result: NotRequired[list[LoyaltyResult | LoyaltyResultDict]]
    payment_receipt: NotRequired[list[PaymentReceipt | PaymentReceiptDict]]
