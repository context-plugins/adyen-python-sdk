
# Association

*This model accepts additional fields of type Any.*

## Structure

`Association`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType1`](../../doc/models/sca-entity-type-1.md) | Required | - |
| `sca_device_id` | `str` | Required | The unique identifier for the SCA device.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |
| `status` | [`AssociationStatus1`](../../doc/models/association-status-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association import Association
from adyen.models.association_status_1 import AssociationStatus1
from adyen.models.sca_entity_type_1 import ScaEntityType1

association = Association(
    entity_id='entityId2',
    entity_type=ScaEntityType1.ACCOUNTHOLDER,
    sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
    status=AssociationStatus1.PENDINGAPPROVAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

