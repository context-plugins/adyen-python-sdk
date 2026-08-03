
# Transaction Rule Reference

*This model accepts additional fields of type Any.*

## Structure

`TransactionRuleReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `outcome_type` | `str` | Optional | The outcome type of the rule. |
| `reference` | `str` | Optional | The reference for the resource. |
| `score` | `int` | Optional | The transaction score determined by the rule. Returned only when `outcomeType` is **scoreBased**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transaction_rule_reference import TransactionRuleReference

transaction_rule_reference = TransactionRuleReference(
    description='description4',
    id='id4',
    outcome_type='outcomeType0',
    reference='reference0',
    score=24,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

