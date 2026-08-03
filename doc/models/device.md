
# Device

*This model accepts additional fields of type Any.*

## Structure

`Device`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the SCA device. |
| `name` | `str` | Optional | The name of the SCA device. You can show this name to your user to help them identify the device. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument that is associated with the SCA device. |
| `mtype` | [`Type10`](../../doc/models/type-10.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.device import Device
from adyen.models.type_10 import Type10

device = Device(
    id='id6',
    name='name6',
    payment_instrument_id='paymentInstrumentId8',
    mtype=Type10.IOS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

