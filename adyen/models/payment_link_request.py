from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .address2 import Address2, Address2Dict
from .address3 import Address3, Address3Dict
from .amount35 import Amount35, Amount35Dict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .checkout_session_three_ds2_request_data3 import (
    CheckoutSessionThreeDs2RequestData3,
    CheckoutSessionThreeDs2RequestData3Dict,
)
from .enums.recurring_processing_model4 import RecurringProcessingModel4OrStr
from .enums.required_shopper_field import RequiredShopperFieldOrStr
from .enums.store_payment_method_mode2 import StorePaymentMethodMode2OrStr
from .fund_origin1 import FundOrigin1, FundOrigin1Dict
from .fund_recipient1 import FundRecipient1, FundRecipient1Dict
from .installment_option import InstallmentOption, InstallmentOptionDict
from .line_item import LineItem, LineItemDict
from .name4 import Name4, Name4Dict
from .platform_chargeback_logic4 import PlatformChargebackLogic4, PlatformChargebackLogic4Dict
from .risk_data1 import RiskData1, RiskData1Dict
from .split import Split, SplitDict


class PaymentLinkRequest(SdkBaseModel):
    allowed_payment_methods: Optional[list[str]] = Field(default=UNSET, alias="allowedPaymentMethods")
    """List of payment methods to be presented to the shopper. To refer to payment methods, use their `payment method
    type <https://docs.adyen.com/payment-methods/payment-method-types>`__.

    Example: ``"allowedPaymentMethods":["ideal","applepay"]``"""

    amount: Amount35
    """The payment amount and currency."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    billing_address: Optional[Address3] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    blocked_payment_methods: Optional[list[str]] = Field(default=UNSET, alias="blockedPaymentMethods")
    """List of payment methods to be hidden from the shopper. To refer to payment methods, use their `payment method
    type <https://docs.adyen.com/payment-methods/payment-method-types>`__.

    Example: ``"blockedPaymentMethods":["ideal","applepay"]``"""

    capture_delay_hours: Optional[int] = Field(default=UNSET, alias="captureDelayHours")
    """The delay between the authorisation and scheduled auto-capture, specified in hours."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The shopper's two-letter country code."""

    date_of_birth: Optional[Date] = Field(default=UNSET, alias="dateOfBirth")
    """The shopper's date of birth.

    Format `ISO-8601 <https://www.w3.org/TR/NOTE-datetime>`__: YYYY-MM-DD"""

    deliver_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliverAt")
    """The date and time when the purchased goods should be delivered.

    `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__ format: YYYY-MM-DDThh:mm:ss+TZD, for example,
    **2020-12-18T10:15:30+01:00**."""

    delivery_address: Optional[Address2] = Field(default=UNSET, alias="deliveryAddress")
    """The address where the purchased goods should be delivered."""

    description: Optional[str] = UNSET
    """A short description visible on the payment page. Maximum length: 280 characters."""

    expires_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expiresAt")
    """The date when the payment link expires.

    `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__ format with time zone offset: YYYY-MM-DDThh:mm:ss+TZD, for
    example, **2020-12-18T10:15:30+01:00**.

    The maximum expiry date is 70 days after the payment link is created.

    If not provided, the payment link expires 24 hours after it was created."""

    fund_origin: Optional[FundOrigin1] = Field(default=UNSET, alias="fundOrigin")
    """The person or entity funding the money."""

    fund_recipient: Optional[FundRecipient1] = Field(default=UNSET, alias="fundRecipient")
    """the person or entity receiving the money"""

    installment_options: Optional[dict[str, InstallmentOption]] = Field(default=UNSET, alias="installmentOptions")
    """A set of key-value pairs that specifies the installment options available per payment method. The key must be a
    payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or
    **mc**. The value must be an object containing the installment options."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information about the purchased items, to be included on the invoice sent to the shopper.
    > This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty."""

    manual_capture: Optional[bool] = Field(default=UNSET, alias="manualCapture")
    """Indicates if the payment must be `captured manually <https://docs.adyen.com/online-payments/capture>`__."""

    mcc: Optional[str] = UNSET
    """The `merchant category code <https://en.wikipedia.org/wiki/Merchant_category_code>`__ (MCC) is a four-digit
    number, which relates to a particular market segment. This code reflects the predominant activity that is conducted
    by the merchant."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier for which the payment link is created."""

    merchant_order_reference: Optional[str] = Field(default=UNSET, alias="merchantOrderReference")
    """This reference allows linking multiple transactions to each other for reporting purposes (for example, order
    auth-rate). The reference should be unique per billing cycle."""

    metadata: Optional[dict[str, str]] = UNSET
    """Metadata consists of entries, each of which includes a key and a value. Limitations:
    * Maximum 20 key-value pairs per request. Otherwise, error "177" occurs: "Metadata size exceeds limit"
    * Maximum 20 characters per key. Otherwise, error "178" occurs: "Metadata key size exceeds limit"
    * A key cannot have the name ``checkout.linkId``. Any value that you provide with this key is going to be replaced
        by the real payment link ID."""

    platform_chargeback_logic: Optional[PlatformChargebackLogic4] = Field(
        default=UNSET, alias="platformChargebackLogic"
    )
    """Dictates the behavior of how a potential chargeback should be booked when using Adyen Platforms."""

    recurring_processing_model: Optional[RecurringProcessingModel4OrStr] = Field(
        default=UNSET, alias="recurringProcessingModel"
    )
    """Defines a recurring payment type. Required when ``storePaymentMethodMode`` is set to **askForConsent** or
    **enabled**. Possible values:
    * **Subscription** – A transaction for a fixed or variable amount, which follows a fixed schedule.
    * **CardOnFile** – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel
        journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also
        considered a card-on-file transaction.
    * **UnscheduledCardOnFile** – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a
        non-fixed schedule and/or has variable amounts. For example, automatic top-ups when a cardholder's balance drops
        below a certain amount."""

    reference: str
    """A reference that is used to uniquely identify the payment in future communications about the payment status."""

    required_shopper_fields: Optional[list[RequiredShopperFieldOrStr]] = Field(
        default=UNSET, alias="requiredShopperFields"
    )
    """List of fields that the shopper has to provide on the payment page before completing the payment. For more
    information, refer to `Provide shopper information
    <https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#shopper-information>`__.

    Possible values:
    * **billingAddress** – The address where to send the invoice.
    * **deliveryAddress** – The address where the purchased goods should be delivered.
    * **shopperEmail** – The shopper's email address.
    * **shopperName** – The shopper's full name.
    * **telephoneNumber** – The shopper's phone number."""

    return_url: Optional[str] = Field(default=UNSET, alias="returnUrl")
    """Website URL used for redirection after payment is completed. If provided, a **Continue** button will be shown on
    the payment page. If shoppers select the button, they are redirected to the specified URL."""

    reusable: Optional[bool] = UNSET
    """Indicates whether the payment link can be reused for multiple payments. If not provided, this defaults to
    **false** which means the link can be used for one successful payment only."""

    risk_data: Optional[RiskData1] = Field(default=UNSET, alias="riskData")
    """Any risk-related settings to apply to the payment."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper's email address."""

    shopper_locale: Optional[str] = Field(default=UNSET, alias="shopperLocale")
    """The language to be used in the payment page, specified by a combination of a language and country code. For
    example, ``en-US``.

    For a list of shopper locales that Pay by Link supports, refer to `Language and localization
    <https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#language>`__."""

    shopper_name: Optional[Name4] = Field(default=UNSET, alias="shopperName")
    """The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're
    enrolled in the PayPal Seller Protection program."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive
    and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    shopper_statement: Optional[str] = Field(default=UNSET, alias="shopperStatement")
    """The text to be shown on the shopper's bank statement.
     We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
     Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**."""

    show_remove_payment_method_button: Optional[bool] = Field(default=UNSET, alias="showRemovePaymentMethodButton")
    """Set to **false** to hide the button that lets the shopper remove a stored payment method."""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """The shopper's social security number."""

    split_card_funding_sources: Optional[bool] = Field(default=UNSET, alias="splitCardFundingSources")
    """Boolean value indicating whether the card payment method should be split into separate debit and credit
    options."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how to split a payment when using `Adyen for Platforms
    <https://docs.adyen.com/platforms/process-payments#providing-split-information>`__, `Classic Platforms integration
    <https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information>`__, or `Issuing
    <https://docs.adyen.com/issuing/manage-funds#split>`__."""

    store: Optional[str] = UNSET
    """The physical store, for which this payment is processed."""

    store_payment_method_mode: Optional[StorePaymentMethodMode2OrStr] = Field(
        default=UNSET, alias="storePaymentMethodMode"
    )
    """Indicates if the details of the payment method will be stored for the shopper. Possible values:
    * **disabled** – No details will be stored (default).
    * **askForConsent** – If the ``shopperReference`` is provided, the Drop-in/Component shows a checkbox where the
        shopper can select to store their payment details for card payments.
    * **enabled** – If the ``shopperReference`` is provided, the details will be stored without asking the shopper for
        consent.
     When set to **askForConsent** or **enabled**, you must also include the ``recurringProcessingModel`` parameter."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's telephone number.
     The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15
        digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``."""

    theme_id: Optional[str] = Field(default=UNSET, alias="themeId")
    """A `theme <https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#themes>`__ to customize the
    appearance of the payment page. If not specified, the payment page is rendered according to the theme set as default
    in your Customer Area."""

    three_ds2_request_data: Optional[CheckoutSessionThreeDs2RequestData3] = Field(
        default=UNSET, alias="threeDS2RequestData"
    )
    """The cardholder phone number need to be part of the authentication message for payment data. It is a requirement
    for Visa Secure Authentication Data Field Mandate effective August 2024."""


