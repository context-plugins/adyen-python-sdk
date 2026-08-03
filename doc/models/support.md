
# Support

*This model accepts additional fields of type Any.*

## Structure

`Support`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The support email address of the legal entity. Required if you have a platform setup. |
| `phone` | [`PhoneNumber`](../../doc/models/phone-number.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.phone_number import PhoneNumber
from adyen.models.support import Support

support = Support(
    email='email6',
    phone=PhoneNumber(
        number='number8',
        phone_country_code='phoneCountryCode8',
        mtype='type0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

