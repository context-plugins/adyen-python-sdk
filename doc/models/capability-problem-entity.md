
# Capability Problem Entity

## Structure

`CapabilityProblemEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs to which the verification errors related to the capabilities correspond to. |
| `id` | `str` | Optional | The ID of the entity. |
| `owner` | [`CapabilityProblemEntityRecursive2`](../../doc/models/capability-problem-entity-recursive-2.md) | Optional | Contains details about the owner of the entity that has an error. |
| `mtype` | [`Type33Enum`](../../doc/models/type-33-enum.md) | Optional | Type of entity.<br><br>Possible values: **LegalEntity**, **BankAccount**, **Document**. |

## Example

```python
from adyen.models.capability_problem_entity import CapabilityProblemEntity
from adyen.models.capability_problem_entity_recursive_2 import CapabilityProblemEntityRecursive2
from adyen.models.type_33_enum import Type33Enum

capability_problem_entity = CapabilityProblemEntity(
    documents=[
        'documents7',
        'documents8'
    ],
    id='id8',
    owner=CapabilityProblemEntityRecursive2(
        documents=[
            'documents3',
            'documents4'
        ],
        id='id4',
        mtype=Type33Enum.LEGALENTITY
    ),
    mtype=Type33Enum.DOCUMENT
)
```

