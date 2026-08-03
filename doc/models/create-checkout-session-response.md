
# Create Checkout Session Response

*This model accepts additional fields of type Any.*

## Structure

`CreateCheckoutSessionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_info` | [`AccountInfo`](../../doc/models/account-info.md) | Optional | - |
| `additional_amount` | [`AdditionalAmount`](../../doc/models/additional-amount.md) | Optional | - |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular payment request.<br><br>The `additionalData` object consists of entries, each of which includes the key and value. |
| `allowed_payment_methods` | `List[str]` | Optional | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).<br><br>Example: `"allowedPaymentMethods":["ideal","applepay"]` |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `application_info` | [`ApplicationInfo1`](../../doc/models/application-info-1.md) | Optional | - |
| `authentication_data` | [`AuthenticationData`](../../doc/models/authentication-data.md) | Optional | - |
| `billing_address` | [`BillingAddress`](../../doc/models/billing-address.md) | Optional | - |
| `blocked_payment_methods` | `List[str]` | Optional | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).<br><br>Example: `"blockedPaymentMethods":["ideal","applepay"]` |
| `capture_delay_hours` | `int` | Optional | The delay between the authorisation and scheduled auto-capture, specified in hours. |
| `channel` | [`Channel`](../../doc/models/channel.md) | Optional | - |
| `company` | [`Company`](../../doc/models/company.md) | Optional | - |
| `country_code` | `str` | Optional | The shopper's two-letter country code. |
| `date_of_birth` | `datetime` | Optional | The shopper's date of birth in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. |
| `deliver_at` | `datetime` | Optional | The date and time when the purchased goods should be delivered.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. |
| `delivery_address` | [`DeliveryAddress1`](../../doc/models/delivery-address-1.md) | Optional | - |
| `enable_one_click` | `bool` | Optional | When true and `shopperReference` is provided, the shopper will be asked if the payment details should be stored for future [one-click payments](https://docs.adyen.com/get-started-with-adyen/payment-glossary/#one-click-payments-definition). |
| `enable_pay_out` | `bool` | Optional | When true and `shopperReference` is provided, the payment details will be tokenized for payouts. |
| `enable_recurring` | `bool` | Optional | When true and `shopperReference` is provided, the payment details will be stored for [recurring payments](https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types) where the shopper is not present, such as subscription or automatic top-up payments. |
| `expires_at` | `datetime` | Required | The date the session expires in [ISO8601](https://www.iso.org/iso-8601-date-and-time-format.html) format. When not specified, the expiry date is set to 1 hour after session creation. You cannot set the session expiry to more than 24 hours after session creation. |
| `fund_origin` | [`FundOrigin`](../../doc/models/fund-origin.md) | Optional | - |
| `fund_recipient` | [`FundRecipient`](../../doc/models/fund-recipient.md) | Optional | - |
| `id` | `str` | Required, Read-only | A unique identifier of the session. |
| `installment_options` | [`Dict[str, CheckoutSessionInstallmentOption]`](../../doc/models/checkout-session-installment-option.md) | Optional | A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or **mc**. The value must be an object containing the installment options. |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information about the purchased items, to be included on the invoice sent to the shopper.<br><br>> This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty. |
| `mandate` | [`Mandate1`](../../doc/models/mandate-1.md) | Optional | - |
| `mcc` | `str` | Optional | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `merchant_order_reference` | `str` | Optional | This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle.<br>The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations.<br><br>> We strongly recommend you send the `merchantOrderReference` value to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provide `retry.orderAttemptNumber`, `retry.chainAttemptNumber`, and `retry.skipRetry` values in `PaymentRequest.additionalData`. |
| `metadata` | `Dict[str, str]` | Optional | Metadata consists of entries, each of which includes a key and a value.<br>Limits:<br><br>* Maximum 20 key-value pairs per request.<br>* Maximum 20 characters per key.<br>* Maximum 80 characters per value. |
| `mode` | [`Mode`](../../doc/models/mode.md) | Optional | - |
| `mpi_data` | [`MpiData`](../../doc/models/mpi-data.md) | Optional | - |
| `platform_chargeback_logic` | [`PlatformChargebackLogic1`](../../doc/models/platform-chargeback-logic-1.md) | Optional | - |
| `recurring_expiry` | `str` | Optional | Date after which no further authorisations shall be performed. Only for 3D Secure 2. |
| `recurring_frequency` | `str` | Optional | Minimum number of days between authorisations. Only for 3D Secure 2. |
| `recurring_processing_model` | [`RecurringProcessingModel1`](../../doc/models/recurring-processing-model-1.md) | Optional | - |
| `redirect_from_issuer_method` | `str` | Optional | Specifies the redirect method (GET or POST) when redirecting back from the issuer. |
| `redirect_to_issuer_method` | `str` | Optional | Specifies the redirect method (GET or POST) when redirecting to the issuer. |
| `reference` | `str` | Required | The reference to uniquely identify a payment. |
| `return_url` | `str` | Required | The URL to return to in case of a redirection.<br>The format depends on the channel.<br><br>* For web, include the protocol `http://` or `https://`. You can also include your own additional query parameters, for example, shopper ID or order reference number.<br>  Example: `https://your-company.example.com/checkout?shopperOrder=12xy`<br>* For iOS, use the custom URL for your app. To know more about setting custom URL schemes, refer to the [Apple Developer documentation](https://developer.apple.com/documentation/uikit/inter-process_communication/allowing_apps_and_websites_to_link_to_your_content/defining_a_custom_url_scheme_for_your_app).<br>  Example: `my-app://`<br>* For Android, use a custom URL handled by an Activity on your app. You can configure it with an [intent filter](https://developer.android.com/guide/components/intents-filters).<br>  Example: `my-app://your.package.name`<br><br>If the URL to return to includes non-ASCII characters, like spaces or special letters, URL encode the value.<br><br>> The URL must not include personally identifiable information (PII), for example name or email address.<br><br>**Constraints**: *Maximum Length*: `1024` |
| `risk_data` | [`RiskData`](../../doc/models/risk-data.md) | Optional | - |
| `session_data` | `str` | Optional | The payment session data you need to pass to your front end. |
| `shopper_email` | `str` | Optional | The shopper's email address. |
| `shopper_ip` | `str` | Optional | The shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks).<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile integrations, if you did not include the `shopperEmail`. For native mobile integrations, the field is required to support cases where authentication is routed to the redirect flow. This field is also mandatory for some merchants depending on your business model. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). |
| `shopper_interaction` | [`ShopperInteraction1`](../../doc/models/shopper-interaction-1.md) | Optional | - |
| `shopper_locale` | `str` | Optional | The language for the payment. The value combines the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) language code with the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) country code. For example, **nl-NL**.<br><br>When using Drop-in/Components, the specified language appears if your front-end global configuration does not set the `locale`. |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `shopper_reference` | `str` | Optional | Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `256` |
| `shopper_statement` | `str` | Optional | The text to be shown on the shopper's bank statement.<br>We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.<br>Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**. |
| `show_installment_amount` | `bool` | Optional | Set to true to show the payment amount per installment. |
| `show_remove_payment_method_button` | `bool` | Optional | Set to **true** to show a button that lets the shopper remove a stored payment method. |
| `social_security_number` | `str` | Optional | The shopper's social security number. |
| `split_card_funding_sources` | `bool` | Optional | Boolean value indicating whether the card payment method should be split into separate debit and credit options.<br><br>**Default**: `False` |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/platforms/process-payments#providing-split-information), [Classic Platforms integration](https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information), or [Issuing](https://docs.adyen.com/issuing/manage-funds#split). |
| `store` | `str` | Optional | Required for Adyen for Platforms integrations if you are a platform model. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/platforms)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment. |
| `store_filtration_mode` | [`StoreFiltrationMode`](../../doc/models/store-filtration-mode.md) | Optional | - |
| `store_payment_method` | `bool` | Optional | When true and `shopperReference` is provided, the payment details will be stored for future [recurring payments](https://docs.adyen.com/online-payments/tokenization/#recurring-payment-types). |
| `store_payment_method_mode` | [`StorePaymentMethodMode`](../../doc/models/store-payment-method-mode.md) | Optional | - |
| `telephone_number` | `str` | Optional | The shopper's telephone number.<br>The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`. |
| `theme_id` | `str` | Optional | Sets a custom theme for [Hosted Checkout](https://docs.adyen.com/online-payments/build-your-integration/?platform=Web&integration=Hosted+Checkout). The value can be any of the **Theme ID** values from your Customer Area. |
| `third_party_token_redundancy_info` | [`ThirdPartyTokenRedundancyInfo`](../../doc/models/third-party-token-redundancy-info.md) | Optional | - |
| `three_ds_2_request_data` | [`CheckoutSessionThreeDs2RequestData`](../../doc/models/checkout-session-three-ds-2-request-data.md) | Optional | - |
| `three_ds_authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**.<br><br>**Default**: `False` |
| `trusted_shopper` | `bool` | Optional | Set to true if the payment should be routed to a trusted MID. |
| `url` | `str` | Optional | The URL for the Hosted Checkout page. Redirect the shopper to this URL so they can make the payment. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.account_age_indicator import AccountAgeIndicator
from adyen.models.account_change_indicator import AccountChangeIndicator
from adyen.models.account_info import AccountInfo
from adyen.models.account_type_1 import AccountType1
from adyen.models.additional_amount import AdditionalAmount
from adyen.models.adyen_library import AdyenLibrary
from adyen.models.adyen_payment_source import AdyenPaymentSource
from adyen.models.amount_16 import Amount16
from adyen.models.application_info_1 import ApplicationInfo1
from adyen.models.create_checkout_session_response import CreateCheckoutSessionResponse
from adyen.models.external_platform_2 import ExternalPlatform2
from adyen.models.merchant_application import MerchantApplication
from adyen.models.merchant_device_2 import MerchantDevice2

create_checkout_session_response = CreateCheckoutSessionResponse(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id4',
    merchant_account='merchantAccount6',
    reference='reference0',
    return_url='returnUrl8',
    account_info=AccountInfo(
        account_age_indicator=AccountAgeIndicator.FROM30TO60DAYS,
        account_change_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        account_change_indicator=AccountChangeIndicator.THISTRANSACTION,
        account_creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        account_type=AccountType1.NOTAPPLICABLE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_amount=AdditionalAmount(
        currency='currency8',
        value=106,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
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
    application_info=ApplicationInfo1(
        adyen_library=AdyenLibrary(
            name='name8',
            version='version4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        adyen_payment_source=AdyenPaymentSource(
            name='name2',
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        external_platform=ExternalPlatform2(
            integrator='integrator0',
            name='name4',
            version='version0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        merchant_application=MerchantApplication(
            name='name2',
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        merchant_device=MerchantDevice2(
            os='os4',
            os_version='osVersion6',
            reference='reference8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    split_card_funding_sources=False,
    three_ds_authentication_only=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

