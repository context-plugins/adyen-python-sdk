
# Tax Total

## Structure

`TaxTotal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Optional | - |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.tax_total import TaxTotal

tax_total = TaxTotal(
    amount=Amount(
        currency='currency2',
        value=110
    )
)
```

