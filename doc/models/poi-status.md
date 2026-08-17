
# POI Status

Indicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal.
State of a POI Terminal.

## Structure

`POIStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `global_status` | [`GlobalStatus1Enum`](../../doc/models/global-status-1-enum.md) | Required | Global status of a POI Server or POI Terminal.<br>Possible values:<br><br>* **Busy**<br>* **Maintenance**<br>* **OK**<br>* **Unreachable** |
| `security_ok_flag` | `bool` | Optional | Indicates if the security module of the POI is working and usable.<br>If security module present. |
| `pedok_flag` | `bool` | Optional | Indicates if the PED is working and usable.<br>If PED present. |
| `card_reader_ok_flag` | `bool` | Optional | Indicates if the card readers are working and usable.<br>If card reader device present. |
| `printer_status` | [`PrinterStatus1Enum`](../../doc/models/printer-status-1-enum.md) | Optional | Possible values:<br><br>* **NoPaper**<br>* **OK**<br>* **OutOfOrder**<br>* **PaperJam**<br>* **PaperLow** |
| `communication_ok_flag` | `bool` | Optional | Indicates if the communication infrastructure is working and usable.<br>If communication infrastructure present. |
| `fraud_prevention_flag` | `bool` | Optional | Indicates a suspicion of fraud by the POI System.<br>Could be set to True by the POI system to notify to the Sale system and the Cashier that a suspicion of fraud had been detected on the POI as an unexpected reboot of the POI. |

## Example

```python
from adyen.models.global_status_1_enum import GlobalStatus1Enum
from adyen.models.poi_status import POIStatus
from adyen.models.printer_status_1_enum import PrinterStatus1Enum

poi_status = POIStatus(
    global_status=GlobalStatus1Enum.OK,
    security_ok_flag=False,
    pedok_flag=False,
    card_reader_ok_flag=False,
    printer_status=PrinterStatus1Enum.NOPAPER,
    communication_ok_flag=False
)
```

