
# Alipay plus Response Info 1

**alipay_plus** details

*This model accepts additional fields of type Any.*

## Structure

`AlipayPlusResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `settlement_currency_code` | `str` | Optional | The currency used for settlement. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.alipay_plus_response_info_1 import AlipayPlusResponseInfo1

alipay_plus_response_info_1 = AlipayPlusResponseInfo1(
    settlement_currency_code='settlementCurrencyCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

