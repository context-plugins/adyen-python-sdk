
# Schedule Account Updater Request

*This model accepts additional fields of type Any.*

## Structure

`ScheduleAccountUpdaterRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request. |
| `card` | [`Card6`](../../doc/models/card-6.md) | Optional | - |
| `merchant_account` | `str` | Required | Account of the merchant. |
| `reference` | `str` | Required | A reference that merchants can apply for the call. |
| `selected_recurring_detail_reference` | `str` | Optional | The selected detail recurring reference.<br><br>Optional if `card` is provided. |
| `shopper_reference` | `str` | Optional | The reference of the shopper that owns the recurring contract.<br><br>Optional if `card` is provided. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_6 import Card6
from adyen.models.schedule_account_updater_request import ScheduleAccountUpdaterRequest

schedule_account_updater_request = ScheduleAccountUpdaterRequest(
    merchant_account='merchantAccount0',
    reference='reference6',
    additional_data={
        'key0': 'additionalData8'
    },
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
    selected_recurring_detail_reference='selectedRecurringDetailReference2',
    shopper_reference='shopperReference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

