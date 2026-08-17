
# Capability Problem Entity Recursive

## Structure

`CapabilityProblemEntityRecursive`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `documents` | `List[str]` | Optional | List of document IDs to which the verification errors related to the capabilities correspond to. |
| `id` | `str` | Optional | The ID of the entity. |
| `mtype` | [`Type33Enum`](../../doc/models/type-33-enum.md) | Optional | Type of entity.<br><br>Possible values: **LegalEntity**, **BankAccount**, **Document**. |

## Example

```python
from adyen.models.capability_problem_entity_recursive import CapabilityProblemEntityRecursive
from adyen.models.type_33_enum import Type33Enum

capability_problem_entity_recursive = CapabilityProblemEntityRecursive(
    documents=[
        'documents3'
    ],
    id='id4',
    mtype=Type33Enum.BANKACCOUNT
)
```

