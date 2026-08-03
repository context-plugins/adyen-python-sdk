
# Entity Type 2

The type of the entity the payout is processed for.

Allowed values:

* NaturalPerson
* Company

> This field is required to update the existing `entityType` that is associated with this recurring contract.

## Enumeration

`EntityType2`

## Fields

| Name |
|  --- |
| `NATURALPERSON` |
| `COMPANY` |

## Example

```python
from adyen.models.entity_type_2 import EntityType2

entity_type_2 = EntityType2.NATURALPERSON
```

