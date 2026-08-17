
# Capability Problem Entity 1

## Structure

`CapabilityProblemEntity1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs corresponding to the verification errors from capabilities. |
| `id` | `str` | Optional | - |
| `owner` | [`CapabilityProblemEntityRecursive1`](../../doc/models/capability-problem-entity-recursive-1.md) | Optional | - |
| `mtype` | [`Type311Enum`](../../doc/models/type-311-enum.md) | Optional | - |

## Example

```python
from adyen.models.capability_problem_entity_1 import CapabilityProblemEntity1
from adyen.models.capability_problem_entity_recursive_1 import CapabilityProblemEntityRecursive1
from adyen.models.type_311_enum import Type311Enum

capability_problem_entity_1 = CapabilityProblemEntity1(
    documents=[
        'documents1'
    ],
    id='id2',
    owner=CapabilityProblemEntityRecursive1(
        documents=[
            'documents3',
            'documents4'
        ],
        id='id4',
        mtype=Type311Enum.LEGALENTITY
    ),
    mtype=Type311Enum.LEGALENTITY
)
```

