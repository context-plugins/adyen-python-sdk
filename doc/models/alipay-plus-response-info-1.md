
# Alipay plus Response Info 1

**alipay_plus** details

## Structure

`AlipayPlusResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. |

## Example

```python
from adyen.models.alipay_plus_response_info_1 import AlipayPlusResponseInfo1

alipay_plus_response_info_1 = AlipayPlusResponseInfo1(
    settlement_currency_code='settlementCurrencyCode0'
)
```

