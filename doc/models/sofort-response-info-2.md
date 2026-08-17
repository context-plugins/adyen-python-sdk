
# Sofort Response Info 2

Sofort details.

## Structure

`SofortResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Optional | Sofort logo. Format: Base64-encoded string. |

## Example

```python
from adyen.models.sofort_response_info_2 import SofortResponseInfo2

sofort_response_info_2 = SofortResponseInfo2(
    currency_code='currencyCode4',
    logo='logo0'
)
```

