
# Confirmation Tracking Data

*This model accepts additional fields of type Any.*

## Structure

`ConfirmationTrackingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status110`](../../doc/models/status-110.md) | Required | - |
| `mtype` | [`Type834`](../../doc/models/type-834.md) | Required | The type of the tracking event.<br><br>Possible values:<br><br>- **confirmation**: the transfer passed Adyen's internal review. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.confirmation_tracking_data import ConfirmationTrackingData
from adyen.models.status_110 import Status110
from adyen.models.type_834 import Type834

confirmation_tracking_data = ConfirmationTrackingData(
    status=Status110.CREDITED,
    mtype=Type834.CONFIRMATION,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

