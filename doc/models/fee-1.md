
# Fee 1

Details of the fee configuration.

## Structure

`Fee1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the fee amount. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.fee_1 import Fee1

fee_1 = Fee1(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

