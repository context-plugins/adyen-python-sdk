
# Check Data 2

*This model accepts additional fields of type Any.*

## Structure

`CheckData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_id` | `str` | Optional | Identification of the bank.<br>Mandatory if TrackData absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `account_number` | `str` | Optional | Identification of the customer account.<br>Mandatory if TrackData absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `check_number` | `str` | Optional | Identification of the bank check.<br>Mandatory if TrackData absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `track_data` | [`TrackData2`](../../doc/models/track-data-2.md) | Optional | - |
| `check_card_number` | `str` | Optional | Check guarantee card number.<br>If provided by the customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `type_code` | [`TypeCode1`](../../doc/models/type-code-1.md) | Optional | - |
| `country` | `str` | Optional | Country of the bank check.<br>Absent if country of the Sale system.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.check_data_2 import CheckData2
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1

check_data_2 = CheckData2(
    bank_id='BankID2',
    account_number='AccountNumber8',
    check_number='CheckNumber0',
    track_data=TrackData2(
        track_value='TrackValue6',
        track_numb=3,
        track_format=TrackFormat1.JISII,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    check_card_number='CheckCardNumber8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

