
# Store Detail and Submit Request

## Structure

`StoreDetailAndSubmitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request. |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | A container object for the payable amount information of the transaction. |
| `bank` | [`BankAccount`](../../doc/models/bank-account.md) | Optional | A container for bank account data.<br><br>> This field is mandatory if `card` is not provided. |
| `billing_address` | [`Address`](../../doc/models/address.md) | Optional | The billing address.<br><br>> The `billingAddress` object is required for cross-border payouts to and from Canada. Include all of the fields within this object. |
| `card` | [`Card`](../../doc/models/card.md) | Optional | A container for card data.<br><br>> This field is mandatory if `bank` is not provided. |
| `date_of_birth` | `date` | Required | The date of birth.<br>Format: [ISO-8601](https://www.w3.org/TR/NOTE-datetime); example: YYYY-MM-DD<br>For Paysafecard it must be the same as used when registering the Paysafecard account.<br><br>> This field is mandatory for natural persons. |
| `entity_type` | [`EntityType1Enum`](../../doc/models/entity-type-1-enum.md) | Required | The type of the entity the payout is processed for. |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `nationality` | `str` | Required | The shopper's nationality.<br><br>A valid value is an ISO 2-character country code (e.g. 'NL').<br><br>**Constraints**: *Maximum Length*: `2` |
| `recurring` | [`Recurring`](../../doc/models/recurring.md) | Required | A container for the type of recurring contract to be retrieved.<br><br>The recurring.contract must be set to `PAYOUT` |
| `reference` | `str` | Required | The merchant reference for this payment. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement. |
| `selected_brand` | `str` | Optional | The name of the brand to make a payout to.<br><br>For Paysafecard it must be set to `paysafecard`. |
| `shopper_email` | `str` | Required | The shopper's email address. |
| `shopper_name` | [`Name`](../../doc/models/name.md) | Optional | The shopper's name.<br><br>When the `entityType` is `Company`, the `shopperName.lastName` must contain the company name. |
| `shopper_reference` | `str` | Required | The shopper's reference for the payment transaction. |
| `shopper_statement` | `str` | Optional | The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method). |
| `social_security_number` | `str` | Optional | The shopper's social security number. |
| `telephone_number` | `str` | Optional | The shopper's phone number. |

## Example

```python
import dateutil.parser

from adyen.models.address import Address
from adyen.models.amount import Amount
from adyen.models.bank_account import BankAccount
from adyen.models.card import Card
from adyen.models.contract_enum import ContractEnum
from adyen.models.entity_type_1_enum import EntityType1Enum
from adyen.models.recurring import Recurring
from adyen.models.store_detail_and_submit_request import StoreDetailAndSubmitRequest
from adyen.models.token_service_enum import TokenServiceEnum

store_detail_and_submit_request = StoreDetailAndSubmitRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    date_of_birth=dateutil.parser.parse('2016-03-13').date(),
    entity_type=EntityType1Enum.NATURALPERSON,
    merchant_account='merchantAccount6',
    nationality='nationality0',
    recurring=Recurring(
        contract=ContractEnum.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenServiceEnum.VISATOKENSERVICE
    ),
    reference='reference2',
    shopper_email='shopperEmail4',
    shopper_reference='shopperReference0',
    additional_data={
        'key0': 'additionalData2',
        'key1': 'additionalData1',
        'key2': 'additionalData0'
    },
    bank=BankAccount(
        bank_account_number='bankAccountNumber8',
        bank_city='bankCity0',
        bank_location_id='bankLocationId2',
        bank_name='bankName4',
        bic='bic0'
    ),
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
    fraud_offset=180
)
```

