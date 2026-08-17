
# Sodexo Info 2

Details to provide if `type` is **sodexo**.

## Structure

`SodexoInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_contact_phone` | `str` | Required | Sodexo merchantContactPhone |

## Example

```python
from adyen.models.sodexo_info_2 import SodexoInfo2

sodexo_info_2 = SodexoInfo2(
    merchant_contact_phone='merchantContactPhone6'
)
```

