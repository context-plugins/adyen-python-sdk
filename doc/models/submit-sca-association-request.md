
# Submit Sca Association Request

*This model accepts additional fields of type Any.*

## Structure

`SubmitScaAssociationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entities` | [`List[ScaEntity]`](../../doc/models/sca-entity.md) | Required | The list of entities to be associated.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `5` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sca_entity import ScaEntity
from adyen.models.sca_entity_type_4 import ScaEntityType4
from adyen.models.submit_sca_association_request import SubmitScaAssociationRequest

submit_sca_association_request = SubmitScaAssociationRequest(
    entities=[
        ScaEntity(
            id='AH9999Z99Z999999ZZZZ9999Z',
            mtype=ScaEntityType4.ACCOUNTHOLDER,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

