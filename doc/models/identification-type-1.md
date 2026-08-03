
# Identification Type 1

Possible values:

* **PAN**
* **ISOTrack2**
* **BarCode**
* **AccountNumber**
* **PhoneNumber**

## Enumeration

`IdentificationType1`

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
from adyen.models.identification_type_1 import IdentificationType1

identification_type_1 = IdentificationType1.ISOTRACK2
```

