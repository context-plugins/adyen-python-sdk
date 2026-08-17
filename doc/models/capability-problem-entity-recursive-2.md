
# Capability Problem Entity Recursive 2

Contains details about the owner of the entity that has an error.

## Structure

`CapabilityProblemEntityRecursive2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs to which the verification errors related to the capabilities correspond to. |
| `id` | `str` | Optional | The ID of the entity. |
| `mtype` | [`Type33Enum`](../../doc/models/type-33-enum.md) | Optional | Type of entity.<br><br>Possible values: **LegalEntity**, **BankAccount**, **Document**. |

## Example

```python
from adyen.models.capability_problem_entity_recursive_2 import CapabilityProblemEntityRecursive2
from adyen.models.type_33_enum import Type33Enum

capability_problem_entity_recursive_2 = CapabilityProblemEntityRecursive2(
    documents=[
        'documents1',
        'documents2'
    ],
    id='id2',
    mtype=Type33Enum.LEGALENTITY
)
```

