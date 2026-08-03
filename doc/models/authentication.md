
# Authentication

*This model accepts additional fields of type Any.*

## Structure

`Authentication`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The email address where the one-time password (OTP) is sent. |
| `password` | `str` | Optional | The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and must only contain the following supported characters.<br><br>* Characters between **a-z**, **A-Z**, and **0-9**<br><br>* Special characters: **äöüßÄÖÜ+-*/ç%()=?!~#'",;:$&àùòâôûáúó**<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30` |
| `phone` | [`Phone`](../../doc/models/phone.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authentication import Authentication
from adyen.models.phone import Phone
from adyen.models.type_4 import Type4

authentication = Authentication(
    email='email8',
    password='password2',
    phone=Phone(
        number='number8',
        mtype=Type4.LANDLINE,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

