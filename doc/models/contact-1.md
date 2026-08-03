
# Contact 1

The contact details for the shipping location.

*This model accepts additional fields of type Any.*

## Structure

`Contact1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The individual's email address. |
| `first_name` | `str` | Optional | The individual's first name. |
| `infix` | `str` | Optional | The infix in the individual's name, if any. |
| `last_name` | `str` | Optional | The individual's last name. |
| `phone_number` | `str` | Optional | The individual's phone number, specified as 10-14 digits with an optional `+` prefix. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.contact_1 import Contact1

contact_1 = Contact1(
    email='email2',
    first_name='firstName0',
    infix='infix8',
    last_name='lastName8',
    phone_number='phoneNumber4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

