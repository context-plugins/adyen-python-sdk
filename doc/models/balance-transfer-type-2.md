
# Balance Transfer Type 2

The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and **adjustment**.

## Enumeration

`BalanceTransferType2`

## Fields

| Name |
|  --- |
| `TAX` |
| `FEE` |
| `TERMINALSALE` |
| `CREDIT` |
| `DEBIT` |
| `ADJUSTMENT` |

## Example

```python
from adyen.models.balance_transfer_type_2 import BalanceTransferType2

balance_transfer_type_2 = BalanceTransferType2.DEBIT
```

