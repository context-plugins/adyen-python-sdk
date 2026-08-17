
# Internal Review Tracking Data

## Structure

`InternalReviewTrackingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | [`Reason11Enum`](../../doc/models/reason-11-enum.md) | Optional | The reason why the transfer failed Adyen's internal review.<br><br>Possible values:<br><br>- **refusedForRegulatoryReasons**: the transfer does not comply with Adyen's risk policy. For more information, [contact the Support Team](https://www.adyen.help/hc/en-us/requests/new). |
| `status` | [`Status44Enum`](../../doc/models/status-44-enum.md) | Required | The status of the transfer.<br><br>Possible values:<br><br>- **pending**: the transfer is under internal review by Adyen.<br><br>- **failed**: the transfer failed Adyen's internal review. For details, see `reason`. |
| `mtype` | `str` | Required, Constant | The type of tracking event.<br><br>Possible values:<br><br>- **internalReview**: the transfer was flagged because it does not comply with Adyen's risk policy.<br><br>**Value**: `"internalReview"` |

## Example

```python
from adyen.models.internal_review_tracking_data import InternalReviewTrackingData
from adyen.models.reason_11_enum import Reason11Enum
from adyen.models.status_44_enum import Status44Enum

internal_review_tracking_data = InternalReviewTrackingData(
    status=Status44Enum.PENDING,
    reason=Reason11Enum.REFUSEDFORREGULATORYREASONS
)
```

