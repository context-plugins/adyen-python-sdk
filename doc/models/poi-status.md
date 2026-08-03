
# Poi Status

Indicate the availability of the POI Terminal components. The data element is absent if the component is not part of the POI Terminal.
State of a POI Terminal.

*This model accepts additional fields of type Any.*

## Structure

`PoiStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `global_status` | [`GlobalStatus1`](../../doc/models/global-status-1.md) | Required | - |
| `security_ok_flag` | `bool` | Optional | Indicates if the security module of the POI is working and usable.<br>If security module present. |
| `pedok_flag` | `bool` | Optional | Indicates if the PED is working and usable.<br>If PED present. |
| `card_reader_ok_flag` | `bool` | Optional | Indicates if the card readers are working and usable.<br>If card reader device present. |
| `printer_status` | [`PrinterStatus1`](../../doc/models/printer-status-1.md) | Optional | - |
| `communication_ok_flag` | `bool` | Optional | Indicates if the communication infrastructure is working and usable.<br>If communication infrastructure present. |
| `fraud_prevention_flag` | `bool` | Optional | Indicates a suspicion of fraud by the POI System.<br>Could be set to True by the POI system to notify to the Sale system and the Cashier that a suspicion of fraud had been detected on the POI as an unexpected reboot of the POI. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.global_status_1 import GlobalStatus1
from adyen.models.poi_status import PoiStatus
from adyen.models.printer_status_1 import PrinterStatus1

poi_status = PoiStatus(
    global_status=GlobalStatus1.OK,
    security_ok_flag=False,
    pedok_flag=False,
    card_reader_ok_flag=False,
    printer_status=PrinterStatus1.NOPAPER,
    communication_ok_flag=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

