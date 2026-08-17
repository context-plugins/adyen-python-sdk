
# Create Checkout Session Response

## Structure

`CreateCheckoutSessionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_info` | [`AccountInfo`](../../doc/models/account-info.md) | Optional | Shopper account information for 3D Secure 2.<br><br>> For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow. |
| `additional_amount` | [`Amount1`](../../doc/models/amount-1.md) | Optional | If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to `additionalAmount` (while the amount must be still set to 0 to trigger BIN or card verification).<br>Required to be in the same currency as the `amount`. |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular payment request.<br><br>The `additionalData` object consists of entries, each of which includes the key and value. |
| `allowed_payment_methods` | `List[str]` | Optional | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).<br><br>Example: `"allowedPaymentMethods":["ideal","applepay"]` |
| `amount` | [`Amount18`](../../doc/models/amount-18.md) | Required | The amount of the payment. |
| `application_info` | [`ApplicationInfo`](../../doc/models/application-info.md) | Optional | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
| `authentication_data` | [`AuthenticationData1`](../../doc/models/authentication-data-1.md) | Optional | Configuration data for 3DS payments. |
| `billing_address` | [`BillingAddress1`](../../doc/models/billing-address-1.md) | Optional | The address where to send the invoice. |
| `blocked_payment_methods` | `List[str]` | Optional | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).<br><br>Example: `"blockedPaymentMethods":["ideal","applepay"]` |
| `capture_delay_hours` | `int` | Optional | The delay between the authorisation and scheduled auto-capture, specified in hours. |
| `channel` | [`ChannelEnum`](../../doc/models/channel-enum.md) | Optional | The platform where a payment transaction takes place. This field is optional for filtering out payment methods that are only available on specific platforms. If this value is not set, then we will try to infer it from the `sdkVersion` or `token`.<br><br>Possible values:<br><br>* **iOS**<br>* **Android**<br>* **Web** |
| `company` | [`Company1`](../../doc/models/company-1.md) | Optional | Information regarding the company. |
| `country_code` | `str` | Optional | The shopper's two-letter country code. |
| `date_of_birth` | `datetime` | Optional | The shopper's date of birth in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |
| `deliver_at` | `datetime` | Optional | The date and time when the purchased goods should be delivered.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. |
| `delivery_address` | [`DeliveryAddress1`](../../doc/models/delivery-address-1.md) | Optional | The address where the purchased goods should be delivered. |
| `enable_one_click` | `bool` | Optional | When true and `shopperReference` is provided, the shopper will be asked if the payment details should be stored for future [one-click payments](https://docs.adyen.com/get-started-with-adyen/payment-glossary/#one-click-payments-definition). |
| `enable_pay_out` | `bool` | Optional | When true and `shopperReference` is provided, the payment details will be tokenized for payouts. |
| `enable_recurring` | `bool` | Optional | When true and `shopperReference` is provided, the payment details will be stored for [recurring payments](https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types) where the shopper is not present, such as subscription or automatic top-up payments. |
| `expires_at` | `datetime` | Required | The date the session expires in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. When not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more than 24 hours after session creation. |
| `fund_origin` | [`FundOrigin1`](../../doc/models/fund-origin-1.md) | Optional | The person or entity funding the money. |
| `fund_recipient` | [`FundRecipient1`](../../doc/models/fund-recipient-1.md) | Optional | the person or entity receiving the money |
| `id` | `str` | Required, Read-only | A unique identifier of the session. |
| `installment_options` | [`Dict[str, CheckoutSessionInstallmentOption]`](../../doc/models/checkout-session-installment-option.md) | Optional | A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or **mc**. The value must be an object containing the installment options. |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information about the purchased items, to be included on the invoice sent to the shopper.<br><br>> This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty. |
| `mandate` | [`Mandate`](../../doc/models/mandate.md) | Optional | The mandate details to initiate recurring transaction. |
| `mcc` | `str` | Optional | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `merchant_order_reference` | `str` | Optional | This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle.<br>The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations.<br><br>> We strongly recommend you send the `merchantOrderReference` value to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provide `retry.orderAttemptNumber`, `retry.chainAttemptNumber`, and `retry.skipRetry` values in `PaymentRequest.additionalData`. |
| `metadata` | `Dict[str, str]` | Optional | Metadata consists of entries, each of which includes a key and a value.<br>Limits:<br><br>* Maximum 20 key-value pairs per request.<br>* Maximum 20 characters per key.<br>* Maximum 80 characters per value. |
| `mode` | [`ModeEnum`](../../doc/models/mode-enum.md) | Optional | Indicates the type of front end integration. Possible values:<br><br>* **embedded** (default): Drop-in or Components integration<br>* **hosted**: Hosted Checkout integration<br><br>**Default**: `"embedded"` |
| `mpi_data` | [`ThreeDSecureData`](../../doc/models/three-d-secure-data.md) | Optional | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `recurring_expiry` | `str` | Optional | Date after which no further authorisations shall be performed. Only for 3D Secure 2. |
| `recurring_frequency` | `str` | Optional | Minimum number of days between authorisations. Only for 3D Secure 2. |
| `recurring_processing_model` | [`RecurringProcessingModel1Enum`](../../doc/models/recurring-processing-model-1-enum.md) | Optional | Defines a recurring payment type. Required when creating a token to store payment details.<br>Allowed values:<br><br>* `Subscription` – A transaction for a fixed or variable amount, which follows a fixed schedule.<br>* `CardOnFile` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.<br>* `UnscheduledCardOnFile` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount. |
| `redirect_from_issuer_method` | `str` | Optional | Specifies the redirect method (GET or POST) when redirecting back from the issuer. |
| `redirect_to_issuer_method` | `str` | Optional | Specifies the redirect method (GET or POST) when redirecting to the issuer. |
| `reference` | `str` | Required | The reference to uniquely identify a payment. |
| `return_url` | `str` | Required | The URL to return to in case of a redirection.<br>The format depends on the channel.<br><br>* For web, include the protocol `http://` or `https://`. You can also include your own additional query parameters, for example, shopper ID or order reference number.<br>  Example: `https://your-company.example.com/checkout?shopperOrder=12xy`<br>* For iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to the [Apple Developer documentation](https://developer.apple.com/documentation/uikit/inter-process_communication/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app).<br>  Example: `my-app://`<br>* For Android, use a custom URL handled by an Activity on your app. You can configure it with an [intent filter](https://developer.android.com/guide/components/intents-filters).<br>  Example: `my-app://your.package.name`<br><br>If the URL to return to includes non-ASCII characters, like spaces or special letters, URL encode the value.<br><br>> The URL must not include personally identifiable information (PII), for example name or email address.<br><br>**Constraints**: *Maximum Length*: `1024` |
| `risk_data` | [`RiskData1`](../../doc/models/risk-data-1.md) | Optional | Any risk-related settings to apply to the payment. |
| `session_data` | `str` | Optional | The payment session data you need to pass to your front end. |
| `shopper_email` | `str` | Optional | The shopper's email address. |
| `shopper_ip` | `str` | Optional | The shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks).<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile integrations, if you did not include the `shopperEmail`. For native mobile integrations, the field is required to support cases where authentication is routed to the redirect flow. This field is also mandatory for some merchants depending on your business model. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). |
| `shopper_interaction` | [`ShopperInteractionEnum`](../../doc/models/shopper-interaction-enum.md) | Optional | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.<br>For the web service API, Adyen assumes Ecommerce shopper interaction by default.<br><br>This field has the following possible values:<br><br>* `Ecommerce` - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.<br>* `ContAuth` - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).<br>* `Moto` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.<br>* `POS` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |
| `shopper_locale` | `str` | Optional | The language for the payment. The value combines the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) language code with the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) country code. For example, **nl-NL**.<br><br>When using Drop-in/Components, the specified language appears if your front-end global configuration does not set the `locale`. |
| `shopper_name` | [`ShopperName1`](../../doc/models/shopper-name-1.md) | Optional | The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program. |
| `shopper_reference` | `str` | Optional | Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `256` |
| `shopper_statement` | `str` | Optional | The text to be shown on the shopper's bank statement.<br>We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.<br>Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**. |
| `show_installment_amount` | `bool` | Optional | Set to true to show the payment amount per installment. |
| `show_remove_payment_method_button` | `bool` | Optional | Set to **true** to show a button that lets the shopper remove a stored payment method. |
| `social_security_number` | `str` | Optional | The shopper's social security number. |
| `split_card_funding_sources` | `bool` | Optional | Boolean value indicating whether the card payment method should be split into separate debit and credit options.<br><br>**Default**: `False` |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/platforms/process-payments#providing-split-information), [Classic Platforms integration](https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information), or [Issuing](https://docs.adyen.com/issuing/manage-funds#split). |
| `store` | `str` | Optional | Required for Adyen for Platforms integrations if you are a platform model. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/platforms)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment. |
| `store_filtration_mode` | [`StoreFiltrationModeEnum`](../../doc/models/store-filtration-mode-enum.md) | Optional | Specifies how payment methods should be filtered based on the 'store' parameter:<br><br>- 'exclusive': Only payment methods belonging to the specified 'store' are returned.<br>- 'inclusive': Payment methods from the 'store' and those not associated with any other store are returned. |
| `store_payment_method` | `bool` | Optional | When true and `shopperReference` is provided, the payment details will be stored for future [recurring payments](https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types). |
| `store_payment_method_mode` | [`StorePaymentMethodModeEnum`](../../doc/models/store-payment-method-mode-enum.md) | Optional | Indicates if the details of the payment method will be stored for the shopper. Possible values:<br><br>* **disabled** – No details will be stored (default).<br>* **askForConsent** – If the `shopperReference` is provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.<br>* **enabled** – If the `shopperReference` is provided, the details will be stored without asking the shopper for consent. |
| `telephone_number` | `str` | Optional | The shopper's telephone number.<br>The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`. |
| `theme_id` | `str` | Optional | Sets a custom theme for [Hosted Checkout](https://docs.adyen.com/online-payments/build-your-integration/?platform=Web&integration=Hosted+Checkout). The value can be any of the **Theme ID** values from your Customer Area. |
| `third_party_token_redundancy_info` | [`ThirdPartyTokenRedundancyInfo1`](../../doc/models/third-party-token-redundancy-info-1.md) | Optional | Configuration for creating redundant payment tokens with third-party token vaults using the Adyen Forward API. This feature requires Forward API webhook integration and pre-configured templates in your Adyen account. Contact your Adyen account manager for setup and availability. |
| `three_ds_2_request_data` | [`CheckoutSessionThreeDS2RequestData1`](../../doc/models/checkout-session-three-ds-2-request-data-1.md) | Optional | Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments). |
| `three_ds_authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**.<br><br>**Default**: `False` |
| `trusted_shopper` | `bool` | Optional | Set to true if the payment should be routed to a trusted MID. |
| `url` | `str` | Optional | The URL for the Hosted Checkout page. Redirect the shopper to this URL so they can make the payment. |

## Example

```python
import dateutil.parser

