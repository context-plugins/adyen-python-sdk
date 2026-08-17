
# Fee 4

An object containing the fee currency and value, in [minor units](https://docs.adyen.com/development-resources/currency-codes).

## Structure

`Fee4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount17`](../../doc/models/amount-17.md) | Required | Contains the fee amount. |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.fee_4 import Fee4

fee_4 = Fee4(
    amount=Amount17(
        currency='currency2',
        value=110
    )
)
```

