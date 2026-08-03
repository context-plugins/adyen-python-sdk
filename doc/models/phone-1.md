
# Phone 1

The phone number where the one-time password (OTP) is sent.

This object must have:

* A `type` set to **mobile**.

* A `number` with a valid country code.

* A `number` with more than 4 digits, excluding the country code.

> Make sure to verify that the card user owns the phone number.

*This model accepts additional fields of type Any.*

## Structure

`Phone1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `number` | `str` | Required | The full phone number provided as a single string.<br>For example, **"0031 6 11 22 33 44"**, **"+316/1122-3344"**,<br><br>or **"(0031) 611223344"**. |
| `mtype` | [`Type4`](../../doc/models/type-4.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.phone_1 import Phone1
from adyen.models.type_4 import Type4

phone_1 = Phone1(
    number='number0',
    mtype=Type4.LANDLINE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

