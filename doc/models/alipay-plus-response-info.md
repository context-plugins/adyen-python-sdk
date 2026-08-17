
# Alipay plus Response Info

## Structure

`AlipayPlusResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. |

## Example

```python
from adyen.models.alipay_plus_response_info import AlipayPlusResponseInfo

alipay_plus_response_info = AlipayPlusResponseInfo(
    settlement_currency_code='settlementCurrencyCode0'
)
```

