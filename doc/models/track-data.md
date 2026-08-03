
# Track Data

Magnetic track or magnetic ink characters line.
ISO 7813 - ISO 4909.
Generic data structure for a card track, used when the magstripe card reader is located on the Sale Terminal, or for magstripe Card Reader device request. The data structure is also used to store the line at the bottom of a bank check.

*This model accepts additional fields of type Any.*

## Structure

`TrackData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `track_numb` | `int` | Optional | Card track number.<br><br>**Default**: `2`<br><br>**Constraints**: `>= 1`, `<= 3` |
| `track_format` | [`TrackFormat1`](../../doc/models/track-format-1.md) | Optional | - |
| `track_value` | `str` | Required | Card track content.<br><br>**Constraints**: *Pattern*: `^.{1,104}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.track_data import TrackData
from adyen.models.track_format_1 import TrackFormat1

track_data = TrackData(
    track_value='TrackValue2',
    track_numb=2,
    track_format=TrackFormat1.CMC7,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

