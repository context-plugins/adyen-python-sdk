
# Alipay plus Info

## Structure

`AlipayPlusInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. Defaults to USD. |

## Example

```python
from adyen.models.alipay_plus_info import AlipayPlusInfo

alipay_plus_info = AlipayPlusInfo(
    settlement_currency_code='settlementCurrencyCode2'
)
```

