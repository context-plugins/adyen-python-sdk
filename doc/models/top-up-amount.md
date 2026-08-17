
# Top Up Amount

## Structure

`TopUpAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The fixed amount with which you want to top up the balance account. |
| `target` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The target balance for the balance account that the top-up must achieve. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.top_up_amount import TopUpAmount

top_up_amount = TopUpAmount(
    fixed=Amount17(
        currency='currency0',
        value=164
    ),
    target=Amount17(
        currency='currency2',
        value=188
    )
)
```

