
# Validate Shopper Id Response

*This model accepts additional fields of type Any.*

## Structure

`ValidateShopperIdResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | Reason for the result. |
| `result` | [`Result1`](../../doc/models/result-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.result_1 import Result1
from adyen.models.validate_shopper_id_response import ValidateShopperIdResponse

validate_shopper_id_response = ValidateShopperIdResponse(
    reason='reason4',
    result=Result1.VALID,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

