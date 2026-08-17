
# Sofort Info 2

Sofort details.

## Structure

`SofortInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Required | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Required | Sofort logo. Format: Base64-encoded string. |

## Example

```python
from adyen.models.sofort_info_2 import SofortInfo2

sofort_info_2 = SofortInfo2(
    currency_code='currencyCode2',
    logo='logo8'
)
```

