
# Tax Total 2

Total tax amount from the order.

## Structure

`TaxTotal2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Optional | - |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.tax_total_2 import TaxTotal2

tax_total_2 = TaxTotal2(
    amount=Amount(
        currency='currency2',
        value=110
    )
)
```

