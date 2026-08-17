
# Info Qualify 2 Enum

Qualification of the information to send to an output logical device, to display or print to the Cashier or the Customer.
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

`InfoQualify2Enum`

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
from adyen.models.info_qualify_2_enum import InfoQualify2Enum

info_qualify_2 = InfoQualify2Enum.CUSTOMERASSISTANCE
```

