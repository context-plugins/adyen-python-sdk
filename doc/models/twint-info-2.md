
# Twint Info 2

Details to provide if `type` is **twint**.

## Structure

`TwintInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `logo` | `str` | Required | Twint logo. Format: Base64-encoded string. |

## Example

```python
from adyen.models.twint_info_2 import TwintInfo2

twint_info_2 = TwintInfo2(
    logo='logo0'
)
```

