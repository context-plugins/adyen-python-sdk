from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount31 import Amount31, Amount31Dict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .enhanced_scheme_data1 import EnhancedSchemeData1, EnhancedSchemeData1Dict
from .line_item import LineItem, LineItemDict
from .platform_chargeback_logic import PlatformChargebackLogic, PlatformChargebackLogicDict
from .split import Split, SplitDict
from .sub_merchant_info import SubMerchantInfo, SubMerchantInfoDict


class PaymentCaptureRequest(SdkBaseModel):
    amount: Amount31
    """The amount that you want to capture. The ``currency`` must match the currency used in authorisation, the
    ``value`` must be smaller than or equal to the authorised amount."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    enhanced_scheme_data: Optional[EnhancedSchemeData1] = Field(default=UNSET, alias="enhancedSchemeData")
    """Enhanced scheme data that may be required for processing the payment. For example, airline information."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information of the refunded items, required for `partial refunds
    <https://docs.adyen.com/online-payments/refund#refund-a-payment>`__.
    > This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay,
        Walley, and Zip."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account that is used to process the payment."""

    platform_chargeback_logic: Optional[PlatformChargebackLogic] = Field(default=UNSET, alias="platformChargebackLogic")
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    reference: Optional[str] = UNSET
    """Your reference for the capture request. Maximum length: 80 characters."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms.
    For more information, see how to process payments for `marketplaces
    <https://docs.adyen.com/marketplaces/split-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/online-payments/split-payments/>`__."""

    sub_merchants: Optional[list[SubMerchantInfo]] = Field(default=UNSET, alias="subMerchants")
    """A List of sub-merchants."""


class PaymentCaptureRequestDict(TypedDict):
    amount: Amount31 | Amount31Dict
    application_info: NotRequired[ApplicationInfo | ApplicationInfoDict]
    enhanced_scheme_data: NotRequired[EnhancedSchemeData1 | EnhancedSchemeData1Dict]
    line_items: NotRequired[list[LineItem | LineItemDict]]
    merchant_account: str
    platform_chargeback_logic: NotRequired[PlatformChargebackLogic | PlatformChargebackLogicDict]
    reference: NotRequired[str]
    splits: NotRequired[list[Split | SplitDict]]
    sub_merchants: NotRequired[list[SubMerchantInfo | SubMerchantInfoDict]]
