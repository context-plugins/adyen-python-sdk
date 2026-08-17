
# Payout Request

## Structure

`PayoutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero). |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | The address where to send the invoice.<br><br>> The `billingAddress` object is required in the following scenarios. Include all of the fields within this object.<br>> <br>> * For 3D Secure 2 transactions in all browser-based and mobile implementations.<br>> * For cross-border payouts to and from Canada. |
| `card` | [`Card`](../../doc/models/card.md) | Optional | A container for card data.<br><br>> Either `bankAccount` or `card` field must be provided in a payment request. |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `fund_source` | [`FundSource11`](../../doc/models/fund-source-11.md) | Optional | The person or entity funding the money. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `recurring` | [`Recurring`](../../doc/models/recurring.md) | Optional | The recurring settings for the payment. Use this property when you want to enable [recurring payments](https://docs.adyen.com/classic-integration/recurring-payments). |
| `reference` | `str` | Required | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br>Maximum length: 80 characters. |
| `selected_recurring_detail_reference` | `str` | Optional | The `recurringDetailReference` you want to use for this payment. The value `LATEST` can be used to select the most recently stored recurring detail. |
| `shopper_email` | `str` | Optional | The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. > Required for Visa and JCB transactions that require 3D Secure 2 authentication if you did not include the `telephoneNumber`. |
| `shopper_interaction` | [`ShopperInteractionEnum`](../../doc/models/shopper-interaction-enum.md) | Optional | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.<br>For the web service API, Adyen assumes Ecommerce shopper interaction by default.<br><br>This field has the following possible values:<br><br>* `Ecommerce` - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.<br>* `ContAuth` - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).<br>* `Moto` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.<br>* `POS` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |
| `shopper_name` | [`Name`](../../doc/models/name.md) | Optional | The shopper's full name. |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address. |
| `telephone_number` | `str` | Optional | The shopper's telephone number.<br>The phone number must include a plus sign (+) and a country code (1-3 digits), followed by the number (4-15 digits). If the value you provide does not follow the guidelines, we do not submit it for authentication.<br><br>> Required for Visa and JCB transactions that require 3D Secure 2 authentication, if you did not include the `shopperEmail`. |

## Example

```python
import dateutil.parser

from adyen.models.address import Address
from adyen.models.amount import Amount
from adyen.models.card import Card
from adyen.models.contract_enum import ContractEnum
from adyen.models.fund_source_11 import FundSource11
from adyen.models.name import Name
from adyen.models.payout_request import PayoutRequest
from adyen.models.recurring import Recurring
from adyen.models.token_service_enum import TokenServiceEnum

payout_request = PayoutRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount2',
    reference='reference8',
    billing_address=Address(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0'
    ),
    card=Card(
        cvc='cvc0',
        expiry_month='expiryMonth0',
        expiry_year='expiryYear0',
        holder_name='holderName2',
        issue_number='issueNumber8'
    ),
    fraud_offset=82,
    fund_source=FundSource11(
        additional_data={
            'key0': 'additionalData8'
        },
        billing_address=Address(
            city='city8',
            country='country6',
            house_number_or_name='houseNumberOrName0',
            postal_code='postalCode6',
            street='street2',
            state_or_province='stateOrProvince0'
        ),
        card=Card(
            cvc='cvc0',
            expiry_month='expiryMonth0',
            expiry_year='expiryYear0',
            holder_name='holderName2',
            issue_number='issueNumber8'
        ),
        shopper_email='shopperEmail4',
        shopper_name=Name(
            first_name='firstName2',
            last_name='lastName6'
        )
    ),
    recurring=Recurring(
        contract=ContractEnum.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenServiceEnum.VISATOKENSERVICE
    )
)
```

