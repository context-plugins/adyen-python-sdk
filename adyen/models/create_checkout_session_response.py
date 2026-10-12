from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .account_info import AccountInfo, AccountInfoDict
from .amount1 import Amount1, Amount1Dict
from .amount18 import Amount18, Amount18Dict
from .application_info import ApplicationInfo, ApplicationInfoDict
from .authentication_data1 import AuthenticationData1, AuthenticationData1Dict
from .billing_address1 import BillingAddress1, BillingAddress1Dict
from .checkout_session_installment_option import CheckoutSessionInstallmentOption, CheckoutSessionInstallmentOptionDict
from .checkout_session_three_ds2_request_data1 import (
    CheckoutSessionThreeDs2RequestData1,
    CheckoutSessionThreeDs2RequestData1Dict,
)
from .company1 import Company1, Company1Dict
from .delivery_address1 import DeliveryAddress1, DeliveryAddress1Dict
from .enums.channel import ChannelOrStr
from .enums.mode import Mode, ModeOrStr
from .enums.recurring_processing_model1 import RecurringProcessingModel1OrStr
from .enums.shopper_interaction import ShopperInteractionOrStr
from .enums.store_filtration_mode import StoreFiltrationModeOrStr
from .enums.store_payment_method_mode import StorePaymentMethodModeOrStr
from .fund_origin1 import FundOrigin1, FundOrigin1Dict
from .fund_recipient1 import FundRecipient1, FundRecipient1Dict
from .line_item import LineItem, LineItemDict
from .mandate import Mandate, MandateDict
from .platform_chargeback_logic import PlatformChargebackLogic, PlatformChargebackLogicDict
from .risk_data1 import RiskData1, RiskData1Dict
from .shopper_name1 import ShopperName1, ShopperName1Dict
from .split import Split, SplitDict
from .third_party_token_redundancy_info1 import ThirdPartyTokenRedundancyInfo1, ThirdPartyTokenRedundancyInfo1Dict
from .three_dsecure_data import ThreeDsecureData, ThreeDsecureDataDict


