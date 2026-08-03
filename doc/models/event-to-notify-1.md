
# Event to Notify 1

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

`EventToNotify1`

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
from adyen.models.event_to_notify_1 import EventToNotify1

event_to_notify_1 = EventToNotify1.USEANOTHERCARDFORPREAUTH
```

