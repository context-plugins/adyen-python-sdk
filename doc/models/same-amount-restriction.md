
# Same Amount Restriction

## Structure

`SameAmountRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | - |

## Example

```python
from adyen.models.same_amount_restriction import SameAmountRestriction

same_amount_restriction = SameAmountRestriction(
    operation='operation0',
    value=False
)
```

