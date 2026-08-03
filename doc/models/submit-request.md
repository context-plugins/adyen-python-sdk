
# Submit Request

*This model accepts additional fields of type Any.*

## Structure

`SubmitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `date_of_birth` | `date` | Optional | The date of birth.<br>Format: ISO-8601; example: YYYY-MM-DD<br><br>For Paysafecard it must be the same as used when registering the Paysafecard account.<br><br>> This field is mandatory for natural persons.<br>> This field is required to update the existing `dateOfBirth` that is associated with this recurring contract. |
| `entity_type` | [`EntityType2`](../../doc/models/entity-type-2.md) | Optional | - |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `merchant_account` | `str` | Required | The merchant account identifier you want to process the transaction request with. |
| `nationality` | `str` | Optional | The shopper's nationality.<br><br>A valid value is an ISO 2-character country code (e.g. 'NL').<br><br>> This field is required to update the existing nationality that is associated with this recurring contract. |
| `recurring` | [`Recurring3`](../../doc/models/recurring-3.md) | Required | - |
| `reference` | `str` | Required | The merchant reference for this payout. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement. |
| `selected_recurring_detail_reference` | `str` | Required | This is the `recurringDetailReference` you want to use for this payout.<br><br>You can use the value LATEST to select the most recently used recurring detail. |
| `shopper_email` | `str` | Required | The shopper's email address. |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `shopper_reference` | `str` | Required | The shopper's reference for the payout transaction. |
| `shopper_statement` | `str` | Optional | The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method). |
| `social_security_number` | `str` | Optional | The shopper's social security number. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.contract import Contract
from adyen.models.entity_type_2 import EntityType2
from adyen.models.recurring_3 import Recurring3
from adyen.models.submit_request import SubmitRequest
from adyen.models.token_service import TokenService

submit_request = SubmitRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount6',
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
    reference='reference0',
    selected_recurring_detail_reference='selectedRecurringDetailReference6',
    shopper_email='shopperEmail8',
    shopper_reference='shopperReference2',
    additional_data={
        'key0': 'additionalData4',
        'key1': 'additionalData5',
        'key2': 'additionalData6'
    },
    date_of_birth=dateutil.parser.parse('2016-03-13').date(),
    entity_type=EntityType2.NATURALPERSON,
    fraud_offset=168,
    nationality='nationality2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

