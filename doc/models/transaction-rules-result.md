
# Transaction Rules Result

*This model accepts additional fields of type Any.*

## Structure

`TransactionRulesResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `advice` | `str` | Optional | The advice given by the Risk analysis. |
| `all_hard_block_rules_passed` | `bool` | Optional | Indicates whether the transaction passed the evaluation for all hardblock rules |
| `score` | `int` | Optional | The score of the Risk analysis. |
| `triggered_transaction_rules` | [`List[TransactionEventViolation]`](../../doc/models/transaction-event-violation.md) | Optional | Array containing all the transaction rules that the transaction triggered. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_event_violation import TransactionEventViolation
from adyen.models.transaction_rule_reference import TransactionRuleReference
from adyen.models.transaction_rule_source import TransactionRuleSource
from adyen.models.transaction_rules_result import TransactionRulesResult

transaction_rules_result = TransactionRulesResult(
    advice='advice8',
    all_hard_block_rules_passed=False,
    score=196,
    triggered_transaction_rules=[
        TransactionEventViolation(
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
        ),
        TransactionEventViolation(
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
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

