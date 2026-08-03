
# Rate Type 2

The type of transaction. Possible values:

* **splitPayment**: for payments
* **splitRefund**: for refunds

## Enumeration

`RateType2`

## Fields

| Name |
|  --- |
| `SPLITPAYMENT` |
| `BALANCECONVERSION` |
| `TRANSFER` |
| `SPLITREFUND` |

## Example

```python
from adyen.models.rate_type_2 import RateType2

rate_type_2 = RateType2.SPLITPAYMENT
```

