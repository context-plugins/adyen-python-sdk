
# Capability Problem Entity

*This model accepts additional fields of type Any.*

## Structure

`CapabilityProblemEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs to which the verification errors related to the capabilities correspond to. |
| `id` | `str` | Optional | The ID of the entity. |
| `owner` | [`CapabilityProblemEntityRecursive`](../../doc/models/capability-problem-entity-recursive.md) | Optional | - |
| `mtype` | [`Type3`](../../doc/models/type-3.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability_problem_entity import CapabilityProblemEntity
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.type_3 import Type3

capability_problem_entity = CapabilityProblemEntity(
    documents=[
        'documents7',
        'documents8'
    ],
    id='id8',
    owner=CapabilityProblemEntityRecursive(
        documents=[
            'documents3',
            'documents4'
        ],
        id='id4',
        mtype=Type3.LEGALENTITY,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mtype=Type3.DOCUMENT,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

