
# Event to Notify

Event the POI notifies to the Sale System.
Possible values:

* **BeginMaintenance**
* **EndMaintenance**
* **Shutdown**
* **Initialised**
* **OutOfOrder**
* **Completed**
* **Abort**
* **SaleWakeUp**
* **SaleAdmin**
* **CustomerLanguage**
* **KeyPressed**
* **SecurityAlarm**
* **StopAssistance**
* **CardInserted**
* **CardRemoved**
* **Reject**
* **UseAnotherCardForPreauth**
* **ScanBarcodeResult**

## Enumeration

`EventToNotify`

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
from adyen.models.event_to_notify import EventToNotify

event_to_notify = EventToNotify.USEANOTHERCARDFORPREAUTH
```

