
# Bcmc Info 1

Details to provide if `type` is **bcmc** (Bancontact).

*This model accepts additional fields of type Any.*

## Structure

`BcmcInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_bcmc_mobile` | `bool` | Optional | Indicates if [Bancontact mobile](https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile) is enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bcmc_info_1 import BcmcInfo1

bcmc_info_1 = BcmcInfo1(
    enable_bcmc_mobile=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

