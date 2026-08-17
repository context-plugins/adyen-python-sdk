
# Info Qualify 3 Enum

Qualification of the information to sent to an output logical device, to display or print to the Cashier or the Customer.
Copy.
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

`InfoQualify3Enum`

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
from adyen.models.info_qualify_3_enum import InfoQualify3Enum

info_qualify_3 = InfoQualify3Enum.DOCUMENT
```

