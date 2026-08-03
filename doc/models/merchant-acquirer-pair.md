
# Merchant Acquirer Pair

*This model accepts additional fields of type Any.*

## Structure

`MerchantAcquirerPair`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `str` | Optional | The acquirer ID. |
| `merchant_id` | `str` | Optional | The merchant identification number (MID). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.merchant_acquirer_pair import MerchantAcquirerPair

merchant_acquirer_pair = MerchantAcquirerPair(
    acquirer_id='acquirerId4',
    merchant_id='merchantId8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

