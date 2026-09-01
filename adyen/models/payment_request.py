from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .account_info import AccountInfo, AccountInfoDict
from .amount1 import Amount1, Amount1Dict
from .amount2 import Amount2, Amount2Dict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .authentication_data3 import AuthenticationData3, AuthenticationData3Dict
from .billing_address3 import BillingAddress3, BillingAddress3Dict
from .browser_info import BrowserInfo, BrowserInfoDict
from .checkout_bank_account1 import CheckoutBankAccount1, CheckoutBankAccount1Dict
from .company1 import Company1, Company1Dict
from .delivery_address1 import DeliveryAddress1, DeliveryAddress1Dict
from .encrypted_order_data2 import EncryptedOrderData2, EncryptedOrderData2Dict
from .enhanced_scheme_data3 import EnhancedSchemeData3, EnhancedSchemeData3Dict
from .enums.channel2 import Channel2OrStr
from .enums.entity_type import EntityTypeOrStr
from .enums.industry_usage1 import IndustryUsage1OrStr
from .enums.recurring_processing_model import RecurringProcessingModelOrStr
from .enums.shopper_interaction import ShopperInteractionOrStr
from .forex_quote2 import ForexQuote2, ForexQuote2Dict
from .fund_origin1 import FundOrigin1, FundOrigin1Dict
from .fund_recipient1 import FundRecipient1, FundRecipient1Dict
from .installments import Installments, InstallmentsDict
from .line_item import LineItem, LineItemDict
from .mandate import Mandate, MandateDict
from .merchant_risk_indicator1 import MerchantRiskIndicator1, MerchantRiskIndicator1Dict
from .payment_validations2 import PaymentValidations2, PaymentValidations2Dict
from .platform_chargeback_logic import PlatformChargebackLogic, PlatformChargebackLogicDict
from .risk_data4 import RiskData4, RiskData4Dict
from .shopper_name2 import ShopperName2, ShopperName2Dict
from .shopper_tax_info2 import ShopperTaxInfo2, ShopperTaxInfo2Dict
from .split import Split, SplitDict
from .sub_merchant_info import SubMerchantInfo, SubMerchantInfoDict
from .surcharge2 import Surcharge2, Surcharge2Dict
from .third_party_token_redundancy_info1 import ThirdPartyTokenRedundancyInfo1, ThirdPartyTokenRedundancyInfo1Dict
from .three_ds2_request_fields1 import ThreeDs2RequestFields1, ThreeDs2RequestFields1Dict
from .three_dsecure_data import ThreeDsecureData, ThreeDsecureDataDict
from .unions.payment_method1 import PaymentMethod1, PaymentMethod1Dict


