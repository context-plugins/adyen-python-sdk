
# Estimation Tracking Data

## Structure

`EstimationTrackingData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `estimated_arrival_time` | `datetime` | Required | The estimated time the beneficiary should have access to the funds. |
| `mtype` | `str` | Required, Constant | The type of tracking event.<br><br>Possible values:<br><br>- **estimation**: the estimated date and time of when the funds will be credited has been determined.<br><br>**Value**: `"estimation"` |

## Example

```python
import dateutil.parser

from adyen.models.estimation_tracking_data import EstimationTrackingData

estimation_tracking_data = EstimationTrackingData(
    estimated_arrival_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

