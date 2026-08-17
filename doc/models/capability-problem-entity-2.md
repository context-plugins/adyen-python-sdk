
# Capability Problem Entity 2

Contains the type of the entity and the corresponding ID.

## Structure

`CapabilityProblemEntity2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs to which the verification errors related to the capabilities correspond to. |
| `id` | `str` | Optional | The ID of the entity. |
| `owner` | [`CapabilityProblemEntityRecursive2`](../../doc/models/capability-problem-entity-recursive-2.md) | Optional | Contains details about the owner of the entity that has an error. |
| `mtype` | [`Type33Enum`](../../doc/models/type-33-enum.md) | Optional | Type of entity.<br><br>Possible values: **LegalEntity**, **BankAccount**, **Document**. |

## Example

```python
from adyen.models.capability_problem_entity_2 import CapabilityProblemEntity2
from adyen.models.capability_problem_entity_recursive_2 import CapabilityProblemEntityRecursive2
from adyen.models.type_33_enum import Type33Enum

capability_problem_entity_2 = CapabilityProblemEntity2(
    documents=[
        'documents5',
        'documents6',
        'documents7'
    ],
    id='id6',
    owner=CapabilityProblemEntityRecursive2(
        documents=[
            'documents3',
            'documents4'
        ],
        id='id4',
        mtype=Type33Enum.LEGALENTITY
    ),
    mtype=Type33Enum.LEGALENTITY
)
```

