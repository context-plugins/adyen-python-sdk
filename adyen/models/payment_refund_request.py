from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .amount38 import Amount38, Amount38Dict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .enhanced_scheme_data1 import EnhancedSchemeData1, EnhancedSchemeData1Dict
from .enums.merchant_refund_reason import MerchantRefundReasonOrStr
from .line_item import LineItem, LineItemDict
from .split import Split, SplitDict


class PaymentRefundRequest(SdkBaseModel):
    amount: Amount38
    """The amount that you want to refund. The ``currency`` must match the currency used in authorisation, the ``value``
    must be smaller than or equal to the authorised amount."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    capture_psp_reference: Optional[str] = Field(default=UNSET, alias="capturePspReference")
    """This is only available for PayPal refunds. The
    https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference of the specific capture
    to refund."""

    enhanced_scheme_data: Optional[EnhancedSchemeData1] = Field(default=UNSET, alias="enhancedSchemeData")
    """Enhanced scheme data that may be required for processing the payment. For example, airline information."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information of the refunded items, required for `partial refunds
    <https://docs.adyen.com/online-payments/refund#refund-a-payment>`__.
    > This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay,
        Walley, and Zip."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    merchant_refund_reason: OptionalNullable[MerchantRefundReasonOrStr] = Field(
        default=UNSET, alias="merchantRefundReason"
    )
    """The reason for the refund request.

    Possible values:

    * **FRAUD**

    * **CUSTOMER REQUEST**

    * **RETURN**

    * **DUPLICATE**

    * **OTHER**"""

    reference: Optional[str] = UNSET
    """Your reference for the refund request. Maximum length: 80 characters."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to process payments for `marketplaces
    <https://docs.adyen.com/marketplaces/split-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/online-payments/split-payments/>`__."""

    store: Optional[str] = UNSET
    """The online store or `physical store
    <https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores>`__ that is
    processing the refund. This must be the same as the store name configured in your Customer Area. Otherwise, you get
    an error and the refund fails."""


class PaymentRefundRequestDict(TypedDict):
    amount: Amount38Dict
    application_info: NotRequired[ApplicationInfoDict]
    capture_psp_reference: NotRequired[str]
    enhanced_scheme_data: NotRequired[EnhancedSchemeData1Dict]
    line_items: NotRequired[list[LineItemDict]]
    merchant_account: str
    merchant_refund_reason: NotRequired[MerchantRefundReasonOrStr | None]
    reference: NotRequired[str]
    splits: NotRequired[list[SplitDict]]
    store: NotRequired[str]
