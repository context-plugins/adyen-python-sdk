
# Amount Min Max Requirement

## Structure

`AmountMinMaxRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the eligible amounts for a particular route. |
| `max` | `int` | Optional | Maximum amount. |
| `min` | `int` | Optional | Minimum amount. |
| `mtype` | `str` | Required, Constant | **amountMinMaxRequirement**<br><br>**Value**: `"amountMinMaxRequirement"` |

## Example

```python
from adyen.models.amount_min_max_requirement import AmountMinMaxRequirement

amount_min_max_requirement = AmountMinMaxRequirement(
    description='description6',
    max=222,
    min=48
)
```

