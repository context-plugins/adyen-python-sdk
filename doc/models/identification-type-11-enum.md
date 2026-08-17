
# Identification Type 11 Enum

Type of account identification. In a request message, it informs the POI System the type of the account or card identification, when provided by the Sale Terminal. (e.g. because the card information is a barcode read by the Cashier on a scanner device). In a response message, it informs the Sale System the type of the account or card identification.
Possible values:

* **AccountNumber**
* **BarCode**
* **ISOTrack2**
* **PAN**
* **PhoneNumber**

## Enumeration

`IdentificationType11Enum`

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
from adyen.models.identification_type_11_enum import IdentificationType11Enum

identification_type_11 = IdentificationType11Enum.ACCOUNTNUMBER
```

