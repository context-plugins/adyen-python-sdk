
# Transaction Event Violation

## Structure

`TransactionEventViolation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | An explanation about why the transaction rule failed. |
| `transaction_rule` | [`TransactionRuleReference2`](../../doc/models/transaction-rule-reference-2.md) | Optional | Contains information about the transaction rule. |
| `transaction_rule_source` | [`TransactionRuleSource2`](../../doc/models/transaction-rule-source-2.md) | Optional | Contains information about the resource to which the transaction rule applies. |

## Example

```python
from adyen.models.transaction_event_violation import TransactionEventViolation
from adyen.models.transaction_rule_reference_2 import TransactionRuleReference2
from adyen.models.transaction_rule_source_2 import TransactionRuleSource2

transaction_event_violation = TransactionEventViolation(
    reason='reason6',
    transaction_rule=TransactionRuleReference2(
        description='description2',
        id='id2',
        outcome_type='outcomeType8',
        reference='reference2',
        score=68
    ),
    transaction_rule_source=TransactionRuleSource2(
        id='id4',
        mtype='type4'
    )
)
```

