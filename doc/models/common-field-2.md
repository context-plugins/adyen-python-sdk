
# Common Field 2

Merchant developed software, such as cashier application, used to interact with the Adyen API.

## Structure

`CommonField2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |

## Example

```python
from adyen.models.common_field_2 import CommonField2

common_field_2 = CommonField2(
    name='name6',
    version='version2'
)
```

