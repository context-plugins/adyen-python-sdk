
# Common Field

Adyen-developed software to get payment details. For example, Checkout SDK, Secured Fields SDK, etc., Merchant developed software, such as cashier application, used to interact with the Adyen API., Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc.

## Structure

`CommonField`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |

## Example

```python
from adyen.models.common_field import CommonField

common_field = CommonField(
    name='name4',
    version='version0'
)
```

