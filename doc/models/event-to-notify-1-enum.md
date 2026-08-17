
# Event to Notify 1 Enum

Event the POI notifies to the Sale System.
Possible values:

* **Abort**
* **BeginMaintenance**
* **CardInserted**
* **CardRemoved**
* **Completed**
* **CustomerLanguage**
* **EndMaintenance**
* **Initialised**
* **KeyPressed**
* **OutOfOrder**
* **Reject**
* **SaleAdmin**
* **SaleWakeUp**
* **ScanBarcodeResult**
* **SecurityAlarm**
* **Shutdown**
* **StopAssistance**
* **UseAnotherCardForPreauth**

## Enumeration

`EventToNotify1Enum`

## Fields

| Name |
|  --- |
| `BEGINMAINTENANCE` |
| `ENDMAINTENANCE` |
| `SHUTDOWN` |
| `INITIALISED` |
| `OUTOFORDER` |
| `COMPLETED` |
| `ABORT` |
| `SALEWAKEUP` |
| `SALEADMIN` |
| `CUSTOMERLANGUAGE` |
| `KEYPRESSED` |
| `SECURITYALARM` |
| `STOPASSISTANCE` |
| `CARDINSERTED` |
| `CARDREMOVED` |
| `REJECT` |
| `USEANOTHERCARDFORPREAUTH` |
| `SCANBARCODERESULT` |

## Example

```python
from adyen.models.event_to_notify_1_enum import EventToNotify1Enum

event_to_notify_1 = EventToNotify1Enum.USEANOTHERCARDFORPREAUTH
```

