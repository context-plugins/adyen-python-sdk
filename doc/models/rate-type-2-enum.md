
# Rate Type 2 Enum

The type of transaction. Possible values:

* **splitPayment**: for payments
* **splitRefund**: for refunds

## Enumeration

`RateType2Enum`

## Fields

| Name |
|  --- |
| `SPLITPAYMENT` |
| `BALANCECONVERSION` |
| `TRANSFER` |
| `SPLITREFUND` |

## Example

```python
from adyen.models.rate_type_2_enum import RateType2Enum

rate_type_2 = RateType2Enum.SPLITPAYMENT
```