class PaymentLinkRequestDict(TypedDict):
    allowed_payment_methods: NotRequired[list[str]]
    amount: Amount35 | Amount35Dict
    application_info: NotRequired[ApplicationInfo | ApplicationInfoDict]
    billing_address: NotRequired[Address3 | Address3Dict]
    blocked_payment_methods: NotRequired[list[str]]
    capture_delay_hours: NotRequired[int]
    country_code: NotRequired[str]
    date_of_birth: NotRequired[Date]
    deliver_at: NotRequired[RFC3339DateTime]
    delivery_address: NotRequired[Address2 | Address2Dict]
    description: NotRequired[str]
    expires_at: NotRequired[RFC3339DateTime]
    fund_origin: NotRequired[FundOrigin1 | FundOrigin1Dict]
    fund_recipient: NotRequired[FundRecipient1 | FundRecipient1Dict]
    installment_options: NotRequired[dict[str, InstallmentOption | InstallmentOptionDict]]
    line_items: NotRequired[list[LineItem | LineItemDict]]
    manual_capture: NotRequired[bool]
    mcc: NotRequired[str]
    merchant_account: str
    merchant_order_reference: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    platform_chargeback_logic: NotRequired[PlatformChargebackLogic4 | PlatformChargebackLogic4Dict]
    recurring_processing_model: NotRequired[RecurringProcessingModel4OrStr]
    reference: str
    required_shopper_fields: NotRequired[list[RequiredShopperFieldOrStr]]
    return_url: NotRequired[str]
    reusable: NotRequired[bool]
    risk_data: NotRequired[RiskData1 | RiskData1Dict]
    shopper_email: NotRequired[str]
    shopper_locale: NotRequired[str]
    shopper_name: NotRequired[Name4 | Name4Dict]
    shopper_reference: NotRequired[str]
    shopper_statement: NotRequired[str]
    show_remove_payment_method_button: NotRequired[bool]
    social_security_number: NotRequired[str]
    split_card_funding_sources: NotRequired[bool]
    splits: NotRequired[list[Split | SplitDict]]
    store: NotRequired[str]
    store_payment_method_mode: NotRequired[StorePaymentMethodMode2OrStr]
    telephone_number: NotRequired[str]
    theme_id: NotRequired[str]
    three_ds2_request_data: NotRequired[CheckoutSessionThreeDs2RequestData3 | CheckoutSessionThreeDs2RequestData3Dict]
