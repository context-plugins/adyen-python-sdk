from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AmountsResp1(SdkBaseModel):
    """Various amounts related to the payment response from the POI System. Amounts approved by the POI and the Acquirer
    for the payment and loyalty transaction, containing:
      * The authorised amount to be paid.
      * The amount of the rebates.
      * The amount of financial fees.
      * The cash back part of the requested amount for a payment with cash back.
      * The tip part of the requested amount for a payment with tip."""

    currency: Optional[str] = Field(default=UNSET, alias="Currency")
    """Currency of a monetary amount."""

    authorized_amount: float = Field(alias="AuthorizedAmount")
    """Amount requested by the Sale for the payment."""

    total_rebates_amount: Optional[float] = Field(default=UNSET, alias="TotalRebatesAmount")
    """Sum of rebates in amount (total amount or line item amount) for all the loyalty programs."""

    total_fees_amount: Optional[float] = Field(default=UNSET, alias="TotalFeesAmount")
    """Total amount of financial fees."""

    cash_back_amount: Optional[float] = Field(default=UNSET, alias="CashBackAmount")
    """The cash-back part of the amount requested by the Sale for the payment."""

    tip_amount: Optional[float] = Field(default=UNSET, alias="TipAmount")
    """Amount paid for a tip. Allow the printing of the tip on the receipt, and to qualify the tip part of the
    amount."""


class AmountsResp1Dict(TypedDict):
    currency: NotRequired[str]
    authorized_amount: float
    total_rebates_amount: NotRequired[float]
    total_fees_amount: NotRequired[float]
    cash_back_amount: NotRequired[float]
    tip_amount: NotRequired[float]
