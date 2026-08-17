
# Approve Association Response

## Structure

`ApproveAssociationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sca_associations` | [`List[Association]`](../../doc/models/association.md) | Required | The list of associations.<br><br>**Constraints**: *Minimum Items*: `1` |

## Example

```python
from adyen.models.approve_association_response import ApproveAssociationResponse
from adyen.models.association import Association
from adyen.models.association_status_1_enum import AssociationStatus1Enum
from adyen.models.sca_entity_type_1_enum import ScaEntityType1Enum

approve_association_response = ApproveAssociationResponse(
    sca_associations=[
        Association(
            entity_id='entityId6',
            entity_type=ScaEntityType1Enum.PAYMENTINSTRUMENT,
            sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
            status=AssociationStatus1Enum.PENDINGAPPROVAL
        )
    ]
)
```

