
# Sofort Info

## Structure

`SofortInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Required | Sofort logo. Format: Base64-encoded string. |

## Example

```python
from adyen.models.sofort_info import SofortInfo

sofort_info = SofortInfo(
    currency_code='currencyCode4',
    logo='logo0'
)
```

