
# Sofort Response Info

## Structure

`SofortResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_code` | `str` | Optional | Sofort currency code. For example, **EUR**. |
| `logo` | `str` | Optional | Sofort logo. Format: Base64-encoded string. |

## Example

```python
from adyen.models.sofort_response_info import SofortResponseInfo

sofort_response_info = SofortResponseInfo(
    currency_code='currencyCode2',
    logo='logo8'
)
```

