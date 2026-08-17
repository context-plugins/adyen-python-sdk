
# Entity Type 2 Enum

The type of the entity the payout is processed for.

Allowed values:

* NaturalPerson
* Company

> This field is required to update the existing `entityType` that is associated with this recurring contract.

## Enumeration

`EntityType2Enum`

## Fields

| Name |
|  --- |
| `NATURALPERSON` |
| `COMPANY` |

## Example

```python
from adyen.models.entity_type_2_enum import EntityType2Enum

entity_type_2 = EntityType2Enum.NATURALPERSON
```

