from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amounts_req import AmountsReq, AmountsReqDict
from .original_poitransaction import OriginalPoitransaction, OriginalPoitransactionDict
from .transaction_conditions import TransactionConditions, TransactionConditionsDict


class PaymentTransaction1(SdkBaseModel):
    """Data related to the payment and loyalty transaction."""

    amounts_req: AmountsReq = Field(alias="AmountsReq")
    """Various amounts related to the payment request from the Sale System."""

    original_poi_transaction: Optional[OriginalPoitransaction] = Field(default=UNSET, alias="OriginalPOITransaction")
    """Identification of a previous POI transaction. In the Payment Request message, it allows using the card of a
    previous CardAcquisition or Payment request."""

    transaction_conditions: Optional[TransactionConditions] = Field(default=UNSET, alias="TransactionConditions")
    """Conditions on which the transaction must be processed."""


class PaymentTransaction1Dict(TypedDict):
    amounts_req: AmountsReqDict
    original_poi_transaction: NotRequired[OriginalPoitransactionDict]
    transaction_conditions: NotRequired[TransactionConditionsDict]
