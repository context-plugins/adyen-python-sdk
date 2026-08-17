
# Fee

## Structure

`Fee`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the fee amount. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.fee import Fee

fee = Fee(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

