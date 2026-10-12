from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .amount2 import Amount2, Amount2Dict
from .browser_info import BrowserInfo, BrowserInfoDict
from .encrypted_order_data2 import EncryptedOrderData2, EncryptedOrderData2Dict
from .enums.channel3 import Channel3OrStr
from .enums.store_filtration_mode2 import StoreFiltrationMode2OrStr


class PaymentMethodsRequest(SdkBaseModel):
    additional_data: Optional[dict[str, str]] = Field(default=UNSET, alias="additionalData")
    """This field contains additional data, which may be required for a particular payment request.

    The ``additionalData`` object consists of entries, each of which includes the key and value."""

    allowed_payment_methods: Optional[list[str]] = Field(default=UNSET, alias="allowedPaymentMethods")
    """List of payment methods to be presented to the shopper. To refer to payment methods, use their `payment method
    type <https://docs.adyen.com/payment-methods/payment-method-types>`__.

    Example: ``"allowedPaymentMethods":["ideal","applepay"]``"""

    amount: Optional[Amount2] = UNSET
    """The amount information for the transaction (in `minor units
    <https://docs.adyen.com/development-resources/currency-codes>`__). For `BIN or card verification
    <https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification>`__ requests, set amount to 0
    (zero)."""

    blocked_payment_methods: Optional[list[str]] = Field(default=UNSET, alias="blockedPaymentMethods")
    """List of payment methods to be hidden from the shopper. To refer to payment methods, use their `payment method
    type <https://docs.adyen.com/payment-methods/payment-method-types>`__.

    Example: ``"blockedPaymentMethods":["ideal","applepay"]``"""

    browser_info: Optional[BrowserInfo] = Field(default=UNSET, alias="browserInfo")
    """The shopper's browser information.
    > For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the
        ``userAgent`` and ``acceptHeader`` fields to indicate that your integration can support a redirect in case a
        payment is routed to 3D Secure 2 redirect."""

    channel: Optional[Channel3OrStr] = UNSET
    """The platform where a payment transaction takes place. This field can be used for filtering out payment methods
    that are only available on specific platforms. Possible values:
    * iOS
    * Android
    * Web"""

    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    """The shopper country code.

    Format: `ISO 3166-1 alpha-2 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__ Example: NL or DE"""

    merchant_account: str = Field(alias="merchantAccount")
    """The merchant account identifier, with which you want to process the transaction."""

    order: Optional[EncryptedOrderData2] = UNSET
    """The order information required for partial payments."""

    shopper_conversion_id: Optional[str] = Field(default=UNSET, alias="shopperConversionId")
    """A unique ID to `connect the shopper to a single checkout session
    <https://docs.adyen.com/online-payments/checkout-settings#checkout-shopper-conversion-id>`__ that uses multiple API
    requests. You can use this to get insights into conversion rates."""

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

    shopper_locale: Optional[str] = Field(default=UNSET, alias="shopperLocale")
    """The language for the payment. The value combines the two-letter `ISO 639-1
    <https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes>`__ language code with the `ISO 3166-1 alpha-2
    <https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes>`__ country code. For example, **nl-NL**.

    When using Drop-in/Components, the specified language appears if your front-end global configuration does not set
    the ``locale``."""

    shopper_reference: Optional[str] = Field(default=UNSET, alias="shopperReference")
    """Required for recurring payments. Your reference to uniquely identify this shopper, for example user ID or account
    ID. The value is case-sensitive and must be at least three characters.
    > Your reference must not include personally identifiable information (PII) such as name or email address."""

    split_card_funding_sources: bool = Field(default=False, alias="splitCardFundingSources")
    """Boolean value indicating whether the card payment method should be split into separate debit and credit
    options."""

    store: Optional[str] = UNSET
    """Required for Adyen for Platforms integrations if you are a platform model. This is your `reference
    <https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId>`__/stores#request-reference) (on
    `balance platform <https://docs.adyen.com/platforms>`__) or the `storeReference
    <https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference>`__
    (in the `classic integration
    <https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store>`__)
    for the ecommerce or point-of-sale store that is processing the payment."""

    store_filtration_mode: Optional[StoreFiltrationMode2OrStr] = Field(default=UNSET, alias="storeFiltrationMode")
    """Specifies how payment methods should be filtered based on the ``store`` parameter:
      - **exclusive**: Only payment methods belonging to the specified ``store`` are returned.
      - **inclusive**: Payment methods from the ``store`` and those not associated with any other store are returned."""

    telephone_number: Optional[str] = Field(default=UNSET, alias="telephoneNumber")
    """The shopper's telephone number.
     The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15
        digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.
    > Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the
        ``shopperEmail``."""


class PaymentMethodsRequestDict(TypedDict):
    additional_data: NotRequired[dict[str, str]]
    allowed_payment_methods: NotRequired[list[str]]
    amount: NotRequired[Amount2Dict]
    blocked_payment_methods: NotRequired[list[str]]
    browser_info: NotRequired[BrowserInfoDict]
    channel: NotRequired[Channel3OrStr]
    country_code: NotRequired[str]
    merchant_account: str
    order: NotRequired[EncryptedOrderData2Dict]
    shopper_conversion_id: NotRequired[str]
    shopper_email: NotRequired[str]
    shopper_ip: NotRequired[str]
    shopper_locale: NotRequired[str]
    shopper_reference: NotRequired[str]
    split_card_funding_sources: NotRequired[bool]
    store: NotRequired[str]
    store_filtration_mode: NotRequired[StoreFiltrationMode2OrStr]
    telephone_number: NotRequired[str]
