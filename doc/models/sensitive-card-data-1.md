
# Sensitive Card Data 1

Sensitive information related to the payment card, entered or read by the Sale System.
If structure non empty and unprotected.

*This model accepts additional fields of type Any.*

## Structure

`SensitiveCardData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pan` | `int` | Optional | Primary Account Number.<br><br>**Constraints**: `>= 8`, `<= 28` |
| `card_seq_numb` | `int` | Optional | Card Sequence Number.<br>If EntryMode is File, Keyed, or Manual.<br><br>**Constraints**: `>= 2`, `<= 3` |
| `expiry_date` | `int` | Optional | Date after which the card cannot be used.<br>If EntryMode is File.<br><br>**Constraints**: `>= 4`, `<= 4` |
| `track_data` | [`List[TrackData]`](../../doc/models/track-data.md) | Optional | Magnetic track or magnetic ink characters line.<br>If EntryMode is MagStripe or RFID . |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sensitive_card_data_1 import SensitiveCardData1
from adyen.models.track_data import TrackData
from adyen.models.track_format_1 import TrackFormat1

sensitive_card_data_1 = SensitiveCardData1(
    pan=28,
    card_seq_numb=3,
    expiry_date=4,
    track_data=[
        TrackData(
            track_value='TrackValue6',
            track_numb=3,
            track_format=TrackFormat1.JISII,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TrackData(
            track_value='TrackValue6',
            track_numb=3,
            track_format=TrackFormat1.JISII,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

