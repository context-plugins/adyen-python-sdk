
# Capability Problem Entity Recursive 2

Contains details about the owner of the entity that has an error.

*This model accepts additional fields of type Any.*

## Structure

`CapabilityProblemEntityRecursive2`

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

from adyen.models.capability_problem_entity_recursive_2 import CapabilityProblemEntityRecursive2
from adyen.models.type_3 import Type3

capability_problem_entity_recursive_2 = CapabilityProblemEntityRecursive2(
    documents=[
        'documents1',
        'documents2'
    ],
    id='id2',
    mtype=Type3.LEGALENTITY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

