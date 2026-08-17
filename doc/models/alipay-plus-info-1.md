
# Alipay plus Info 1

Details to provide if `type` is **alipay_plus**.

## Structure

`AlipayPlusInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. Defaults to USD. |

## Example

```python
from adyen.models.alipay_plus_info_1 import AlipayPlusInfo1

alipay_plus_info_1 = AlipayPlusInfo1(
    settlement_currency_code='settlementCurrencyCode0'
)
```

