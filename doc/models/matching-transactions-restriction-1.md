
# Matching Transactions Restriction 1

The number of transactions and the operation.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

## Structure

`MatchingTransactionsRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | The number of transactions. |

## Example

```python
from adyen.models.matching_transactions_restriction_1 import MatchingTransactionsRestriction1

matching_transactions_restriction_1 = MatchingTransactionsRestriction1(
    operation='operation0',
    value=4
)
```

