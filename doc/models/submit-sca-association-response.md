
# Submit Sca Association Response

*This model accepts additional fields of type Any.*

## Structure

`SubmitScaAssociationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sca_associations` | [`List[Association]`](../../doc/models/association.md) | Required | List of associations created to the entities and their statuses.<br><br>**Constraints**: *Minimum Items*: `1` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.association import Association
from adyen.models.association_status_1 import AssociationStatus1
from adyen.models.sca_entity_type_1 import ScaEntityType1
from adyen.models.submit_sca_association_response import SubmitScaAssociationResponse

submit_sca_association_response = SubmitScaAssociationResponse(
    sca_associations=[
        Association(
            entity_id='entityId6',
            entity_type=ScaEntityType1.PAYMENTINSTRUMENT,
            sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
            status=AssociationStatus1.PENDINGAPPROVAL,
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

