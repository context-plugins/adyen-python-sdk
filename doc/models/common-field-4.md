
# Common Field 4

Adyen-developed software, such as libraries and plugins, used to interact with the Adyen API. For example, Magento plugin, Java API library, etc.

## Structure

`CommonField4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | Name of the field. For example, Name of External Platform. |
| `version` | `str` | Optional | Version of the field. For example, Version of External Platform. |

## Example

```python
from adyen.models.common_field_4 import CommonField4

common_field_4 = CommonField4(
    name='name2',
    version='version8'
)
```

