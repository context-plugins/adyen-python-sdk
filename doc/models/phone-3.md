
# Phone 3

The phone number of the account holder.

*This model accepts additional fields of type Any.*

## Structure

`Phone3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Required | The full phone number provided as a single string.<br>For example, **"0031 6 11 22 33 44"**, **"+316/1122-3344"**,<br><br>or **"(0031) 611223344"**. |
| `mtype` | [`Type4`](../../doc/models/type-4.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.phone_3 import Phone3
from adyen.models.type_4 import Type4

phone_3 = Phone3(
    number='number4',
    mtype=Type4.LANDLINE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

