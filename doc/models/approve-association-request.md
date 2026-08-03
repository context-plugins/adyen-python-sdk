
# Approve Association Request

*This model accepts additional fields of type Any.*

## Structure

`ApproveAssociationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType2`](../../doc/models/sca-entity-type-2.md) | Required | - |
| `sca_device_ids` | `List[str]` | Required | List of device ids associated to the entity that will be approved.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `5`, *Minimum Length*: `30`, *Maximum Length*: `30` |
| `status` | [`AssociationStatus1`](../../doc/models/association-status-1.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.approve_association_request import ApproveAssociationRequest
from adyen.models.association_status_1 import AssociationStatus1
from adyen.models.sca_entity_type_2 import ScaEntityType2

approve_association_request = ApproveAssociationRequest(
    entity_id='entityId8',
    entity_type=ScaEntityType2.PAYMENTINSTRUMENT,
    sca_device_ids=[
        'scaDeviceIds4',
        'scaDeviceIds5',
        'scaDeviceIds6'
    ],
    status=AssociationStatus1.PENDINGAPPROVAL,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

