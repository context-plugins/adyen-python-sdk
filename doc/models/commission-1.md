
# Commission 1

Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. The commission is booked to your platform's liable balance account.

## Structure

`Commission1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed_amount` | `int` | Optional | A fixed commission fee, in minor units. |
| `variable_percentage` | `int` | Optional | A variable commission fee, in basis points. |

## Example

```python
from adyen.models.commission_1 import Commission1

commission_1 = Commission1(
    fixed_amount=18,
    variable_percentage=182
)
```

