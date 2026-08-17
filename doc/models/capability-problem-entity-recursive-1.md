
# Capability Problem Entity Recursive 1

## Structure

`CapabilityProblemEntityRecursive1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs corresponding to the verification errors from capabilities. |
| `id` | `str` | Optional | - |
| `mtype` | [`Type311Enum`](../../doc/models/type-311-enum.md) | Optional | - |

## Example

```python
from adyen.models.capability_problem_entity_recursive_1 import CapabilityProblemEntityRecursive1
from adyen.models.type_311_enum import Type311Enum

capability_problem_entity_recursive_1 = CapabilityProblemEntityRecursive1(
    documents=[
        'documents7'
    ],
    id='id8',
    mtype=Type311Enum.LEGALENTITY
)
```

