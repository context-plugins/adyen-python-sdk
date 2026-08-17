
# Event to Notify Enum

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

`EventToNotifyEnum`

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
from adyen.models.event_to_notify_enum import EventToNotifyEnum

event_to_notify = EventToNotifyEnum.USEANOTHERCARDFORPREAUTH
```

