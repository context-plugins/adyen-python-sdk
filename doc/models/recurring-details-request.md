
# Recurring Details Request

*This model accepts additional fields of type Any.*

## Structure

`RecurringDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier you want to process the (transaction) request with. |
| `recurring` | [`Recurring3`](../../doc/models/recurring-3.md) | Optional | - |
| `shopper_reference` | `str` | Required | The reference you use to uniquely identify the shopper (e.g. user ID or account ID). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.contract import Contract
from adyen.models.recurring_3 import Recurring3
from adyen.models.recurring_details_request import RecurringDetailsRequest
from adyen.models.token_service import TokenService

recurring_details_request = RecurringDetailsRequest(
    merchant_account='merchantAccount8',
    shopper_reference='shopperReference4',
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
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

