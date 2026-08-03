
# Processing Type 1

Contains information about how the payment was processed.

Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **purchaseWithCashback**, **recurring**, **token**.

## Enumeration

`ProcessingType1`

## Fields

| Name |
|  --- |
| `ATMWITHDRAW` |
| `BALANCEINQUIRY` |
| `ECOMMERCE` |
| `MOTO` |
| `POS` |
| `PURCHASEWITHCASHBACK` |
| `RECURRING` |
| `TOKEN` |

## Example

```python
from adyen.models.processing_type_1 import ProcessingType1

processing_type_1 = ProcessingType1.POS
```

