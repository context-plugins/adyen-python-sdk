
# Processing Type 1 Enum

Contains information about how the payment was processed.

Possible values: **atmWithdraw**, **balanceInquiry**, **ecommerce**, **moto**, **pos**, **purchaseWithCashback**, **recurring**, **token**.

## Enumeration

`ProcessingType1Enum`

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
from adyen.models.processing_type_1_enum import ProcessingType1Enum

processing_type_1 = ProcessingType1Enum.POS
```

