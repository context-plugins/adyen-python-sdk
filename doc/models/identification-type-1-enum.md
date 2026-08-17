
# Identification Type 1 Enum

Possible values:

* **PAN**
* **ISOTrack2**
* **BarCode**
* **AccountNumber**
* **PhoneNumber**

## Enumeration

`IdentificationType1Enum`

## Fields

| Name |
|  --- |
| `PAN` |
| `ISOTRACK2` |
| `BARCODE` |
| `ACCOUNTNUMBER` |
| `PHONENUMBER` |

## Example

```python
from adyen.models.identification_type_1_enum import IdentificationType1Enum

identification_type_1 = IdentificationType1Enum.ISOTRACK2
```

