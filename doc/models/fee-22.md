
# Fee 22

Contains information about the fee that your user must pay for the disbursement.

## Structure

`Fee22`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the amount of the grant fee. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.fee_22 import Fee22

fee_22 = Fee22(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

