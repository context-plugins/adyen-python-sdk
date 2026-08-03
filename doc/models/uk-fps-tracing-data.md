
# Uk Fps Tracing Data

*This model accepts additional fields of type Any.*

## Structure

`UkFpsTracingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fpid` | `str` | Required | The FPS trace number. This is a unique identifier assigned to transfers processed by [FPS](https://www.bankofengland.co.uk/payment-systems/services/faster-payments-service). |
| `mtype` | [`Type88`](../../doc/models/type-88.md) | Required | **ukFps** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_88 import Type88
from adyen.models.uk_fps_tracing_data import UkFpsTracingData

uk_fps_tracing_data = UkFpsTracingData(
    fpid='fpid0',
    mtype=Type88.UKFPS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

