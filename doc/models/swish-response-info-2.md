
# Swish Response Info 2

**swish** or its variant details

*This model accepts additional fields of type Any.*

## Structure

`SwishResponseInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `swish_number` | `str` | Optional | Swish number. Format: 10 digits without spaces. For example, **1231111111**.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.swish_response_info_2 import SwishResponseInfo2

swish_response_info_2 = SwishResponseInfo2(
    swish_number='swishNumber2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

