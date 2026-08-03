
# Alipay plus Info

*This model accepts additional fields of type Any.*

## Structure

`AlipayPlusInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. Defaults to USD. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.alipay_plus_info import AlipayPlusInfo

alipay_plus_info = AlipayPlusInfo(
    settlement_currency_code='settlementCurrencyCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

