
# Pay at Table

*This model accepts additional fields of type Any.*

## Structure

`PayAtTable`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication_method` | [`AuthenticationMethod`](../../doc/models/authentication-method.md) | Optional | - |
| `enable_pay_at_table` | `bool` | Optional | Enable Pay at table. |
| `payment_instrument` | `Any` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication_method import AuthenticationMethod
from adyen.models.pay_at_table import PayAtTable

pay_at_table = PayAtTable(
    authentication_method=AuthenticationMethod.MAGSWIPE,
    enable_pay_at_table=False,
    payment_instrument=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

