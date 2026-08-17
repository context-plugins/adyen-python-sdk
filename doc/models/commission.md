
# Commission

## Structure

`Commission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed_amount` | `int` | Optional | A fixed commission fee, in minor units. |
| `variable_percentage` | `int` | Optional | A variable commission fee, in basis points. |

## Example

```python
from adyen.models.commission import Commission

commission = Commission(
    fixed_amount=112,
    variable_percentage=52
)
```

