
# Remove Association Request

*This model accepts additional fields of type Any.*

## Structure

`RemoveAssociationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType3`](../../doc/models/sca-entity-type-3.md) | Required | - |
| `sca_device_ids` | `List[str]` | Required | A list of device ids associated with the entity that should be removed.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `5`, *Minimum Length*: `30`, *Maximum Length*: `30` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.remove_association_request import RemoveAssociationRequest
from adyen.models.sca_entity_type_3 import ScaEntityType3

remove_association_request = RemoveAssociationRequest(
    entity_id='entityId6',
    entity_type=ScaEntityType3.LEGALENTITY,
    sca_device_ids=[
        'scaDeviceIds0',
        'scaDeviceIds1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

