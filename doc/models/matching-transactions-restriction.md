
# Matching Transactions Restriction

*This model accepts additional fields of type Any.*

## Structure

`MatchingTransactionsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | The number of transactions. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.matching_transactions_restriction import MatchingTransactionsRestriction

matching_transactions_restriction = MatchingTransactionsRestriction(
    operation='operation8',
    value=76,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

