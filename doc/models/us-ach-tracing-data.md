
# Us Ach Tracing Data

*This model accepts additional fields of type Any.*

## Structure

`UsAchTracingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trace_number` | `str` | Required | The ACH trace number. This is a unique 15-digit identifier assigned to transfers processed by [ACH](https://fiscal.treasury.gov/payments-from-government/automated-clearing-house-ach). |
| `mtype` | [`Type89`](../../doc/models/type-89.md) | Required | **usAch** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_89 import Type89
from adyen.models.us_ach_tracing_data import UsAchTracingData

us_ach_tracing_data = UsAchTracingData(
    trace_number='traceNumber4',
    mtype=Type89.USACH,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

