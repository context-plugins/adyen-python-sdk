from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .amount39 import Amount39, Amount39Dict
from .enums.merchant_refund_reason1 import MerchantRefundReason1OrStr
from .line_item import LineItem, LineItemDict
from .split import Split, SplitDict


class PaymentRefundResponse(SdkBaseModel):
    amount: Amount39
    """The refund amount."""

    capture_psp_reference: Optional[str] = Field(default=UNSET, alias="capturePspReference")
    """This is only available for PayPal refunds. The
    https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the specific capture
    to refund."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information of the refunded items, required for `partial refunds
    <https://docs.adyen.com/online-payments/refund#refund-a-payment>`__.
    > This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay,
        Walley, and Zip."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    merchant_refund_reason: OptionalNullable[MerchantRefundReason1OrStr] = Field(
        default=UNSET, alias="merchantRefundReason"
    )
    """Your reason for the refund request."""

    payment_psp_reference: str = Field(alias="paymentPspReference")
    """The https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the payment
    to refund."""

    psp_reference: str = Field(alias="pspReference")
    """Adyen's 16-character reference associated with the refund request."""

    reference: Optional[str] = UNSET
    """Your reference for the refund request."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to process payments for `marketplaces
    <https://docs.adyen.com/marketplaces/split-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/online-payments/split-payments/>`__."""

    status: Literal["received"] = "received"
    """The status of your request. This will always have the value **received**."""

    store: Optional[str] = UNSET
    """The online store or `physical store
    <https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores>`__ that is
    processing the refund. This must be the same as the store name configured in your Customer Area. Otherwise, you get
    an error and the refund fails."""


class PaymentRefundResponseDict(TypedDict):
    amount: Amount39 | Amount39Dict
    capture_psp_reference: NotRequired[str]
    line_items: NotRequired[list[LineItem | LineItemDict]]
    merchant_account: str
    merchant_refund_reason: NotRequired[MerchantRefundReason1OrStr | None]
    payment_psp_reference: str
    psp_reference: str
    reference: NotRequired[str]
    splits: NotRequired[list[Split | SplitDict]]
    status: NotRequired[Literal["received"]]
    store: NotRequired[str]
