
# Capability Problem Entity Recursive

*This model accepts additional fields of type Any.*

## Structure

`CapabilityProblemEntityRecursive`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs to which the verification errors related to the capabilities correspond to. |
| `id` | `str` | Optional | The ID of the entity. |
| `mtype` | [`Type3`](../../doc/models/type-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.type_3 import Type3

capability_problem_entity_recursive = CapabilityProblemEntityRecursive(
    documents=[
        'documents3'
    ],
    id='id4',
    mtype=Type3.BANKACCOUNT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

