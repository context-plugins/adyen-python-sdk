
# Transaction Rule Reference 2

Contains information about the transaction rule.

## Structure

`TransactionRuleReference2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `outcome_type` | `str` | Optional | The outcome type of the rule. |
| `reference` | `str` | Optional | The reference for the resource. |
| `score` | `int` | Optional | The transaction score determined by the rule. Returned only when `outcomeType` is **scoreBased**. |

## Example

```python
from adyen.models.transaction_rule_reference_2 import TransactionRuleReference2

transaction_rule_reference_2 = TransactionRuleReference2(
    description='description6',
    id='id4',
    outcome_type='outcomeType0',
    reference='reference0',
    score=160
)
```

