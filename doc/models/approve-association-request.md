
# Approve Association Request

## Structure

`ApproveAssociationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType2Enum`](../../doc/models/sca-entity-type-2-enum.md) | Required | The type of the entity.<br><br>Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**. |
| `sca_device_ids` | `List[str]` | Required | List of device ids associated to the entity that will be approved.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `5`, *Minimum Length*: `30`, *Maximum Length*: `30` |
| `status` | [`AssociationStatus1Enum`](../../doc/models/association-status-1-enum.md) | Required | The status of the association.<br><br>Possible values: **active** or **pendingApproval**. |

## Example

```python
from adyen.models.approve_association_request import ApproveAssociationRequest
from adyen.models.association_status_1_enum import AssociationStatus1Enum
from adyen.models.sca_entity_type_2_enum import ScaEntityType2Enum

approve_association_request = ApproveAssociationRequest(
    entity_id='entityId8',
    entity_type=ScaEntityType2Enum.PAYMENTINSTRUMENT,
    sca_device_ids=[
        'scaDeviceIds4',
        'scaDeviceIds5',
        'scaDeviceIds6'
    ],
    status=AssociationStatus1Enum.PENDINGAPPROVAL
)
```

