
# Track Data 1

Magnetic track or magnetic ink characters line.
Mandatory if CheckNumber absent.

*This model accepts additional fields of type Any.*

## Structure

`TrackData1`

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

from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1 import TrackFormat1

track_data_1 = TrackData1(
    track_value='TrackValue4',
    track_numb=2,
    track_format=TrackFormat1.CMC7,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

