
# Top Up Amount 1

The currency and value to be added to the balance account, specified in minor units. This can be a fixed amount or a target amount.

## Structure

`TopUpAmount1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The fixed amount with which you want to top up the balance account. |
| `target` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The target balance for the balance account that the top-up must achieve. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.top_up_amount_1 import TopUpAmount1

top_up_amount_1 = TopUpAmount1(
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