class CreateCheckoutSessionResponse(SdkBaseModel):
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

    allowed_payment_methods: Optional[list[str]] = Field(default=UNSET, alias="allowedPaymentMethods")
    """List of payment methods to be presented to the shopper. To refer to payment methods, use their `payment method
    type <https://docs.adyen.com/payment-methods/payment-method-types>`__.

    Example: ``"allowedPaymentMethods":["ideal","applepay"]``"""

    amount: Amount18
    """The amount of the payment."""

    application_info: Optional[ApplicationInfo] = Field(default=UNSET, alias="applicationInfo")
    """Information about your application. For more details, see `Building Adyen solutions
    <https://docs.adyen.com/development-resources/building-adyen-solutions>`__."""

    authentication_data: Optional[AuthenticationData1] = Field(default=UNSET, alias="authenticationData")
    """Configuration data for 3DS payments."""

    billing_address: Optional[BillingAddress1] = Field(default=UNSET, alias="billingAddress")
    """The address where to send the invoice."""

    blocked_payment_methods: Optional[list[str]] = Field(default=UNSET, alias="blockedPaymentMethods")
    """List of payment methods to be hidden from the shopper. To refer to payment methods, use their `payment method
    type <https://docs.adyen.com/payment-methods/payment-method-types>`__.

    Example: ``"blockedPaymentMethods":["ideal","applepay"]``"""

    capture_delay_hours: Optional[int] = Field(default=UNSET, alias="captureDelayHours")
    """The delay between the authorisation and scheduled auto-capture, specified in hours."""

    channel: Optional[ChannelOrStr] = UNSET
    """The platform where a payment transaction takes place. This field is optional for filtering out payment methods
    that are only available on specific platforms. If this value is not set, then we will try to infer it from the
    ``sdkVersion`` or ``token``.

    Possible values:
    * **iOS**
    * **Android**
    * **Web**"""

    company: Optional[Company1] = UNSET
    """Information regarding the company."""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The shopper's two-letter country code."""

    date_of_birth: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dateOfBirth")
    """The shopper's date of birth in `ISO8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`__ format."""

    deliver_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="deliverAt")
    """The date and time when the purchased goods should be delivered.

    `ISO 8601 <https://www.w3.org/TR/NOTE-datetime>`__ format: YYYY-MM-DDThh:mm:ss+TZD, for example,
    **2020-12-18T10:15:30+01:00**."""

    delivery_address: Optional[DeliveryAddress1] = Field(default=UNSET, alias="deliveryAddress")
    """The address where the purchased goods should be delivered."""

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

    expires_at: RFC3339DateTime = Field(alias="expiresAt")
    """The date the session expires in `ISO8601 <https://www.iso.org/iso-8601-date-and-time-format.html>`__ format. When
    not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more
    than 24 hours after session creation."""

    fund_origin: Optional[FundOrigin1] = Field(default=UNSET, alias="fundOrigin")
    """The person or entity funding the money."""

    fund_recipient: Optional[FundRecipient1] = Field(default=UNSET, alias="fundRecipient")
    """the person or entity receiving the money"""

    id: str
    """A unique identifier of the session."""

    installment_options: Optional[dict[str, CheckoutSessionInstallmentOption]] = Field(
        default=UNSET, alias="installmentOptions"
    )
    """A set of key-value pairs that specifies the installment options available per payment method. The key must be a
    payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or
    **mc**. The value must be an object containing the installment options."""

    line_items: Optional[list[LineItem]] = Field(default=UNSET, alias="lineItems")
    """Price and product information about the purchased items, to be included on the invoice sent to the shopper.
    > This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty."""

    mandate: Optional[Mandate] = UNSET
    """The mandate details to initiate recurring transaction."""

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

    metadata: Optional[dict[str, str]] = UNSET
    """Metadata consists of entries, each of which includes a key and a value. Limits:
    * Maximum 20 key-value pairs per request.
    * Maximum 20 characters per key.
    * Maximum 80 characters per value."""

    mode: ModeOrStr = Mode.EMBEDDED
    """Indicates the type of front end integration. Possible values:
    * **embedded** (default): Drop-in or Components integration
    * **hosted**: Hosted Checkout integration"""

    mpi_data: Optional[ThreeDsecureData] = Field(default=UNSET, alias="mpiData")
    """Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires)."""

    platform_chargeback_logic: Optional[PlatformChargebackLogic] = Field(default=UNSET, alias="platformChargebackLogic")
    """Defines how to book chargebacks when using `Adyen for Platforms
    <https://docs.adyen.com/adyen-for-platforms-model>`__."""

    recurring_expiry: Optional[str] = Field(default=UNSET, alias="recurringExpiry")
    """Date after which no further authorisations shall be performed. Only for 3D Secure 2."""

    recurring_frequency: Optional[str] = Field(default=UNSET, alias="recurringFrequency")
    """Minimum number of days between authorisations. Only for 3D Secure 2."""

    recurring_processing_model: Optional[RecurringProcessingModel1OrStr] = Field(
        default=UNSET, alias="recurringProcessingModel"
    )
    """Defines a recurring payment type. Required when creating a token to store payment details. Allowed values:
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
    """The reference to uniquely identify a payment."""

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

    risk_data: Optional[RiskData1] = Field(default=UNSET, alias="riskData")
    """Any risk-related settings to apply to the payment."""

    session_data: Optional[str] = Field(default=UNSET, alias="sessionData")
    """The payment session data you need to pass to your front end."""

    shopper_email: Optional[str] = Field(default=UNSET, alias="shopperEmail")
    """The shopper's email address."""

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

    shopper_name: Optional[ShopperName1] = Field(default=UNSET, alias="shopperName")
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

    show_installment_amount: Optional[bool] = Field(default=UNSET, alias="showInstallmentAmount")
    """Set to true to show the payment amount per installment."""

    show_remove_payment_method_button: Optional[bool] = Field(default=UNSET, alias="showRemovePaymentMethodButton")
    """Set to **true** to show a button that lets the shopper remove a stored payment method."""

    social_security_number: Optional[str] = Field(default=UNSET, alias="socialSecurityNumber")
    """The shopper's social security number."""

    split_card_funding_sources: bool = Field(default=False, alias="splitCardFundingSources")
    """Boolean value indicating whether the card payment method should be split into separate debit and credit
    options."""

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

    store_filtration_mode: Optional[StoreFiltrationModeOrStr] = Field(default=UNSET, alias="storeFiltrationMode")
    """Specifies how payment methods should be filtered based on the 'store' parameter:
      - 'exclusive': Only payment methods belonging to the specified 'store' are returned.
      - 'inclusive': Payment methods from the 'store' and those not associated with any other store are returned."""

    store_payment_method: Optional[bool] = Field(default=UNSET, alias="storePaymentMethod")
    """When true and ``shopperReference`` is provided, the payment details will be stored for future `recurring payments
    <https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types>`__."""

    store_payment_method_mode: Optional[StorePaymentMethodModeOrStr] = Field(
        default=UNSET, alias="storePaymentMethodMode"
    )
    """Indicates if the details of the payment method will be stored for the shopper. Possible values:
    * **disabled** – No details will be stored (default).
    * **askForConsent** – If the ``shopperReference`` is provided, the Drop-in/Component shows a checkbox where the
        shopper can select to store their payment details for card payments.
    * **enabled** – If the ``shopperReference`` is provided, the details will be stored without asking the shopper for
        consent."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's telephone number.
     The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15
        digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``."""

    theme_id: Optional[str] = Field(default=UNSET, alias="themeId")
    """Sets a custom theme for `Hosted Checkout
    <https://docs.adyen.com/online-payments/build-your-integration/?platform=Web&integration=Hosted+Checkout>`__. The
    value can be any of the **Theme ID** values from your Customer Area."""

    third_party_token_redundancy_info: Optional[ThirdPartyTokenRedundancyInfo1] = Field(
        default=UNSET, alias="thirdPartyTokenRedundancyInfo"
    )
    """Configuration for creating redundant payment tokens with third-party token vaults using the Adyen Forward API.
    This feature requires Forward API webhook integration and pre-configured templates in your Adyen account. Contact
    your Adyen account manager for setup and availability."""

    three_ds2_request_data: Optional[CheckoutSessionThreeDs2RequestData1] = Field(
        default=UNSET, alias="threeDS2RequestData"
    )
    """Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer
    to `Online payments <https://docs.adyen.com/online-payments>`__."""

    three_ds_authentication_only: bool = Field(default=False, alias="threeDSAuthenticationOnly")
    """Required to trigger the `authentication-only flow
    <https://docs.adyen.com/online-payments/3d-secure/authentication-only/>`__. If set to **true**, you will only
    perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**."""

    trusted_shopper: Optional[bool] = Field(default=UNSET, alias="trustedShopper")
    """Set to true if the payment should be routed to a trusted MID."""

    url: Optional[str] = UNSET
    """The URL for the Hosted Checkout page. Redirect the shopper to this URL so they can make the payment."""


