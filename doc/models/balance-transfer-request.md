
# Balance Transfer Request

## Structure

`BalanceTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | The amount of the transfer. |
| `from_merchant` | `str` | Required | The unique identifier of the source merchant account from which funds are deducted.<br><br>**Constraints**: *Minimum Length*: `1` |
| `reference` | `str` | Optional | A reference for the balance transfer. Maximum length: 80 characters.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `80` |
| `to_merchant` | `str` | Required | The unique identifier of the destination merchant account to which funds are transferred.<br><br>**Constraints**: *Minimum Length*: `1` |
| `mtype` | [`BalanceTransferType2Enum`](../../doc/models/balance-transfer-type-2-enum.md) | Required | The type of balance transfer. Possible values: **tax**, **fee**, **terminalSale**, **credit**, **debit**, and **adjustment**. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.balance_transfer_request import BalanceTransferRequest
from adyen.models.balance_transfer_type_2_enum import BalanceTransferType2Enum

balance_transfer_request = BalanceTransferRequest(
    amount=Amount17(
        currency='currency2',
        value=110
    ),
    from_merchant='fromMerchant4',
    to_merchant='toMerchant4',
    mtype=BalanceTransferType2Enum.DEBIT,
    reference='reference8'
)
```

