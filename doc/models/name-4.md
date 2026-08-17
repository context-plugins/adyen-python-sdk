
# Name 4

The shopper's full name. This object is required for some payment methods such as AfterPay, Klarna, or if you're enrolled in the PayPal Seller Protection program.

## Structure

`Name4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Required | The first name.<br><br>**Constraints**: *Maximum Length*: `80` |
| `last_name` | `str` | Required | The last name.<br><br>**Constraints**: *Maximum Length*: `80` |

## Example

```python
from adyen.models.name_4 import Name4

name_4 = Name4(
    first_name='firstName0',
    last_name='lastName8'
)
```

