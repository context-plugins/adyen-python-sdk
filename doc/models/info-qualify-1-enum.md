
# Info Qualify 1 Enum

Qualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer. Allows the manager of the device, Sale or POI Terminal, to send the information to a particular physical device or to present the information accordingly.
Possible values:

* **CustomerAssistance**
* **Display**
* **Document**
* **Error**
* **Input**
* **POIReplication**
* **Receipt**
* **Sound**
* **Status**
* **Voucher**

## Enumeration

`InfoQualify1Enum`

## Fields

| Name |
|  --- |
| `STATUS` |
| `ERROR` |
| `DISPLAY` |
| `SOUND` |
| `INPUT` |
| `POIREPLICATION` |
| `CUSTOMERASSISTANCE` |
| `RECEIPT` |
| `DOCUMENT` |
| `VOUCHER` |

## Example

```python
from adyen.models.info_qualify_1_enum import InfoQualify1Enum

info_qualify_1 = InfoQualify1Enum.INPUT
```

