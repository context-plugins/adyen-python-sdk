from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .loyalty_data import LoyaltyData, LoyaltyDataDict
from .payment_data1 import PaymentData1, PaymentData1Dict
from .payment_transaction1 import PaymentTransaction1, PaymentTransaction1Dict
from .sale_data1 import SaleData1, SaleData1Dict


class PaymentRequest2(SdkBaseModel):
    """Request sent to terminal to initiate payment. It conveys Information related to the Payment transaction to
    process. Content of the ``PaymentRequest`` message."""

    sale_data: SaleData1 = Field(alias="SaleData")
    """Data related to the Sale System."""

    payment_transaction: PaymentTransaction1 = Field(alias="PaymentTransaction")
    """Data related to the payment and loyalty transaction."""

    payment_data: Optional[PaymentData1] = Field(default=UNSET, alias="PaymentData")
    """Data related to the payment transaction. If one data element is present."""

    loyalty_data: Optional[list[LoyaltyData]] = Field(default=UNSET, alias="LoyaltyData")
    """Data related to a Loyalty program or account. Loyalty cards used with the payment transaction and read by the
    Sale System."""


class PaymentRequest2Dict(TypedDict):
    sale_data: SaleData1 | SaleData1Dict
    payment_transaction: PaymentTransaction1 | PaymentTransaction1Dict
    payment_data: NotRequired[PaymentData1 | PaymentData1Dict]
    loyalty_data: NotRequired[list[LoyaltyData | LoyaltyDataDict]]
