
# Fee 2

## Structure

`Fee2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the amount of the grant fee. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.fee_2 import Fee2

fee_2 = Fee2(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

