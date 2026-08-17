
# Patchable Amount DTO 1

The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated.

## Structure

`PatchableAmountDTO1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `int` | Optional | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |

## Example

```python
from adyen.models.patchable_amount_dto_1 import PatchableAmountDTO1

patchable_amount_dto_1 = PatchableAmountDTO1(
    currency='currency6',
    value=138
)
```

