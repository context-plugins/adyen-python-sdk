
# Same Counterparty Restriction 1

Checks if a user has recently made multiple transfers to the same counterparty.

To use this restriction, you must:

- Set the rule `type` to **velocity**.

- Specify a time `interval`.

- Specify a number of `matchingTransactions`.

Supported operations: **equals**.

*This model accepts additional fields of type Any.*

## Structure

`SameCounterpartyRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.same_counterparty_restriction_1 import SameCounterpartyRestriction1

same_counterparty_restriction_1 = SameCounterpartyRestriction1(
    operation='operation6',
    value=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

