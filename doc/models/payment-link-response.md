
# Payment Link Response

## Structure

`PaymentLinkResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allowed_payment_methods` | `List[str]` | Optional | List of payment methods to be presented to the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).<br><br>Example: `"allowedPaymentMethods":["ideal","applepay"]` |
| `amount` | [`Amount35`](../../doc/models/amount-35.md) | Required | The payment amount and currency. |
| `application_info` | [`ApplicationInfo`](../../doc/models/application-info.md) | Optional | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
| `billing_address` | [`Address3`](../../doc/models/address-3.md) | Optional | The address where to send the invoice. |
| `blocked_payment_methods` | `List[str]` | Optional | List of payment methods to be hidden from the shopper. To refer to payment methods, use their [payment method type](https://docs.adyen.com/payment-methods/payment-method-types).<br><br>Example: `"blockedPaymentMethods":["ideal","applepay"]` |
| `capture_delay_hours` | `int` | Optional | The delay between the authorisation and scheduled auto-capture, specified in hours. |
| `country_code` | `str` | Optional | The shopper's two-letter country code.<br><br>**Constraints**: *Maximum Length*: `100` |
| `date_of_birth` | `date` | Optional | The shopper's date of birth.<br><br>Format [ISO-8601](https://www.w3.org/TR/NOTE-datetime): YYYY-MM-DD |
| `deliver_at` | `datetime` | Optional | The date and time when the purchased goods should be delivered.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. |
| `delivery_address` | [`Address2`](../../doc/models/address-2.md) | Optional | The address where the purchased goods should be delivered. |
| `description` | `str` | Optional | A short description visible on the payment page.<br>Maximum length: 280 characters. |
| `expires_at` | `datetime` | Optional | The date when the payment link expires.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format with time zone offset: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**.<br><br>The maximum expiry date is 70 days after the payment link is created.<br><br>If not provided, the payment link expires 24 hours after it was created. |
| `fund_origin` | [`FundOrigin1`](../../doc/models/fund-origin-1.md) | Optional | The person or entity funding the money. |
| `fund_recipient` | [`FundRecipient1`](../../doc/models/fund-recipient-1.md) | Optional | the person or entity receiving the money |
| `id` | `str` | Required, Read-only | A unique identifier of the payment link. |
| `installment_options` | [`Dict[str, InstallmentOption]`](../../doc/models/installment-option.md) | Optional | A set of key-value pairs that specifies the installment options available per payment method. The key must be a payment method name in lowercase. For example, **card** to specify installment options for all cards, or **visa** or **mc**. The value must be an object containing the installment options. |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information about the purchased items, to be included on the invoice sent to the shopper.<br><br>> This field is required for 3x 4x Oney, Affirm, Afterpay, Clearpay, Klarna, Ratepay, and Riverty. |
| `manual_capture` | `bool` | Optional | Indicates if the payment must be [captured manually](https://docs.adyen.com/online-payments/capture). |
| `mcc` | `str` | Optional | The [merchant category code](https://en.wikipedia.org/wiki/Merchant_category_code) (MCC) is a four-digit number, which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.<br><br>**Constraints**: *Maximum Length*: `16` |
| `merchant_account` | `str` | Required | The merchant account identifier for which the payment link is created. |
| `merchant_order_reference` | `str` | Optional | This reference allows linking multiple transactions to each other for reporting purposes (for example, order auth-rate). The reference should be unique per billing cycle.<br><br>**Constraints**: *Maximum Length*: `1000` |
| `metadata` | `Dict[str, str]` | Optional | Metadata consists of entries, each of which includes a key and a value.<br>Limitations:<br><br>* Maximum 20 key-value pairs per request. Otherwise, error "177" occurs: "Metadata size exceeds limit"<br>* Maximum 20 characters per key. Otherwise, error "178" occurs: "Metadata key size exceeds limit"<br>* A key cannot have the name `checkout.linkId`. Any value that you provide with this key is going to be replaced by the real payment link ID. |
| `platform_chargeback_logic` | [`PlatformChargebackLogic4`](../../doc/models/platform-chargeback-logic-4.md) | Optional | Dictates the behavior of how a potential chargeback should be booked when using Adyen Platforms. |
| `recurring_processing_model` | [`RecurringProcessingModel4Enum`](../../doc/models/recurring-processing-model-4-enum.md) | Optional | Defines a recurring payment type. Required when `storePaymentMethodMode` is set to **askForConsent** or **enabled**.<br>Possible values:<br><br>* **Subscription** – A transaction for a fixed or variable amount, which follows a fixed schedule.<br>* **CardOnFile** – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.<br>* **UnscheduledCardOnFile** – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or has variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount.<br><br>**Constraints**: *Maximum Length*: `50` |
| `reference` | `str` | Required | A reference that is used to uniquely identify the payment in future communications about the payment status. |
| `required_shopper_fields` | [`List[RequiredShopperFieldEnum]`](../../doc/models/required-shopper-field-enum.md) | Optional | List of fields that the shopper has to provide on the payment page before completing the payment. For more information, refer to [Provide shopper information](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#shopper-information).<br><br>Possible values:<br><br>* **billingAddress** – The address where to send the invoice.<br>* **deliveryAddress** – The address where the purchased goods should be delivered.<br>* **shopperEmail** – The shopper's email address.<br>* **shopperName** – The shopper's full name.<br>* **telephoneNumber** – The shopper's phone number. |
| `return_url` | `str` | Optional | Website URL used for redirection after payment is completed.<br>If provided, a **Continue** button will be shown on the payment page. If shoppers select the button, they are redirected to the specified URL.<br><br>**Constraints**: *Maximum Length*: `8000` |
| `reusable` | `bool` | Optional | Indicates whether the payment link can be reused for multiple payments. If not provided, this defaults to **false** which means the link can be used for one successful payment only. |
| `risk_data` | [`RiskData1`](../../doc/models/risk-data-1.md) | Optional | Any risk-related settings to apply to the payment. |
| `shopper_email` | `str` | Optional | The shopper's email address.<br><br>**Constraints**: *Maximum Length*: `500` |
| `shopper_locale` | `str` | Optional | The language to be used in the payment page, specified by a combination of a language and country code. For example, `en-US`.<br><br>For a list of shopper locales that Pay by Link supports, refer to [Language and localization](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#language).<br><br>**Constraints**: *Maximum Length*: `32` |
| `shopper_name` | [`Name4`](../../doc/models/name-4.md) | Optional | The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program. |
| `shopper_reference` | `str` | Optional | Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `256` |
| `shopper_statement` | `str` | Optional | The text to be shown on the shopper's bank statement.<br>We recommend sending a maximum of 22 characters, otherwise banks might truncate the string.<br>Allowed characters: **a-z**, **A-Z**, **0-9**, spaces, and special characters **. , ' _ - ? + * /**.<br><br>**Constraints**: *Maximum Length*: `10000` |
| `show_remove_payment_method_button` | `bool` | Optional | Set to **false** to hide the button that lets the shopper remove a stored payment method.<br><br>**Default**: `True` |
| `social_security_number` | `str` | Optional | The shopper's social security number.<br><br>**Constraints**: *Maximum Length*: `32` |
| `split_card_funding_sources` | `bool` | Optional | Boolean value indicating whether the card payment method should be split into separate debit and credit options.<br><br>**Default**: `False` |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how to split a payment when using [Adyen for Platforms](https://docs.adyen.com/platforms/process-payments#providing-split-information), [Classic Platforms integration](https://docs.adyen.com/classic-platforms/processing-payments#providing-split-information), or [Issuing](https://docs.adyen.com/issuing/manage-funds#split). |
| `status` | [`Status3Enum`](../../doc/models/status-3-enum.md) | Required | Status of the payment link. Possible values:<br><br>* **active**: The link can be used to make payments.<br>* **expired**: The expiry date for the payment link has passed. Shoppers can no longer use the link to make payments.<br>* **completed**: The shopper completed the payment.<br>* **paymentPending**: The shopper is in the process of making the payment. Applies to payment methods with an asynchronous flow. |
| `store` | `str` | Optional | The physical store, for which this payment is processed. |
| `store_payment_method_mode` | [`StorePaymentMethodMode2Enum`](../../doc/models/store-payment-method-mode-2-enum.md) | Optional | Indicates if the details of the payment method will be stored for the shopper. Possible values:<br><br>* **disabled** – No details will be stored (default).<br>* **askForConsent** – If the `shopperReference` is provided, the Drop-in/Component shows a checkbox where the shopper can select to store their payment details for card payments.<br>* **enabled** – If the `shopperReference` is provided, the details will be stored without asking the shopper for consent.<br>  When set to **askForConsent** or **enabled**, you must also include the `recurringProcessingModel` parameter. |
| `telephone_number` | `str` | Optional | The shopper's telephone number.<br>The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`.<br><br>**Constraints**: *Maximum Length*: `32` |
| `theme_id` | `str` | Optional | A [theme](https://docs.adyen.com/unified-commerce/pay-by-link/payment-links/api#themes) to customize the appearance of the payment page. If not specified, the payment page is rendered according to the theme set as default in your Customer Area. |
| `three_ds_2_request_data` | [`CheckoutSessionThreeDS2RequestData3`](../../doc/models/checkout-session-three-ds-2-request-data-3.md) | Optional | The cardholder phone number need to be part of the authentication message for payment data. It is a requirement for Visa Secure Authentication Data Field Mandate effective August 2024. |
| `updated_at` | `datetime` | Optional | The date when the payment link status was updated.<br><br>[ISO 8601](https://www.w3.org/TR/NOTE-datetime) format: YYYY-MM-DDThh:mm:ss+TZD, for example, **2020-12-18T10:15:30+01:00**. |
| `url` | `str` | Required, Read-only | The URL at which the shopper can complete the payment. |

## Example

```python
from adyen.models.address_3 import Address3
from adyen.models.amount_35 import Amount35
from adyen.models.application_info import ApplicationInfo
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.external_platform import ExternalPlatform
from adyen.models.merchant_device import MerchantDevice
from adyen.models.payment_link_response import PaymentLinkResponse
from adyen.models.status_3_enum import Status3Enum

payment_link_response = PaymentLinkResponse(
    amount=Amount35(
        currency='currency2',
        value=110
    ),
    id=None,
    merchant_account='merchantAccount2',
    reference='reference6',
    status=Status3Enum.EXPIRED,
    url=None,
    allowed_payment_methods=[
        'allowedPaymentMethods5',
        'allowedPaymentMethods6'
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
    billing_address=Address3(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0'
    ),
    blocked_payment_methods=[
        'blockedPaymentMethods4',
        'blockedPaymentMethods5'
    ],
    capture_delay_hours=12,
    show_remove_payment_method_button=True,
    split_card_funding_sources=False
)
```