class PaymentRequest(SdkBaseModel):
    account_info: Optional[AccountInfo] = Field(default=UNSET, alias="accountInfo")
    """Shopper account information for 3D Secure 2.
    > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a
        frictionless flow."""

    additional_amount: Optional[Amount1] = Field(default=UNSET, alias="additionalAmount")
    """If you want a `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ request to use a non-zero value,
    assign this value to ``additionalAmount`` (while the amount must be still set to 0 to trigger BIN or card
    verification). Required to be in the same currency as the ``amount``."""

    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular payment request.

    The ``additionalData`` object consists of entries, each of which includes the key and value."""

    amount: Amount2
    """The amount information for the transaction (in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__). For `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ requests, set amount to 0
    (zero)."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    authentication_data: Optional[AuthenticationData3] = Field(default=UNSET, alias="authenticationData")
    """Data for 3DS authentication."""

    bank_account: Optional[CheckoutBankAccount1] = Field(default=UNSET, alias="bankAccount")
    """The details of the bank account, from which the payment should be made.
    > Either ``bankAccount`` or ``card`` field must be provided in a payment request."""

    billing_address: Optional[BillingAddress3] = Field(default=UNSET, alias="billingAddress")
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
    """The `delay between the authorization and automatic capture
    <https://docs.adyen.com/online-payments/capture?tab=delayed-individual_2#delayed-automatic-capture>`__ of the
    payment, specified in hours.

    Maximum value: **672** (28 days)."""

    channel: Optional[Channel2OrStr] = UNSET
    """The platform where a payment transaction takes place. This field is optional for filtering out payment methods
    that are only available on specific platforms. If this value is not set, then we will try to infer it from the
    ``sdkVersion`` or ``token``.

    Possible values:
    * iOS
    * Android
    * Web"""

    checkout_attempt_id: Optional[str] = Field(default=UNSET, alias="checkoutAttemptId")
    """Checkout attempt ID that corresponds to the Id generated by the client SDK for tracking user payment journey."""

    company: Optional[Company1] = UNSET
    """Information regarding the company."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The shopper country code.

    Format: `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ Example: NL or DE"""

    date_of_birth: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dateOfBirth")
    """The shopper's date of birth.

    Format `ISO-8601 <https://www.w3.org/TR/NOTE-datetime>`__: YYYY-MM-DD"""

    dcc_quote: Optional[ForexQuote2] = Field(default=UNSET, alias="dccQuote")
    """The forex quote as returned in the response of the forex service."""

    deliver_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliverAt")
    """The date and time the purchased goods should be delivered.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: YYYY-MM-DDThh:mm:ss.sssTZD

    Example: 2017-07-17T13:42:40.428+01:00"""

    delivery_address: Optional[DeliveryAddress1] = Field(default=UNSET, alias="deliveryAddress")
    """The address where the purchased goods should be delivered."""

    delivery_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliveryDate")
    """The date and time the purchased goods should be delivered.

    Format `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__: YYYY-MM-DDThh:mm:ss.sssTZD

    Example: 2017-07-17T13:42:40.428+01:00"""

    device_fingerprint: Optional[str] = Field(default=UNSET, alias="deviceFingerprint")
    """A string containing the shopper's device fingerprint. For more information, refer to `Device fingerprinting
    <https://docs.adyen.com/risk-management/device-fingerprinting>`__."""

    enable_one_click: Optional[bool] = Field(default=UNSET, alias="enableOneClick")
    """When true and ``shopperReference`` is provided, the shopper will be asked if the payment details should be stored
    for future `one-click payments
    <https://docs.adyen.com/get-started-with-adyen/payment-glossary/#one-click-payments-definition>`__."""

    enable_pay_out: Optional[bool] = Field(default=UNSET, alias="enablePayOut")
    """When true and ``shopperReference`` is provided, the payment details will be tokenized for payouts."""

    enable_recurring: Optional[bool] = Field(default=UNSET, alias="enableRecurring")
    """When true and ``shopperReference`` is provided, the payment details will be stored for `recurring payments
    <https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types>`__ where the shopper is not present,
    such as subscription or automatic top-up payments."""

    enhanced_scheme_data: Optional[EnhancedSchemeData3] = Field(default=UNSET, alias="enhancedSchemeData")
    """`Enhanced scheme data <https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/>`__ that may be
    required for processing the payment and/or interchange savings can apply."""

    entity_type: Optional[EntityTypeOrStr] = Field(default=UNSET, alias="entityType")
    """The type of the entity the payment is processed for."""

    fraud_offset: Optional[int] = Field(default=UNSET, alias="fraudOffset")
    """An integer value that is added to the normal fraud score. The value can be either positive or negative."""

    fund_origin: Optional[FundOrigin1] = Field(default=UNSET, alias="fundOrigin")
    """The person or entity funding the money."""

    fund_recipient: Optional[FundRecipient1] = Field(default=UNSET, alias="fundRecipient")
    """the person or entity receiving the money"""

    industry_usage: Optional[IndustryUsage1OrStr] = Field(default=UNSET, alias="industryUsage")
    """The reason for the amount update. Possible values:
    * **delayedCharge**
    * **noShow**
    * **installment**"""

    installments: Optional[Installments] = UNSET
    """Contains installment settings. For more information, refer to `Installments
    <https://docs.adyen.com/payment-methods/cards/credit-card-installments>`__."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information about the purchased items, to be included on the invoice sent to the shopper.
    > This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty."""

    localized_shopper_statement: Optional[dict[str, str]] = Field(default=UNSET, alias="localizedShopperStatement")
    """The ``localizedShopperStatement`` field lets you use dynamic values for your shopper statement in a local
    character set. If this parameter is left empty, not provided, or not applicable (in case of cross-border
    transactions), then **shopperStatement** is used.

    Currently, ``localizedShopperStatement`` is only supported for payments with Visa, Mastercard, JCB, Diners, and
    Discover.

    **Supported characters**: Hiragana, Katakana, Kanji, and alphanumeric."""

    mandate: Optional[Mandate] = UNSET
    """The mandate details to initiate recurring transaction."""

    mcc: Optional[str] = UNSET
    """The `merchant category code <https://en.wikipedia.org/wiki/Merchant_category_code>`__ (MCC) is a four-digit
    number, which relates to a particular market segment. This code reflects the predominant activity that is conducted
    by the merchant."""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    merchant_order_reference: Optional[str] = Field(default=UNSET, alias="merchantOrderReference")
    """You can use this reference to link multiple transactions to one another (for example, to track order
    authorization rate).For each billing cycle, this reference should be unique. After the first authorized payment
    attempt, do not reuse the reference. If you use this parameter, include it in all of the payment requests that you
    make.
     We strongly recommend that you:
    * Always include this parameter, so that you can benefit from linking payment requests to one another, in case of
        authorization retries.
    * Additionally include the following parameters in the ``additionalData`` object:
        https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions#request-additionalData-AdditionalDataRetry-retry-orderAttemptNumber,
        https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions#request-additionalData-AdditionalDataRetry-retry-chainAttemptNumber,
        and
        https://docs.adyen.com/api-explorer/Checkout/latest/post/sessions#request-additionalData-AdditionalDataRetry-retry-skipRetry"""

    merchant_risk_indicator: Optional[MerchantRiskIndicator1] = Field(default=UNSET, alias="merchantRiskIndicator")
    """Additional risk fields for 3D Secure 2.
    > For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a
        frictionless flow."""

    metadata: Optional[dict[str, str]] = UNSET
    """Metadata consists of entries, each of which includes a key and a value. Limits:
    * Maximum 20 key-value pairs per request. When exceeding, the "177" error occurs: "Metadata size exceeds limit".
    * Maximum 20 characters per key.
    * Maximum 80 characters per value."""

    mpi_data: Optional[ThreeDsecureData] = Field(default=UNSET, alias="mpiData")
    """Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires)."""

    order: Optional[EncryptedOrderData2] = UNSET
    """The order information required for partial payments."""

    order_reference: Optional[str] = Field(default=UNSET, alias="orderReference")
    """When you are doing multiple partial (gift card) payments, this is the ``pspReference`` of the first payment. We
    use this to link the multiple payments to each other. As your own reference for linking multiple payments, use the
    ``merchantOrderReference``instead."""

    origin: Optional[str] = UNSET
    """> Required for browser-based (``channel`` **Web**) 3D Secure 2 transactions.Set this to the origin URL of the
        page where you are rendering the Drop-in/Component. Do not include subdirectories and a trailing slash."""

    payment_method: PaymentMethod1 = Field(alias="paymentMethod")
    """The type and required details of a payment method to use."""

    payment_validations: Optional[PaymentValidations2] = Field(default=UNSET, alias="paymentValidations")
    """The object that you can use to enable payment validations for a transaction."""

    platform_chargeback_logic: Optional[PlatformChargebackLogic] = Field(default=UNSET, alias="platformChargebackLogic")
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    recurring_expiry: Optional[str] = Field(default=UNSET, alias="recurringExpiry")
    """Date after which no further authorisations shall be performed. Only for 3D Secure 2."""

    recurring_frequency: Optional[str] = Field(default=UNSET, alias="recurringFrequency")
    """Minimum number of days between authorisations. Only for 3D Secure 2."""

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

    redirect_from_issuer_method: Optional[str] = Field(default=UNSET, alias="redirectFromIssuerMethod")
    """Specifies the redirect method (GET or POST) when redirecting back from the issuer."""

    redirect_to_issuer_method: Optional[str] = Field(default=UNSET, alias="redirectToIssuerMethod")
    """Specifies the redirect method (GET or POST) when redirecting to the issuer."""

    reference: str
    """The reference to uniquely identify a payment. This reference is used in all communication with you about the
    payment status. To provide multiple references for one transaction, separate the reference values with the hyphen
    (``-``) character.We strongly recommend that you use a unique value for each transaction. Maximum length: 80
    characters."""

    return_url: str = Field(alias="returnUrl")
    """The URL to return to in case of a redirection. The format depends on the channel.
    * For web, include the protocol ``http://`` or ``https://``. You can also include your own additional query
        parameters, for example, shopper ID or order reference number.
    Example: ``https://your-company.example.com/checkout?shopperOrder=12xy``
    * For iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to the `Apple
        Developer documentation
        <https://developer.apple.com/documentation/uikit/inter-process_communication/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app>`__.
    Example: ``my-app://``
    * For Android, use a custom URL handled by an Activity on your app. You can configure it with an `intent filter
        <https://developer.android.com/guide/components/intents-filters>`__.
    Example: ``my-app://your.package.name``

    If the URL to return to includes non-ASCII characters, like spaces or special letters, URL encode the value.
    > The URL must not include personally identifiable information (PII), for example name or email address."""

    risk_data: Optional[RiskData4] = Field(default=UNSET, alias="riskData")
    """Contains risk data, such as client-side data, used to identify risk for a transaction."""

    session_validity: Optional[str] = Field(default=UNSET, alias="sessionValidity")
    """The date and time until when the session remains valid, in `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__
    format.

    For example: 2020-07-18T15:42:40.428+01:00"""

    shopper_conversion_id: Optional[str] = Field(default=UNSET, alias="shopperConversionId")
    """A unique ID to `connect the shopper to a single checkout session
    <https://docs.adyen.com/online-payments/checkout-settings#checkout-shopper-conversion-id>`__ that uses multiple API
    requests. You can use this to get insights into conversion rates."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper's email address, in valid `RFC-5322 <https://www.rfc-editor.org/rfc/rfc5322>`__ format. We recommend
    that you provide this data, because it is used in velocity fraud checks. > Required for Visa and JCB transactions
    that require 3D Secure 2 authentication if you did not include the ``telephoneNumber``."""

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

    shopper_name: Optional[ShopperName2] = Field(default=UNSET, alias="shopperName")
    """The shopper's full name."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. Minimum length: 3 characters.
    > Your reference must not include personally identifiable information (PII), for example name or email address."""

    shopper_statement: Optional[str] = Field(default=UNSET, alias="shopperStatement")
    """The text to be shown on the shopper's bank statement.
     We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.
     Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**."""

    shopper_tax_info: Optional[ShopperTaxInfo2] = Field(default=UNSET, alias="shopperTaxInfo")
    """The tax info of the shopper"""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """The shopper's social security number."""

    splits: Optional[list[Split]] = UNSET
    """An array of objects specifying how to split a payment when using `Adyen for Platforms
    <https://docs.adyen.com/platforms/process-payments#providing-split-information>`__, `Classic Platforms integration
    <https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information>`__, or `Issuing
    <https://docs.adyen.com/issuing/manage-funds#split>`__."""

    store: Optional[str] = UNSET
    """Required for Adyen for Platforms integrations if you are a platform model. This is your `reference
    <https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId>`__/stores#request-reference) (on
    `balance platform <https://docs.adyen.com/platforms>`__) or the `storeReference
    <https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference>`__
    (in the `classic integration
    <https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store>`__)
    for the ecommerce or point-of-sale store that is processing the payment."""

    store_payment_method: Optional[bool] = Field(default=UNSET, alias="storePaymentMethod")
    """When true and ``shopperReference`` is provided, the payment details will be stored for future `recurring payments
    <https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types>`__."""

    sub_merchants: Optional[list[SubMerchantInfo]] = Field(default=UNSET, alias="subMerchants")
    """This field contains additional information on the submerchant, who is onboarded to an acquirer through a payment
    facilitator or aggregator"""

    surcharge: Optional[Surcharge2] = UNSET
    """The `surcharge <https://docs.adyen.com/online-payments/surcharge/>`__ amount to apply to the transaction, in
    `minor units <https://docs.adyen.com/development-resources/currency-codes>`__. When you apply surcharge, include the
    surcharge in the ``amount.value`` field.

    Review our `Surcharge compliance guide <https://docs.adyen.com/development-resources/surcharge-compliance/>`__ to
    learn about how to comply with regulatory requirements when applying surcharge."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's telephone number.
     The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15
        digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``."""

    third_party_token_redundancy_info: Optional[ThirdPartyTokenRedundancyInfo1] = Field(
        default=UNSET, alias="thirdPartyTokenRedundancyInfo"
    )
    """Configuration for creating redundant payment tokens with third-party token vaults using the Adyen Forward API.
    This feature requires Forward API webhook integration and pre-configured templates in your Adyen account. Contact
    your Adyen account manager for setup and availability."""

    three_ds2_request_data: Optional[ThreeDs2RequestFields1] = Field(default=UNSET, alias="threeDS2RequestData")
    """Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer
    to `Online payments <https://docs.adyen.com/online-payments>`__ or `Classic integration
    <https://docs.adyen.com/classic-integration>`__ documentation."""

    three_ds_authentication_only: Optional[bool] = Field(default=UNSET, alias="threeDSAuthenticationOnly")
    """Required to trigger the `authentication-only flow
    <https://docs.adyen.com/online-payments/3d-secure/authentication-only/>`__. If set to **true**, you will only
    perform the 3D Secure 2 authentication, and will not proceed to the payment authorisation.Default: **false**."""

    trusted_shopper: Optional[bool] = Field(default=UNSET, alias="trustedShopper")
    """Set to true if the payment should be routed to a trusted MID."""


