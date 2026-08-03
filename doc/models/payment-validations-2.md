
# Payment Validations 2

The object that you can use to enable payment validations for a transaction.

*This model accepts additional fields of type Any.*

## Structure

`PaymentValidations2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`Name6`](../../doc/models/name-6.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.name_6 import Name6
from adyen.models.payment_validations_2 import PaymentValidations2

payment_validations_2 = PaymentValidations2(
    name=Name6(
        status='status2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

