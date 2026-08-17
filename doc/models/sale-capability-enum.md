
# Sale Capability Enum

## Enumeration

`SaleCapabilityEnum`

## Fields

| Name |
|  --- |
| `CASHIERSTATUS` |
| `CASHIERERROR` |
| `CASHIERDISPLAY` |
| `POIREPLICATION` |
| `CASHIERINPUT` |
| `CUSTOMERASSISTANCE` |
| `CUSTOMERDISPLAY` |
| `CUSTOMERERROR` |
| `CUSTOMERINPUT` |
| `PRINTERRECEIPT` |
| `PRINTERDOCUMENT` |
| `PRINTERVOUCHER` |
| `MAGSTRIPE` |
| `ICC` |
| `EMVCONTACTLESS` |

## Example

```python
from adyen.models.sale_capability_enum import SaleCapabilityEnum

sale_capability = SaleCapabilityEnum.CUSTOMERDISPLAY
```

