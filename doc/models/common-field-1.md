
# Common Field 1

Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc.

## Structure

`CommonField1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |

## Example

```python
from adyen.models.common_field_1 import CommonField1

common_field_1 = CommonField1(
    name='name4',
    version='version0'
)
```

