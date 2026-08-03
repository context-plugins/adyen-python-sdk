
# Bcmc Info

*This model accepts additional fields of type Any.*

## Structure

`BcmcInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_bcmc_mobile` | `bool` | Optional | Indicates if [Bancontact mobile](https://docs.adyen.com/payment-methods/bancontact/bancontact-mobile) is enabled. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bcmc_info import BcmcInfo

bcmc_info = BcmcInfo(
    enable_bcmc_mobile=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

