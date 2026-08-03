
# Same Counterparty Restriction

*This model accepts additional fields of type Any.*

## Structure

`SameCounterpartyRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.same_counterparty_restriction import SameCounterpartyRestriction

same_counterparty_restriction = SameCounterpartyRestriction(
    operation='operation0',
    value=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

