
# Create Permit Request

*This model accepts additional fields of type Any.*

## Structure

`CreatePermitRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `permits` | [`List[Permit]`](../../doc/models/permit.md) | Required | The permits to create for this recurring contract. |
| `recurring_detail_reference` | `str` | Required | The recurring contract the new permits will use. |
| `shopper_reference` | `str` | Required | The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.create_permit_request import CreatePermitRequest
from adyen.models.max_amount_3 import MaxAmount3
from adyen.models.permit import Permit
from adyen.models.permit_restriction import PermitRestriction
from adyen.models.single_transaction_limit import SingleTransactionLimit

create_permit_request = CreatePermitRequest(
    merchant_account='merchantAccount6',
    permits=[
        Permit(
            partner_id='partnerId8',
            profile_reference='profileReference0',
            restriction=PermitRestriction(
                max_amount=MaxAmount3(
                    currency='currency4',
                    value=160,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                single_transaction_limit=SingleTransactionLimit(
                    currency='currency8',
                    value=122,
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                single_use=False,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            result_key='resultKey4',
            valid_till_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    recurring_detail_reference='recurringDetailReference4',
    shopper_reference='shopperReference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

