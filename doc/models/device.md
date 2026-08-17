
# Device

## Structure

`Device`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The unique identifier of the SCA device. |
| `name` | `str` | Optional | The name of the SCA device. You can show this name to your user to help them identify the device. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument that is associated with the SCA device. |
| `mtype` | [`Type101Enum`](../../doc/models/type-101-enum.md) | Optional | The type of device.<br><br>Possible values: **ios**, **android**, **browser**. |

## Example

```python
from adyen.models.device import Device
from adyen.models.type_101_enum import Type101Enum

device = Device(
    id='id6',
    name='name6',
    payment_instrument_id='paymentInstrumentId8',
    mtype=Type101Enum.IOS
)
```

