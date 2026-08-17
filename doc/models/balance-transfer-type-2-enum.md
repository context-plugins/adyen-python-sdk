
# Balance Transfer Type 2 Enum

The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and **adjustment**.

## Enumeration

`BalanceTransferType2Enum`

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
from adyen.models.balance_transfer_type_2_enum import BalanceTransferType2Enum

balance_transfer_type_2 = BalanceTransferType2Enum.DEBIT
```

