from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount30 import Amount30, Amount30Dict
from .enums.industry_usage1 import IndustryUsage1OrStr
from .enums.status2 import Status2OrStr
from .line_item import LineItem, LineItemDict
from .split import Split, SplitDict


class PaymentAmountUpdateResponse(SdkBaseModel):
    adjust_authorisation_data: Optional[str] = Field(default=UNSET, alias="adjustAuthorisationData")
    """The data blob for subsequent synchronous adjust authorisation calls. Returned when the synchronous flow is
    used."""

    amount: Amount30
    """The updated amount."""

    industry_usage: Optional[IndustryUsage1OrStr] = Field(default=UNSET, alias="industryUsage")
    """The reason for the amount update. Possible values:
    * **delayedCharge**
    * **noShow**
    * **installment**"""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information of the refunded items, required for `partial refunds
    <https://docs.adyen.com/online-payments/refund#refund-a-payment>`__.
    > This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay,
        Walley, and Zip."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    payment_psp_reference: str = Field(alias="paymentPspReference")
    """The https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the payment
    to update."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character reference associated with the amount update request."""

    reference: str
    """Your reference for the amount update request. Maximum length: 80 characters."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to process payments for `marketplaces
    <https://docs.adyen.com/marketplaces/process-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/process-payments>`__."""

    status: Status2OrStr
    """The status of your request.

    If you included ``adjustAuthorisationData`` in your request, possible values are the following:

    * **authorised**

    * **refused**

    Otherwise, the value is **received**."""


class PaymentAmountUpdateResponseDict(TypedDict):
    adjust_authorisation_data: NotRequired[str]
    amount: Amount30Dict
    industry_usage: NotRequired[IndustryUsage1OrStr]
    line_items: NotRequired[list[LineItemDict]]
    merchant_account: str
    payment_psp_reference: str
    psp_reference: str
    reference: str
    splits: NotRequired[list[SplitDict]]
    status: Status2OrStr
