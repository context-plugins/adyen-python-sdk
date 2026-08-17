
# Same Amount Restriction 1

Checks if a user has recently sent the same amount of funds in multiple transfers.

To use this restriction, you must:

- Set the rule `type` to **velocity**.

- Specify a time `interval`.

- Specify a number of `matchingTransactions`.

Supported operation: **equals**.

## Structure

`SameAmountRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | - |

## Example

```python
from adyen.models.same_amount_restriction_1 import SameAmountRestriction1

same_amount_restriction_1 = SameAmountRestriction1(
    operation='operation6',
    value=False
)
```

