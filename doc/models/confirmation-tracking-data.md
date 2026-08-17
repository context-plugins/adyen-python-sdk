
# Confirmation Tracking Data

## Structure

`ConfirmationTrackingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | [`Status15Enum`](../../doc/models/status-15-enum.md) | Required | The status of the transfer.<br><br>Possible values:<br><br>- **credited**: the funds are credited to your user's transfer instrument or bank account.- **accepted**: the request is accepted by the integration. |
| `mtype` | `str` | Required, Constant | The type of the tracking event.<br><br>Possible values:<br><br>- **confirmation**: the transfer passed Adyen's internal review.<br><br>**Value**: `"confirmation"` |

## Example

```python
from adyen.models.confirmation_tracking_data import ConfirmationTrackingData
from adyen.models.status_15_enum import Status15Enum

confirmation_tracking_data = ConfirmationTrackingData(
    status=Status15Enum.CREDITED
)
```

