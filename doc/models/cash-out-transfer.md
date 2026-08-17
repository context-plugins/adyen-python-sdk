
# Cash Out Transfer

## Structure

`CashOutTransfer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The amount of the cashout instruction transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `id` | `str` | Required | The reference of the cashout transfer. |
| `mtype` | [`Type121Enum`](../../doc/models/type-121-enum.md) | Required | The type of the cashout transfer.<br><br>Possible values:<br><br>- **cashoutRepayment**: Corresponds to the transfer created to deduct the cashout amount after settlement.<br>- **cashoutFee**: Corresponds to the transfer created to debit the cashout fee form the user's balance account. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.cash_out_transfer import CashOutTransfer
from adyen.models.type_121_enum import Type121Enum

cash_out_transfer = CashOutTransfer(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    id='id6',
    mtype=Type121Enum.CASHOUTREPAYMENT
)
```

