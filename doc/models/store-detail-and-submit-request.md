
# Store Detail and Submit Request

*This model accepts additional fields of type Any.*

## Structure

`StoreDetailAndSubmitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `bank` | [`Bank`](../../doc/models/bank.md) | Optional | - |
| `billing_address` | [`BillingAddress7`](../../doc/models/billing-address-7.md) | Optional | - |
| `card` | [`Card6`](../../doc/models/card-6.md) | Optional | - |
| `date_of_birth` | `date` | Required | The date of birth.<br>Format: [ISO-8601](https://www.w3.org/TR/NOTE-datetime); example: YYYY-MM-DD<br>For Paysafecard it must be the same as used when registering the Paysafecard account.<br><br>> This field is mandatory for natural persons. |
| `entity_type` | [`EntityType1`](../../doc/models/entity-type-1.md) | Required | - |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `nationality` | `str` | Required | The shopper's nationality.<br><br>A valid value is an ISO 2-character country code (e.g. 'NL').<br><br>**Constraints**: *Maximum Length*: `2` |
| `recurring` | [`Recurring3`](../../doc/models/recurring-3.md) | Required | - |
| `reference` | `str` | Required | The merchant reference for this payment. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement. |
| `selected_brand` | `str` | Optional | The name of the brand to make a payout to.<br><br>For Paysafecard it must be set to `paysafecard`. |
| `shopper_email` | `str` | Required | The shopper's email address. |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `shopper_reference` | `str` | Required | The shopper's reference for the payment transaction. |
| `shopper_statement` | `str` | Optional | The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method). |
| `social_security_number` | `str` | Optional | The shopper's social security number. |
| `telephone_number` | `str` | Optional | The shopper's phone number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.bank import Bank
from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.card_6 import Card6
from adyen.models.contract import Contract
from adyen.models.entity_type_1 import EntityType1
from adyen.models.recurring_3 import Recurring3
from adyen.models.store_detail_and_submit_request import StoreDetailAndSubmitRequest
from adyen.models.token_service import TokenService

store_detail_and_submit_request = StoreDetailAndSubmitRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    date_of_birth=dateutil.parser.parse('2016-03-13').date(),
    entity_type=EntityType1.NATURALPERSON,
    merchant_account='merchantAccount6',
    nationality='nationality0',
    recurring=Recurring3(
        contract=Contract.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenService.VISATOKENSERVICE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference2',
    shopper_email='shopperEmail4',
    shopper_reference='shopperReference0',
    additional_data={
        'key0': 'additionalData2',
        'key1': 'additionalData1',
        'key2': 'additionalData0'
    },
    bank=Bank(
        bank_account_number='bankAccountNumber8',
        bank_city='bankCity0',
        bank_location_id='bankLocationId2',
        bank_name='bankName4',
        bic='bic0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    billing_address=BillingAddress7(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card=Card6(
        cvc='cvc0',
        expiry_month='expiryMonth0',
        expiry_year='expiryYear0',
        holder_name='holderName2',
        issue_number='issueNumber8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    fraud_offset=180,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

