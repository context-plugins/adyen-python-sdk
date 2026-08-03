
# Counterparty Types Restriction

*This model accepts additional fields of type Any.*

## Structure

`CounterpartyTypesRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value]`](../../doc/models/value.md) | Optional | The list of counterparty types to be evaluated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.counterparty_types_restriction import CounterpartyTypesRestriction
from adyen.models.value import Value

counterparty_types_restriction = CounterpartyTypesRestriction(
    operation='operation8',
    value=[
        Value.BALANCEACCOUNT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

