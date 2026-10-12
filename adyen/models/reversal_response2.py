from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .original_poitransaction import OriginalPoitransaction, OriginalPoitransactionDict
from .payment_receipt import PaymentReceipt, PaymentReceiptDict
from .poidata4 import Poidata4, Poidata4Dict
from .response11 import Response11, Response11Dict


class ReversalResponse2(SdkBaseModel):
    """Content of the Reversal Response message."""

    response: Response11 = Field(alias="Response")
    """Result of a message request processing."""

    poi_data: Optional[Poidata4] = Field(default=UNSET, alias="POIData")
    """Data related to the POI System. If Result is Success."""

    original_poi_transaction: Optional[OriginalPoitransaction] = Field(default=UNSET, alias="OriginalPOITransaction")
    """Identification of a previous POI transaction. In the Payment Request message, it allows using the card of a
    previous CardAcquisition or Payment request."""

    reversed_amount: Optional[float] = Field(default=UNSET, alias="ReversedAmount")
    """Amount of the payment or loyalty to reverse. Copy."""

    payment_receipt: Optional[list[PaymentReceipt]] = Field(default=UNSET, alias="PaymentReceipt")


class ReversalResponse2Dict(TypedDict):
    response: Response11Dict
    poi_data: NotRequired[Poidata4Dict]
    original_poi_transaction: NotRequired[OriginalPoitransactionDict]
    reversed_amount: NotRequired[float]
    payment_receipt: NotRequired[list[PaymentReceiptDict]]
