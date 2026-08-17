
# Contact

## Structure

`Contact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The individual's email address. |
| `first_name` | `str` | Optional | The individual's first name. |
| `infix` | `str` | Optional | The infix in the individual's name, if any. |
| `last_name` | `str` | Optional | The individual's last name. |
| `phone_number` | `str` | Optional | The individual's phone number, specified as 10-14 digits with an optional `+` prefix. |

## Example

```python
from adyen.models.contact import Contact

contact = Contact(
    email='email4',
    first_name='firstName2',
    infix='infix6',
    last_name='lastName6',
    phone_number='phoneNumber2'
)
```

