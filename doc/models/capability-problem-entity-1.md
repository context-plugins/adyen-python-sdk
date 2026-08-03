
# Capability Problem Entity 1

*This model accepts additional fields of type Any.*

## Structure

`CapabilityProblemEntity1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs corresponding to the verification errors from capabilities. |
| `id` | `str` | Optional | - |
| `owner` | [`CapabilityProblemEntityRecursive`](../../doc/models/capability-problem-entity-recursive.md) | Optional | - |
| `mtype` | [`Type32`](../../doc/models/type-32.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.capability_problem_entity_1 import CapabilityProblemEntity1
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.type_3 import Type3
from adyen.models.type_32 import Type32

capability_problem_entity_1 = CapabilityProblemEntity1(
    documents=[
        'documents1'
    ],
    id='id2',
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
    mtype=Type32.LEGALENTITY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

