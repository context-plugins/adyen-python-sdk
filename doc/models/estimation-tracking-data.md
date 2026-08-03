
# Estimation Tracking Data

*This model accepts additional fields of type Any.*

## Structure

`EstimationTrackingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_arrival_time` | `datetime` | Required | The estimated time the beneficiary should have access to the funds. |
| `mtype` | [`Type84`](../../doc/models/type-84.md) | Required | The type of tracking event.<br><br>Possible values:<br><br>- **estimation**: the estimated date and time of when the funds will be credited has been determined. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.estimation_tracking_data import EstimationTrackingData
from adyen.models.type_84 import Type84

estimation_tracking_data = EstimationTrackingData(
    estimated_arrival_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    mtype=Type84.ESTIMATION,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

