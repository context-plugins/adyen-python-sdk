
# Internal Review Tracking Data

*This model accepts additional fields of type Any.*

## Structure

`InternalReviewTrackingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`Reason11`](../../doc/models/reason-11.md) | Optional | - |
| `status` | [`Status44`](../../doc/models/status-44.md) | Required | - |
| `mtype` | [`Type90`](../../doc/models/type-90.md) | Required | The type of tracking event.<br><br>Possible values:<br><br>- **internalReview**: the transfer was flagged because it does not comply with Adyen's risk policy. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.internal_review_tracking_data import InternalReviewTrackingData
from adyen.models.reason_11 import Reason11
from adyen.models.status_44 import Status44
from adyen.models.type_90 import Type90

internal_review_tracking_data = InternalReviewTrackingData(
    status=Status44.PENDING,
    mtype=Type90.INTERNALREVIEW,
    reason=Reason11.REFUSEDFORREGULATORYREASONS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

