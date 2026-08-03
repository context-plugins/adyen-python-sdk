
# Sca Entity

*This model accepts additional fields of type Any.*

## Structure

`ScaEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `100` |
| `mtype` | [`ScaEntityType4`](../../doc/models/sca-entity-type-4.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sca_entity import ScaEntity
from adyen.models.sca_entity_type_4 import ScaEntityType4

sca_entity = ScaEntity(
    id='AH9999Z99Z999999ZZZZ9999Z',
    mtype=ScaEntityType4.LEGALENTITY,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