class PaymentRequestDict(TypedDict):
    account_info: NotRequired[AccountInfo | AccountInfoDict]
    additional_amount: NotRequired[Amount1 | Amount1Dict]
    additional_data: NotRequired[dict[str, str]]
    amount: Amount2 | Amount2Dict
    application_info: NotRequired[ApplicationInfo | ApplicationInfoDict]
    authentication_data: NotRequired[AuthenticationData3 | AuthenticationData3Dict]
    bank_account: NotRequired[CheckoutBankAccount1 | CheckoutBankAccount1Dict]
    billing_address: NotRequired[BillingAddress3 | BillingAddress3Dict]
    browser_info: NotRequired[BrowserInfo | BrowserInfoDict]
    capture_delay_hours: NotRequired[int]
    channel: NotRequired[Channel2OrStr]
    checkout_attempt_id: NotRequired[str]
    company: NotRequired[Company1 | Company1Dict]
    country_code: NotRequired[str]
    date_of_birth: NotRequired[RFC3339DateTime]
    dcc_quote: NotRequired[ForexQuote2 | ForexQuote2Dict]
    deliver_at: NotRequired[RFC3339DateTime]
    delivery_address: NotRequired[DeliveryAddress1 | DeliveryAddress1Dict]
    delivery_date: NotRequired[RFC3339DateTime]
    device_fingerprint: NotRequired[str]
    enable_one_click: NotRequired[bool]
    enable_pay_out: NotRequired[bool]
    enable_recurring: NotRequired[bool]
    enhanced_scheme_data: NotRequired[EnhancedSchemeData3 | EnhancedSchemeData3Dict]
    entity_type: NotRequired[EntityTypeOrStr]
    fraud_offset: NotRequired[int]
    fund_origin: NotRequired[FundOrigin1 | FundOrigin1Dict]
    fund_recipient: NotRequired[FundRecipient1 | FundRecipient1Dict]
    industry_usage: NotRequired[IndustryUsage1OrStr]
    installments: NotRequired[Installments | InstallmentsDict]
    line_items: NotRequired[list[LineItem | LineItemDict]]
    localized_shopper_statement: NotRequired[dict[str, str]]
    mandate: NotRequired[Mandate | MandateDict]
    mcc: NotRequired[str]
    merchant_account: str
    merchant_order_reference: NotRequired[str]
    merchant_risk_indicator: NotRequired[MerchantRiskIndicator1 | MerchantRiskIndicator1Dict]
    metadata: NotRequired[dict[str, str]]
    mpi_data: NotRequired[ThreeDsecureData | ThreeDsecureDataDict]
    order: NotRequired[EncryptedOrderData2 | EncryptedOrderData2Dict]
    order_reference: NotRequired[str]
    origin: NotRequired[str]
    payment_method: PaymentMethod1 | PaymentMethod1Dict
    payment_validations: NotRequired[PaymentValidations2 | PaymentValidations2Dict]
    platform_chargeback_logic: NotRequired[PlatformChargebackLogic | PlatformChargebackLogicDict]
    recurring_expiry: NotRequired[str]
    recurring_frequency: NotRequired[str]
    recurring_processing_model: NotRequired[RecurringProcessingModelOrStr]
    redirect_from_issuer_method: NotRequired[str]
    redirect_to_issuer_method: NotRequired[str]
    reference: str
    return_url: str
    risk_data: NotRequired[RiskData4 | RiskData4Dict]
    session_validity: NotRequired[str]
    shopper_conversion_id: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_ip: NotRequired[str]
    shopper_interaction: NotRequired[ShopperInteractionOrStr]
    shopper_locale: NotRequired[str]
    shopper_name: NotRequired[ShopperName2 | ShopperName2Dict]
    shopper_reference: NotRequired[str]
    shopper_statement: NotRequired[str]
    shopper_tax_info: NotRequired[ShopperTaxInfo2 | ShopperTaxInfo2Dict]
    social_security_number: NotRequired[str]
    splits: NotRequired[list[Split | SplitDict]]
    store: NotRequired[str]
    store_payment_method: NotRequired[bool]
    sub_merchants: NotRequired[list[SubMerchantInfo | SubMerchantInfoDict]]
    surcharge: NotRequired[Surcharge2 | Surcharge2Dict]
    telephone_number: NotRequired[str]
    third_party_token_redundancy_info: NotRequired[ThirdPartyTokenRedundancyInfo1 | ThirdPartyTokenRedundancyInfo1Dict]
    three_ds2_request_data: NotRequired[ThreeDs2RequestFields1 | ThreeDs2RequestFields1Dict]
    three_ds_authentication_only: NotRequired[bool]
    trusted_shopper: NotRequired[bool]
