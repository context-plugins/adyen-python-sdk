
# Support

## Structure

`Support`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The support email address of the legal entity. Required if you have a platform setup. |
| `phone` | [`PhoneNumber1`](../../doc/models/phone-number-1.md) | Optional | The support phone number of the legal entity. Required if you have a platform setup. |

## Example

```python
from adyen.models.phone_number_1 import PhoneNumber1
from adyen.models.support import Support

support = Support(
    email='email6',
    phone=PhoneNumber1(
        number='number8',
        mtype='type0'
    )
)
```

