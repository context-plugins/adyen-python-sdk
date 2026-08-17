
# Fee 21

Contains the currency and value of the cashout fee, in [minor units](https://docs.adyen.com/development-resources/currency-codes).

## Structure

`Fee21`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the fee amount. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.fee_21 import Fee21

fee_21 = Fee21(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

