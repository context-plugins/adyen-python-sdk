
# Transaction Event Violation

*This model accepts additional fields of type Any.*

## Structure

`TransactionEventViolation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Optional | An explanation about why the transaction rule failed. |
| `transaction_rule` | [`TransactionRuleReference`](../../doc/models/transaction-rule-reference.md) | Optional | - |
| `transaction_rule_source` | [`TransactionRuleSource`](../../doc/models/transaction-rule-source.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_event_violation import TransactionEventViolation
from adyen.models.transaction_rule_reference import TransactionRuleReference
from adyen.models.transaction_rule_source import TransactionRuleSource

transaction_event_violation = TransactionEventViolation(
    reason='reason6',
    transaction_rule=TransactionRuleReference(
        description='description2',
        id='id2',
        outcome_type='outcomeType8',
        reference='reference2',
        score=68,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    transaction_rule_source=TransactionRuleSource(
        id='id4',
        mtype='type4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

