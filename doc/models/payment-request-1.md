
# Payment Request 1

## Structure

`PaymentRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_info` | [`AccountInfo`](../../doc/models/account-info.md) | Optional | Shopper account information for 3D Secure 2.<br><br>> For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow. |
| `additional_amount` | [`Amount`](../../doc/models/amount.md) | Optional | If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to `additionalAmount` (while the amount must be still set to 0 to trigger BIN or card verification).<br>Required to be in the same currency as the `amount`. |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular payment request.<br><br>The `additionalData` object consists of entries, each of which includes the key and value. |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero). |
| `application_info` | [`ApplicationInfo`](../../doc/models/application-info.md) | Optional | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
| `bank_account` | [`BankAccount1`](../../doc/models/bank-account-1.md) | Optional | The details of the bank account, from which the payment should be made.<br><br>> Either `bankAccount` or `card` field must be provided in a payment request. |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | The address where to send the invoice.<br><br>> The `billingAddress` object is required in the following scenarios. Include all of the fields within this object.<br>> <br>> * For 3D Secure 2 transactions in all browser-based and mobile implementations.<br>> * For cross-border payouts to and from Canada. |
| `browser_info` | [`BrowserInfo`](../../doc/models/browser-info.md) | Optional | The shopper's browser information.<br><br>> For 3D Secure, the full object is required for web integrations. For mobile app integrations, include the `userAgent` and `acceptHeader` fields to indicate  that your integration can support a redirect in case a payment is routed to 3D Secure 2 redirect. |
| `capture_delay_hours` | `int` | Optional | The delay between the authorisation and scheduled auto-capture, specified in hours. |
| `card` | [`Card3`](../../doc/models/card-3.md) | Optional | A container for card data.<br><br>> Either `bankAccount` or `card` field must be provided in a payment request. |
| `date_of_birth` | `date` | Optional | The shopper's date of birth.<br><br>Format [ISO-8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DD |
| `dcc_quote` | [`ForexQuote11`](../../doc/models/forex-quote-11.md) | Optional | The forex quote as returned in the response of the forex service. |
| `delivery_address` | [`Address`](../../doc/models/address.md) | Optional | The address where the purchased goods should be delivered. |
| `delivery_date` | `datetime` | Optional | The date and time the purchased goods should be delivered.<br><br>Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DDThh:mm:ss.sssTZD<br><br>Example: 2017-07-17T13:42:40.428+01:00 |
| `device_fingerprint` | `str` | Optional | A string containing the shopper's device fingerprint. For more information, refer to [Device fingerprinting](https://docs.adyen.com/risk-management/device-fingerprinting).<br><br>**Constraints**: *Maximum Length*: `5000` |
| `entity_type` | [`EntityTypeEnum`](../../doc/models/entity-type-enum.md) | Optional | The type of the entity the payment is processed for. |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `fund_destination` | [`FundDestination1`](../../doc/models/fund-destination-1.md) | Optional | the person or entity receiving the money |
| `fund_source` | [`FundSource1`](../../doc/models/fund-source-1.md) | Optional | The person or entity funding the money. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `installments` | [`Installments`](../../doc/models/installments.md) | Optional | Contains installment settings. For more information, refer to [Installments](https://docs.adyen.com/payment-methods/cards/credit-card-installments). |
| `localized_shopper_statement` | `Dict[str, str]` | Optional | The `localizedShopperStatement` field lets you use dynamic values for your shopper statement in a local character set. If this parameter is left empty, not provided, or not applicable (in case of cross-border transactions), then **shopperStatement** is used.<br><br>Currently, `localizedShopperStatement` is only supported for payments with Visa, Mastercard, JCB, Diners, and Discover.<br><br>**Supported characters**: Hiragana, Katakana, Kanji, and alphanumeric. |
| `mandate` | [`Mandate`](../../doc/models/mandate.md) | Optional | The mandate details to initiate recurring transaction. |
| `mcc` | `str` | Optional | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `merchant_order_reference` | `str` | Optional | This reference allows linking multiple transactions to each other for reporting purposes (i.e. order auth-rate). The reference should be unique per billing cycle.<br>The same merchant order reference should never be reused after the first authorised attempt. If used, this field should be supplied for all incoming authorisations.<br><br>> We strongly recommend you send the `merchantOrderReference` value to benefit from linking payment requests when authorisation retries take place. In addition, we recommend you provide `retry.orderAttemptNumber`, `retry.chainAttemptNumber`, and `retry.skipRetry` values in `PaymentRequest.additionalData`. |
| `merchant_risk_indicator` | [`MerchantRiskIndicator11`](../../doc/models/merchant-risk-indicator-11.md) | Optional | Additional risk fields for 3D Secure 2.<br><br>> For 3D Secure 2 transactions, we recommend that you include this object to increase the chances of achieving a frictionless flow. |
| `metadata` | `Dict[str, str]` | Optional | Metadata consists of entries, each of which includes a key and a value.<br>Limits:<br><br>* Maximum 20 key-value pairs per request. When exceeding, the "177" error occurs: "Metadata size exceeds limit".<br>* Maximum 20 characters per key.<br>* Maximum 80 characters per value. |
| `mpi_data` | [`ThreeDSecureData`](../../doc/models/three-d-secure-data.md) | Optional | Authentication data produced by an MPI (Mastercard SecureCode, Visa Secure, or Cartes Bancaires). |
| `nationality` | `str` | Optional | The two-character country code of the shopper's nationality.<br><br>**Constraints**: *Maximum Length*: `2` |
| `order_reference` | `str` | Optional | When you are doing multiple partial (gift card) payments, this is the `pspReference` of the first payment. We use this to link the multiple payments to each other. As your own reference for linking multiple payments, use the `merchantOrderReference`instead. |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `recurring` | [`Recurring`](../../doc/models/recurring.md) | Optional | The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/classic-integration/recurring-payments). |
| `recurring_processing_model` | [`RecurringProcessingModelEnum`](../../doc/models/recurring-processing-model-enum.md) | Optional | Defines a recurring payment type. Required when creating a token to store payment details or using stored payment details.<br>Allowed values:<br><br>* `Subscription` – A transaction for a fixed or variable amount, which follows a fixed schedule.<br>* `CardOnFile` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.<br>* `UnscheduledCardOnFile` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount. |
| `reference` | `str` | Required | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br>Maximum length: 80 characters. |
| `secure_remote_commerce_checkout_data` | [`SecureRemoteCommerceCheckoutData2`](../../doc/models/secure-remote-commerce-checkout-data-2.md) | Optional | Checkout data for a Secure Remote Commerce payment. |
| `selected_brand` | `str` | Optional | Some payment methods require defining a value for this field to specify how to process the transaction.<br><br>For the Bancontact payment method, it can be set to:<br><br>* `maestro` (default), to be processed like a Maestro card, or<br>* `bcmc`, to be processed like a Bancontact card. |
| `selected_recurring_detail_reference` | `str` | Optional | The `recurringDetailReference` you want to use for this payment. The value `LATEST` can be used to select the most recently stored recurring detail. |
| `session_id` | `str` | Optional | A session ID used to identify a payment session. |
| `shopper_email` | `str` | Optional | The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. > Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include the `telephoneNumber`. |
| `shopper_ip` | `str` | Optional | The shopper's IP address. We recommend that you provide this data, as it is used in a number of risk checks (for instance, number of payment attempts or location-based checks).<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication for all web and mobile integrations, if you did not include the `shopperEmail`. For native mobile integrations, the field is required to support cases where authentication is routed to the redirect flow. This field is also mandatory for some merchants depending on your business model. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new). |
| `shopper_interaction` | [`ShopperInteractionEnum`](../../doc/models/shopper-interaction-enum.md) | Optional | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.<br>For the web service API, Adyen assumes Ecommerce shopper interaction by default.<br><br>This field has the following possible values:<br><br>* `Ecommerce` - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.<br>* `ContAuth` - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).<br>* `Moto` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.<br>* `POS` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |
| `shopper_locale` | `str` | Optional | The language for the payment. The value combines the two-letter [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) language code with the [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes) country code. For example, **nl-NL**.<br><br>When using Drop-in/Components, the specified language appears if your front-end global configuration does not set the `locale`. |
| `shopper_name` | [`Name`](../../doc/models/name.md) | Optional | The shopper's full name. |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `shopper_statement` | `str` | Optional | The text to be shown on the shopper's bank statement.<br>We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.<br>Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**. |
| `social_security_number` | `str` | Optional | The shopper's social security number. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the payment should be split when using either Adyen for Platforms for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/split-payments), or standalone [Issuing](https://docs.adyen.com/issuing/add-manage-funds#split). |
| `store` | `str` | Optional | Required for Adyen for Platforms integrations if you are a platform model. This is your [reference](https://docs.adyen.com/api-explorer/Management/3/post/merchants/(merchantId)/stores#request-reference) (on [balance platform](https://docs.adyen.com/platforms)) or the [storeReference](https://docs.adyen.com/api-explorer/Account/latest/post/updateAccountHolder#request-accountHolderDetails-storeDetails-storeReference) (in the [classic integration](https://docs.adyen.com/classic-platforms/processing-payments/route-payment-to-store/#route-a-payment-to-a-store)) for the ecommerce or point-of-sale store that is processing the payment.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |
| `telephone_number` | `str` | Optional | The shopper's telephone number.<br>The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`. |
| `three_ds_2_request_data` | [`ThreeDS2RequestData11`](../../doc/models/three-ds-2-request-data-11.md) | Optional | Request fields for 3D Secure 2. To check if any of the following fields are required for your integration, refer to [Online payments](https://docs.adyen.com/online-payments) or [Classic integration](https://docs.adyen.com/classic-integration) documentation. |
| `three_ds_authentication_only` | `bool` | Optional | Required to trigger the [authentication-only flow](https://docs.adyen.com/online-payments/3d-secure/authentication-only/). If set to **true**, you will only perform the 3D Secure 2 authentication, and will not proceed to the payment authorization.Default: **false**.<br><br>**Default**: `False` |
| `totals_group` | `str` | Optional | The reference value to aggregate sales totals in reporting. When not specified, the store field is used (if available).<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |
| `trusted_shopper` | `bool` | Optional | Set to true if the payment should be routed to a trusted MID. |

## Example

```python
import dateutil.parser

from adyen.models.account_age_indicator_enum import AccountAgeIndicatorEnum
from adyen.models.account_change_indicator_enum import AccountChangeIndicatorEnum
from adyen.models.account_info import AccountInfo
from adyen.models.account_type_enum import AccountTypeEnum
from adyen.models.amount import Amount
from adyen.models.application_info import ApplicationInfo
from adyen.models.bank_account_1 import BankAccount1
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.external_platform import ExternalPlatform
from adyen.models.merchant_device import MerchantDevice
from adyen.models.payment_request_1 import PaymentRequest1

payment_request_1 = PaymentRequest1(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount2',
    reference='reference8',
    account_info=AccountInfo(
        account_age_indicator=AccountAgeIndicatorEnum.FROM30TO60DAYS,
        account_change_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        account_change_indicator=AccountChangeIndicatorEnum.THISTRANSACTION,
        account_creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        account_type=AccountTypeEnum.NOTAPPLICABLE
    ),
    additional_amount=Amount(
        currency='currency8',
        value=106
    ),
    additional_data={
        'key0': 'additionalData6',
        'key1': 'additionalData7'
    },
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
    bank_account=BankAccount1(
        bank_account_number='bankAccountNumber8',
        bank_city='bankCity0',
        bank_location_id='bankLocationId2',
        bank_name='bankName6',
        bic='bic0'
    ),
    three_ds_authentication_only=False
)
```

