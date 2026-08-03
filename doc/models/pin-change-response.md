
# Pin Change Response

*This model accepts additional fields of type Any.*

## Structure

`PinChangeResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status13`](../../doc/models/status-13.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.pin_change_response import PinChangeResponse
from adyen.models.status_13 import Status13

pin_change_response = PinChangeResponse(
    status=Status13.UNAVAILABLE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

