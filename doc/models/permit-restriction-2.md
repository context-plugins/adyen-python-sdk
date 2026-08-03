
# Permit Restriction 2

Permit level restriction overrides.

*This model accepts additional fields of type Any.*

## Structure

`PermitRestriction2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_amount` | [`MaxAmount3`](../../doc/models/max-amount-3.md) | Optional | - |
| `single_transaction_limit` | [`SingleTransactionLimit`](../../doc/models/single-transaction-limit.md) | Optional | - |
| `single_use` | `bool` | Optional | Only a single payment can be made using this permit if set to true, otherwise multiple payments are allowed. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.max_amount_3 import MaxAmount3
from adyen.models.permit_restriction_2 import PermitRestriction2
from adyen.models.single_transaction_limit import SingleTransactionLimit

permit_restriction_2 = PermitRestriction2(
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
)
```