class CreateCheckoutSessionResponseDict(TypedDict):
    account_info: NotRequired[AccountInfoDict]
    additional_amount: NotRequired[Amount1Dict]
    additional_data: NotRequired[dict[str, str]]
    allowed_payment_methods: NotRequired[list[str]]
    amount: Amount18Dict
    application_info: NotRequired[ApplicationInfoDict]
    authentication_data: NotRequired[AuthenticationData1Dict]
    billing_address: NotRequired[BillingAddress1Dict]
    blocked_payment_methods: NotRequired[list[str]]
    capture_delay_hours: NotRequired[int]
    channel: NotRequired[ChannelOrStr]
    company: NotRequired[Company1Dict]
    country_code: NotRequired[str]
    date_of_birth: NotRequired[RFC3339DateTime]
    deliver_at: NotRequired[RFC3339DateTime]
    delivery_address: NotRequired[DeliveryAddress1Dict]
    enable_one_click: NotRequired[bool]
    enable_pay_out: NotRequired[bool]
    enable_recurring: NotRequired[bool]
    expires_at: RFC3339DateTime
    fund_origin: NotRequired[FundOrigin1Dict]
    fund_recipient: NotRequired[FundRecipient1Dict]
    id: str
    installment_options: NotRequired[dict[str, CheckoutSessionInstallmentOptionDict]]
    line_items: NotRequired[list[LineItemDict]]
    mandate: NotRequired[MandateDict]
    mcc: NotRequired[str]
    merchant_account: str
    merchant_order_reference: NotRequired[str]
    metadata: NotRequired[dict[str, str]]
    mode: NotRequired[ModeOrStr]
    mpi_data: NotRequired[ThreeDsecureDataDict]
    platform_chargeback_logic: NotRequired[PlatformChargebackLogicDict]
    recurring_expiry: NotRequired[str]
    recurring_frequency: NotRequired[str]
    recurring_processing_model: NotRequired[RecurringProcessingModel1OrStr]
    redirect_from_issuer_method: NotRequired[str]
    redirect_to_issuer_method: NotRequired[str]
    reference: str
    return_url: str
    risk_data: NotRequired[RiskData1Dict]
    session_data: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_ip: NotRequired[str]
    shopper_interaction: NotRequired[ShopperInteractionOrStr]
    shopper_locale: NotRequired[str]
    shopper_name: NotRequired[ShopperName1Dict]
    shopper_reference: NotRequired[str]
    shopper_statement: NotRequired[str]
    show_installment_amount: NotRequired[bool]
    show_remove_payment_method_button: NotRequired[bool]
    social_security_number: NotRequired[str]
    split_card_funding_sources: NotRequired[bool]
    splits: NotRequired[list[SplitDict]]
    store: NotRequired[str]
    store_filtration_mode: NotRequired[StoreFiltrationModeOrStr]
    store_payment_method: NotRequired[bool]
    store_payment_method_mode: NotRequired[StorePaymentMethodModeOrStr]
    telephone_number: NotRequired[str]
    theme_id: NotRequired[str]
    third_party_token_redundancy_info: NotRequired[ThirdPartyTokenRedundancyInfo1Dict]
    three_ds2_request_data: NotRequired[CheckoutSessionThreeDs2RequestData1Dict]
    three_ds_authentication_only: NotRequired[bool]
    trusted_shopper: NotRequired[bool]
    url: NotRequired[str]
