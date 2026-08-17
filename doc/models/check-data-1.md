
# Check Data 1

Information related to the paper check used for the transaction.
If PaymentInstrumentType is Check.

## Structure

`CheckData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_id` | `str` | Optional | Identification of the bank.<br>Mandatory if TrackData absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `account_number` | `str` | Optional | Identification of the customer account.<br>Mandatory if TrackData absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `check_number` | `str` | Optional | Identification of the bank check.<br>Mandatory if TrackData absent.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `track_data` | [`TrackData1`](../../doc/models/track-data-1.md) | Optional | Magnetic track or magnetic ink characters line.<br>Mandatory if CheckNumber absent. |
| `check_card_number` | `str` | Optional | Check guarantee card number.<br>If provided by the customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `type_code` | [`TypeCode1Enum`](../../doc/models/type-code-1-enum.md) | Optional | Type of bank check.<br>Possible values:<br><br>* **Company**<br>* **Personal** |
| `country` | `str` | Optional | Country of the bank check.<br>Absent if country of the Sale system.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |

## Example

```python
from adyen.models.check_data_1 import CheckData1
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum

check_data_1 = CheckData1(
    bank_id='BankID8',
    account_number='AccountNumber4',
    check_number='CheckNumber4',
    track_data=TrackData1(
        track_value='TrackValue6',
        track_numb=3,
        track_format=TrackFormat1Enum.JISII
    ),
    check_card_number='CheckCardNumber4'
)
```