from adyen.models.account_age_indicator_enum import AccountAgeIndicatorEnum
from adyen.models.account_change_indicator_enum import AccountChangeIndicatorEnum
from adyen.models.account_info import AccountInfo
from adyen.models.account_type_enum import AccountTypeEnum
from adyen.models.amount_1 import Amount1
from adyen.models.amount_18 import Amount18
from adyen.models.application_info import ApplicationInfo
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.create_checkout_session_response import CreateCheckoutSessionResponse
from adyen.models.external_platform import ExternalPlatform
from adyen.models.merchant_device import MerchantDevice
from adyen.models.mode_enum import ModeEnum

create_checkout_session_response = CreateCheckoutSessionResponse(
    amount=Amount18(
        currency='currency2',
        value=110
    ),
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id=None,
    merchant_account='merchantAccount6',
    reference='reference0',
    return_url='returnUrl8',
    account_info=AccountInfo(
        account_age_indicator=AccountAgeIndicatorEnum.FROM30TO60DAYS,
        account_change_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        account_change_indicator=AccountChangeIndicatorEnum.THISTRANSACTION,
        account_creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        account_type=AccountTypeEnum.NOTAPPLICABLE
    ),
    additional_amount=Amount1(
        currency='currency8',
        value=106
    ),
    additional_data={
        'key0': 'additionalData4',
        'key1': 'additionalData5',
        'key2': 'additionalData6'
    },
    allowed_payment_methods=[
        'allowedPaymentMethods9',
        'allowedPaymentMethods0',
        'allowedPaymentMethods1'
    ],
    application_info=ApplicationInfo(
        adyen_library=CommonField4(
            name='name8',
            version='version4'
        ),
        adyen_payment_source=CommonField1(
            name='name2',
            version='version8'
        ),
        external_platform=ExternalPlatform(
            integrator='integrator0',
            name='name4',
            version='version0'
        ),
        merchant_application=CommonField2(
            name='name2',
            version='version8'
        ),
        merchant_device=MerchantDevice(
            os='os4',
            os_version='osVersion6',
            reference='reference8'
        )
    ),
    mode=ModeEnum.EMBEDDED,
    split_card_funding_sources=False,
    three_ds_authentication_only=False
)
```

