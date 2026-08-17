
# Matching Transactions Restriction

## Structure

`MatchingTransactionsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | The number of transactions. |

## Example

```python
from adyen.models.matching_transactions_restriction import MatchingTransactionsRestriction

matching_transactions_restriction = MatchingTransactionsRestriction(
    operation='operation8',
    value=76
)
```

