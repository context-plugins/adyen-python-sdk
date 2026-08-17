
# Sensitive Card Data 1

Sensitive information related to the payment card, entered or read by the Sale System.
If structure non empty and unprotected.

## Structure

`SensitiveCardData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pan` | `int` | Optional | Primary Account Number.<br><br>**Constraints**: `>= 8`, `<= 28` |
| `card_seq_numb` | `int` | Optional | Card Sequence Number.<br>If EntryMode is File, Keyed, or Manual.<br><br>**Constraints**: `>= 2`, `<= 3` |
| `expiry_date` | `int` | Optional | Date after which the card cannot be used.<br>If EntryMode is File.<br><br>**Constraints**: `>= 4`, `<= 4` |
| `track_data` | [`List[TrackData]`](../../doc/models/track-data.md) | Optional | Magnetic track or magnetic ink characters line.<br>If EntryMode is MagStripe or RFID . |

## Example

```python
from adyen.models.sensitive_card_data_1 import SensitiveCardData1
from adyen.models.track_data import TrackData
from adyen.models.track_format_1_enum import TrackFormat1Enum

sensitive_card_data_1 = SensitiveCardData1(
    pan=28,
    card_seq_numb=3,
    expiry_date=4,
    track_data=[
        TrackData(
            track_value='TrackValue6',
            track_numb=3,
            track_format=TrackFormat1Enum.JISII
        ),
        TrackData(
            track_value='TrackValue6',
            track_numb=3,
            track_format=TrackFormat1Enum.JISII
        )
    ]
)
```

