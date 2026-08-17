
# Track Data 1

Magnetic track or magnetic ink characters line.
Mandatory if CheckNumber absent.

## Structure

`TrackData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `track_numb` | `int` | Optional | Card track number.<br><br>**Default**: `2`<br><br>**Constraints**: `>= 1`, `<= 3` |
| `track_format` | [`TrackFormat1Enum`](../../doc/models/track-format-1-enum.md) | Optional | Card track format.<br>Possible values:<br><br>* **AAMVA**<br>* **ISO** |
| `track_value` | `str` | Required | Card track content.<br><br>**Constraints**: *Pattern*: `^.{1,104}$` |

## Example

```python
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum

track_data_1 = TrackData1(
    track_value='TrackValue4',
    track_numb=2,
    track_format=TrackFormat1Enum.CMC7
)
```

