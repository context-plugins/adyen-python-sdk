
# Refund Funds Transfer Request

## Structure

`RefundFundsTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount to be transferred. |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |
| `original_reference` | `str` | Required | A PSP reference of the original fund transfer. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.refund_funds_transfer_request import RefundFundsTransferRequest

refund_funds_transfer_request = RefundFundsTransferRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    original_reference='originalReference4',
    merchant_reference='merchantReference6'
)
```

