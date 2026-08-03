
# Counterparty Types Restriction 1

Contains a list of counterparty types and how they must be evaluated.

Supported operations: **anyMatch**, **noneMatch**.

Supported value inputs:

- **balanceAccount**
- **bankAccount**
- **card**
- **transferInstrument**

*This model accepts additional fields of type Any.*

## Structure

`CounterpartyTypesRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | [`List[Value]`](../../doc/models/value.md) | Optional | The list of counterparty types to be evaluated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.counterparty_types_restriction_1 import CounterpartyTypesRestriction1
from adyen.models.value import Value

counterparty_types_restriction_1 = CounterpartyTypesRestriction1(
    operation='operation8',
    value=[
        Value.BALANCEACCOUNT,
        Value.BANKACCOUNT
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

