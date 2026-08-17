
# Submit Request

## Structure

`SubmitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request. |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | A container object for the payable amount information of the transaction. |
| `date_of_birth` | `date` | Optional | The date of birth.<br>Format: ISO-8601; example: YYYY-MM-DD<br><br>For Paysafecard it must be the same as used when registering the Paysafecard account.<br><br>> This field is mandatory for natural persons.<br>> This field is required to update the existing `dateOfBirth` that is associated with this recurring contract. |
| `entity_type` | [`EntityType2Enum`](../../doc/models/entity-type-2-enum.md) | Optional | The type of the entity the payout is processed for.<br><br>Allowed values:<br><br>* NaturalPerson<br>* Company<br><br>> This field is required to update the existing `entityType` that is associated with this recurring contract. |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `merchant_account` | `str` | Required | The merchant account identifier you want to process the transaction request with. |
| `nationality` | `str` | Optional | The shopper's nationality.<br><br>A valid value is an ISO 2-character country code (e.g. 'NL').<br><br>> This field is required to update the existing nationality that is associated with this recurring contract. |
| `recurring` | [`Recurring`](../../doc/models/recurring.md) | Required | A container for the type of recurring contract to be retrieved.<br><br>The `recurring.contract` must be set to "PAYOUT". |
| `reference` | `str` | Required | The merchant reference for this payout. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement. |
| `selected_recurring_detail_reference` | `str` | Required | This is the `recurringDetailReference` you want to use for this payout.<br><br>You can use the value LATEST to select the most recently used recurring detail. |
| `shopper_email` | `str` | Required | The shopper's email address. |
| `shopper_name` | [`Name`](../../doc/models/name.md) | Optional | The shopper's name.<br><br>In case the `entityType` is `Company`, the `shopperName.lastName` must contain the company name.<br><br>> This field is required to update the existing `shopperName` associated with a recurring contract. |
| `shopper_reference` | `str` | Required | The shopper's reference for the payout transaction. |
| `shopper_statement` | `str` | Optional | The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method). |
| `social_security_number` | `str` | Optional | The shopper's social security number. |

## Example

```python
import dateutil.parser

from adyen.models.amount import Amount
from adyen.models.contract_enum import ContractEnum
from adyen.models.entity_type_2_enum import EntityType2Enum
from adyen.models.recurring import Recurring
from adyen.models.submit_request import SubmitRequest
from adyen.models.token_service_enum import TokenServiceEnum

submit_request = SubmitRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount6',
    recurring=Recurring(
        contract=ContractEnum.ENUM_ONECLICKRECURRING,
        recurring_detail_name='recurringDetailName2',
        recurring_expiry=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        recurring_frequency='recurringFrequency0',
        token_service=TokenServiceEnum.VISATOKENSERVICE
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
    entity_type=EntityType2Enum.NATURALPERSON,
    fraud_offset=168,
    nationality='nationality2'
)
```

