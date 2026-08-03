
# Alipay plus Info 1

Details to provide if `type` is **alipay_plus**.

*This model accepts additional fields of type Any.*

## Structure

`AlipayPlusInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. Defaults to USD. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.alipay_plus_info_1 import AlipayPlusInfo1

alipay_plus_info_1 = AlipayPlusInfo1(
    settlement_currency_code='settlementCurrencyCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

