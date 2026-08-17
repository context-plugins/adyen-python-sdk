
# Support 1

Support information for the legal entity. Required if you have a platform setup.

## Structure

`Support1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The support email address of the legal entity. Required if you have a platform setup. |
| `phone` | [`PhoneNumber1`](../../doc/models/phone-number-1.md) | Optional | The support phone number of the legal entity. Required if you have a platform setup. |

## Example

```python
from adyen.models.phone_number_1 import PhoneNumber1
from adyen.models.support_1 import Support1

support_1 = Support1(
    email='email4',
    phone=PhoneNumber1(
        number='number8',
        mtype='type0'
    )
)
```

