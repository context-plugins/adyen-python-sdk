from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, RFC3339DateTime, SdkBaseModel
from .account_info import AccountInfo, AccountInfoDict
from .address import Address, AddressDict
from .amount import Amount, AmountDict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .browser_info import BrowserInfo, BrowserInfoDict
from .enums.recurring_processing_model import RecurringProcessingModelOrStr
from .enums.shopper_interaction import ShopperInteractionOrStr
from .forex_quote11 import ForexQuote11, ForexQuote11Dict
from .installments import Installments, InstallmentsDict
from .merchant_risk_indicator11 import MerchantRiskIndicator11, MerchantRiskIndicator11Dict
from .name import Name, NameDict
from .recurring import Recurring, RecurringDict
from .split import Split, SplitDict
from .three_ds2_request_data11 import ThreeDs2RequestData11, ThreeDs2RequestData11Dict
from .three_ds2_result import ThreeDs2Result, ThreeDs2ResultDict


class PaymentRequest3Ds2(SdkBaseModel):
    account_info: Optional[AccountInfo] = Field(default=UNSET, alias="accountInfo")
    """Shopper account information for 3D Secure 2.
    > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a
        frictionless flow."""

    additional_amount: Optional[Amount] = Field(default=UNSET, alias="additionalAmount")
    """If you want a `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ request to use a non-zero value,
    assign this value to ``additionalAmount`` (while the amount must be still set to 0 to trigger BIN or card
    verification). Required to be in the same currency as the ``amount``."""

    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular payment request.

    The ``additionalData`` object consists of entries, each of which includes the key and value."""

    amount: Amount
    """The amount information for the transaction (in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__). For `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ requests, set amount to 0
    (zero)."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    billing_address: Optional[Address] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice.
    > The ``billingAddress`` object is required in the following scenarios. Include all of the fields within this
        object.
    >* For 3D Secure 2 transactions in all browser-based and mobile implementations. >* For cross-border payouts to and
    from Canada."""

    browser_info: Optional[BrowserInfo] = Field(default=UNSET, alias="browserInfo")
    """The shopper's browser information.
    > For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the
        ``userAgent`` and ``acceptHeader`` fields to indicate that your integration can support a redirect in case a
        payment is routed to 3D Secure 2 redirect."""

    capture_delay_hours: Optional[int] = Field(default=UNSET, alias="captureDelayHours")
    """The delay between the authorisation and scheduled auto-capture, specified in hours."""

    date_of_birth: Optional[Date] = Field(default=UNSET, alias="dateOfBirth")
    """The shopper's date of birth.

    Format `ISO-8601 <https://www.w3.org/TR/NOTE-datetime>`__: YYYY-MM-DD"""

    dcc_quote: Optional[ForexQuote11] = Field(default=UNSET, alias="dccQuote")
    """The forex quote as returned in the response of the forex service."""

    delivery_address: Optional[Address] = Field(default=UNSET, alias="deliveryAddress")
    """The address where the purchased goods should be delivered."""

    delivery_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveryDate")
    """The date and time the purchased goods should be delivered.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: YYYY-MM-DDThh:mm:ss.sssTZD

    Example: 2017-07-17T13:42:40.428+01:00"""

    device_fingerprint: Optional[str] = Field(default=UNSET, alias="deviceFingerprint")
    """A string containing the shopper's device fingerprint. For more information, refer to `Device fingerprinting
    <https://docs.adyen.com/risk-management/device-fingerprinting>`__."""

    fraud_offset: Optional[int] = Field(default=UNSET, alias="fraudOffset")
    """An integer value that is added to the normal fraud score. The value can be either positive or negative."""

    installments: Optional[Installments] = UNSET
    """Contains installment settings. For more information, refer to `Installments
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments>`__."""

    localized_shopper_statement: Optional[dict[str, str]] = Field(default=UNSET, alias="localizedShopperStatement")
    """The ``localizedShopperStatement`` field lets you use dynamic values for your shopper statement in a local
    character set. If this parameter is left empty, not provided, or not applicable (in case of cross-border
    transactions), then **shopperStatement** is used.

    Currently, ``localizedShopperStatement`` is only supported for payments with Visa, Mastercard, JCB, Diners, and
    Discover.

    **Supported characters**: Hiragana, Katakana, Kanji, and alphanumeric."""

    mcc: Optional[str] = UNSET
    """The `merchant category code <https://en.wikipedia.org/wiki/Merchant_category_code>`__ (MCC) is a four-digit
    number, which relates to a particular market segment. This code reflects the predominant activity that is conducted
    by the merchant."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    merchant_order_reference: Optional[str] = Field(default=UNSET, alias="merchantOrderReference")
    """This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate).
    The reference should be unique per billing cycle. The same merchant order reference should never be reused after the
    first authorised attempt. If used, this field should be supplied for all incoming authorisations.
    > We strongly recommend you send the ``merchantOrderReference`` value to benefit from linking payment requests when
        authorisation retries take place. In addition, we recommend you provide ``retry.orderAttemptNumber``,
        ``retry.chainAttemptNumber``, and ``retry.skipRetry`` values in ``PaymentRequest.additionalData``."""

    merchant_risk_indicator: Optional[MerchantRiskIndicator11] = Field(default=UNSET, alias="merchantRiskIndicator")
    """Additional risk fields for 3D Secure 2.
    > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a
        frictionless flow."""

    metadata: Optional[dict[str, str]] = UNSET
    """Metadata consists of entries, each of which includes a key and a value. Limits:
    * Maximum 20 key-value pairs per request. When exceeding, the "177" error occurs: "Metadata size exceeds limit".
    * Maximum 20 characters per key.
    * Maximum 80 characters per value."""

    order_reference: Optional[str] = Field(default=UNSET, alias="orderReference")
    """When you are doing multiple partial (gift card) payments, this is the ``pspReference`` of the first payment. We
    use this to link the multiple payments to each other. As your own reference for linking multiple payments, use the
    ``merchantOrderReference``instead."""

    recurring: Optional[Recurring] = UNSET
    """The recurring settings for the payment. Use this property when you want to enable `recurring payments
    <https://docs.adyen.com/classic-integration/recurring-payments>`__."""

    recurring_processing_model: Optional[RecurringProcessingModelOrStr] = Field(
        default=UNSET, alias="recurringProcessingModel"
    )
    """Defines a recurring payment type. Required when creating a token to store payment details or using stored payment
    details. Allowed values:
    * ``Subscription`` – A transaction for a fixed or variable amount, which follows a fixed schedule.
    * ``CardOnFile`` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel
        journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also
        considered a card-on-file transaction.
    * ``UnscheduledCardOnFile`` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a
        non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance
        drops below a certain amount."""

    reference: str
    """The reference to uniquely identify a payment. This reference is used in all communication with you about the
    payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to
    provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters."""

    selected_brand: Optional[str] = Field(default=UNSET, alias="selectedBrand")
    """Some payment methods require defining a value for this field to specify how to process the transaction.

    For the Bancontact payment method, it can be set to:
    * ``maestro`` (default), to be processed like a Maestro card, or
    * ``bcmc``, to be processed like a Bancontact card."""

    selected_recurring_detail_reference: Optional[str] = Field(default=UNSET, alias="selectedRecurringDetailReference")
    """The ``recurringDetailReference`` you want to use for this payment. The value ``LATEST`` can be used to select the
    most recently stored recurring detail."""

    session_id: Optional[str] = Field(default=UNSET, alias="sessionId")
    """A session ID used to identify a payment session."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. >
    Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include the
    ``telephoneNumber``."""

    shopper_ip: Optional[str] = Field(default=UNSET, alias="shopperIP")
    """The shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for
    instance, number of payment attempts or location-based checks).
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile
        integrations, if you did not include the ``shopperEmail``. For native mobile integrations, the field is required
        to support cases where authentication is routed to the redirect flow. This field is also mandatory for some
        merchants depending on your business model. For more information, `contact Support
        <https://www.adyen.help/hc/en-us/requests/new>`__."""

    shopper_interaction: Optional[ShopperInteractionOrStr] = Field(default=UNSET, alias="shopperInteraction")
    """Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a
    returning customer. For the web service API, Adyen assumes Ecommerce shopper interaction by default.

    This field has the following possible values:
    * ``Ecommerce`` - Online transactions where the cardholder is present (online). For better authorisation rates, we
        recommend sending the card security code (CSC) along with the request.
    * ``ContAuth`` - Card on file and/or subscription transactions, where the cardholder is known to the merchant
        (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation
        (one-click payment).
    * ``Moto`` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email
        or telephone.
    * ``POS`` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure
        payment terminal."""

    shopper_locale: Optional[str] = Field(default=UNSET, alias="shopperLocale")
    """The language for the payment. The value combines the two-letter `ISO 639-1
    <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`__ language code with the `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes>`__ country code. For example, **nl-NL**.

    When using Drop-in/Components, the specified language appears if your front-end global configuration does not set
    the ``locale``."""

    shopper_name: Optional[Name] = Field(default=UNSET, alias="shopperName")
    """The shopper's full name."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. The value is case-sensitive and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    shopper_statement: Optional[str] = Field(default=UNSET, alias="shopperStatement")
    """The text to be shown on the shopper's bank statement.
     We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
     Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**."""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """The shopper's social security number."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how the payment should be split when using either Adyen for Platforms for
    `marketplaces <https://docs.adyen.com/marketplaces/split-payments>`__ or `platforms
    <https://docs.adyen.com/platforms/split-payments>`__, or standalone `Issuing
    <https://docs.adyen.com/issuing/add-manage-funds#split>`__."""

    store: Optional[str] = UNSET
    """Required for Adyen for Platforms integrations if you are a platform model. This is your `reference
    <https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId>`__/stores#request-reference) (on
    `balance platform <https://docs.adyen.com/platforms>`__) or the `storeReference
    <https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference>`__
    (in the `classic integration
    <https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store>`__)
    for the ecommerce or point-of-sale store that is processing the payment."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's telephone number.
     The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15
        digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``."""

    three_ds2_request_data: Optional[ThreeDs2RequestData11] = Field(default=UNSET, alias="threeDS2RequestData")
    """Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer
    to `Online payments <https://docs.adyen.com/online-payments>`__ or `Classic integration
    <https://docs.adyen.com/classic-integration>`__ documentation."""

    three_ds2_result: Optional[ThreeDs2Result] = Field(default=UNSET, alias="threeDS2Result")
    """The ThreeDS2Result that was returned in the final CRes."""

    three_ds2_token: Optional[str] = Field(default=UNSET, alias="threeDS2Token")
    """The ThreeDS2Token that was returned in the /authorise call."""

    three_ds_authentication_only: bool = Field(default=False, alias="threeDSAuthenticationOnly")
    """Required to trigger the `authentication-only flow
    <https://docs.adyen.com/online-payments/3d-secure/authentication-only/>`__. If set to **true**, you will only
    perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**."""

    totals_group: Optional[str] = Field(default=UNSET, alias="totalsGroup")
    """The reference value to aggregate sales totals in reporting. When not specified, the store field is used (if
    available)."""

    trusted_shopper: Optional[bool] = Field(default=UNSET, alias="trustedShopper")
    """Set to true if the payment should be routed to a trusted MID."""


class PaymentRequest3Ds2Dict(TypedDict):
    account_info: NotRequired[AccountInfoDict]
    additional_amount: NotRequired[AmountDict]
    additional_data: NotRequired[dict[str, str]]
    amount: AmountDict
    application_info: NotRequired[ApplicationInfoDict]
    billing_address: NotRequired[AddressDict]
    browser_info: NotRequired[BrowserInfoDict]
    capture_delay_hours: NotRequired[int]
    date_of_birth: NotRequired[Date]
    dcc_quote: NotRequired[ForexQuote11Dict]
    delivery_address: NotRequired[AddressDict]
    delivery_date: NotRequired[RFC3339DateTime]
    device_fingerprint: NotRequired[str]
    fraud_offset: NotRequired[int]
    installments: NotRequired[InstallmentsDict]
    localized_shopper_statement: NotRequired[dict[str, str]]
    mcc: NotRequired[str]
    merchant_account: str
    merchant_order_reference: NotRequired[str]
    merchant_risk_indicator: NotRequired[MerchantRiskIndicator11Dict]
    metadata: NotRequired[dict[str, str]]
    order_reference: NotRequired[str]
    recurring: NotRequired[RecurringDict]
    recurring_processing_model: NotRequired[RecurringProcessingModelOrStr]
    reference: str
    selected_brand: NotRequired[str]
    selected_recurring_detail_reference: NotRequired[str]
    session_id: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_ip: NotRequired[str]
    shopper_interaction: NotRequired[ShopperInteractionOrStr]
    shopper_locale: NotRequired[str]
    shopper_name: NotRequired[NameDict]
    shopper_reference: NotRequired[str]
    shopper_statement: NotRequired[str]
    social_security_number: NotRequired[str]
    splits: NotRequired[list[SplitDict]]
    store: NotRequired[str]
    telephone_number: NotRequired[str]
    three_ds2_request_data: NotRequired[ThreeDs2RequestData11Dict]
    three_ds2_result: NotRequired[ThreeDs2ResultDict]
    three_ds2_token: NotRequired[str]
    three_ds_authentication_only: NotRequired[bool]
    totals_group: NotRequired[str]
    trusted_shopper: NotRequired[bool]
