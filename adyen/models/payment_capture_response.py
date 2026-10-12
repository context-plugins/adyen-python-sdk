from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount33 import Amount33, Amount33Dict
from .line_item import LineItem, LineItemDict
from .platform_chargeback_logic import PlatformChargebackLogic, PlatformChargebackLogicDict
from .split import Split, SplitDict
from .sub_merchant_info import SubMerchantInfo, SubMerchantInfoDict


class PaymentCaptureResponse(SdkBaseModel):
    amount: Amount33
    """The captured amount."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information of the refunded items, required for `partial refunds
    <https://docs.adyen.com/online-payments/refund#refund-a-payment>`__.
    > This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay,
        Walley, and Zip."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    payment_psp_reference: str = Field(alias="paymentPspReference")
    """The https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the payment
    to capture."""

    platform_chargeback_logic: Optional[PlatformChargebackLogic] = Field(default=UNSET, alias="platformChargebackLogic")
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character reference associated with the capture request."""

    reference: Optional[str] = UNSET
    """Your reference for the capture request."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to process payments for `marketplaces
    <https://docs.adyen.com/marketplaces/split-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/online-payments/split-payments/>`__."""

    status: Literal["received"] = "received"
    """The status of your request. This will always have the value **received**."""

    sub_merchants: Optional[list[SubMerchantInfo]] = Field(default=UNSET, alias="subMerchants")
    """List of sub-merchants."""


class PaymentCaptureResponseDict(TypedDict):
    amount: Amount33Dict
    line_items: NotRequired[list[LineItemDict]]
    merchant_account: str
    payment_psp_reference: str
    platform_chargeback_logic: NotRequired[PlatformChargebackLogicDict]
    psp_reference: str
    reference: NotRequired[str]
    splits: NotRequired[list[SplitDict]]
    status: Literal["received"]
    sub_merchants: NotRequired[list[SubMerchantInfoDict]]
