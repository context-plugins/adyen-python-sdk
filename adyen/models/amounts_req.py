from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AmountsReq(SdkBaseModel):
    """Various amounts related to the payment request from the Sale System."""

    currency: str = Field(alias="Currency")
    """Currency of a monetary amount."""

    requested_amount: float = Field(alias="RequestedAmount")
    """Amount requested by the Sale for the payment."""

    cash_back_amount: Optional[float] = Field(default=UNSET, alias="CashBackAmount")
    """The cash-back part of the amount requested by the Sale for the payment."""

    tip_amount: Optional[float] = Field(default=UNSET, alias="TipAmount")
    """Amount paid for a tip. Allow the printing of the tip on the receipt, and to qualify the tip part of the
    amount."""

    paid_amount: Optional[float] = Field(default=UNSET, alias="PaidAmount")
    """Amount already paid in case of split payment. Depending on the context, a split payment is either a split amount,
    or a split basket (required by some payment means as fleet cards). The PaidAmount is present when the split payment
    is a split
         of the amount. Split of the basket involves two Sale Transactions, and does not have to be recognised by
         the POI."""

    minimum_amount_to_deliver: Optional[float] = Field(default=UNSET, alias="MinimumAmountToDeliver")
    """Minimum amount the Sale System is allowed to deliver for this payment. For the OneTimeReservation, when the
    maximum amount is unknown, the Sale System indicates the minimum amount it allows."""

    maximum_cash_back_amount: Optional[float] = Field(default=UNSET, alias="MaximumCashBackAmount")
    """Maximum amount which could be requested for cash-back to the Sale System. Allows the Cashier
       to limit the amount value of cash-back to deliver to the Customer."""

    minimum_split_amount: Optional[float] = Field(default=UNSET, alias="MinimumSplitAmount")
    """Minimum amount of a split, which could be requested by a Customer.Allows the Merchant to limit the number of
    split requested by the Customer."""


class AmountsReqDict(TypedDict):
    currency: str
    requested_amount: float
    cash_back_amount: NotRequired[float]
    tip_amount: NotRequired[float]
    paid_amount: NotRequired[float]
    minimum_amount_to_deliver: NotRequired[float]
    maximum_cash_back_amount: NotRequired[float]
    minimum_split_amount: NotRequired[float]
