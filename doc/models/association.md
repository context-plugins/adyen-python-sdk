
# Association

## Structure

`Association`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `entity_type` | [`ScaEntityType1Enum`](../../doc/models/sca-entity-type-1-enum.md) | Required | The type of entity you are associating the device with.<br><br>Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**. |
| `sca_device_id` | `str` | Required | The unique identifier for the SCA device.<br><br>**Constraints**: *Minimum Length*: `30`, *Maximum Length*: `30` |
| `status` | [`AssociationStatus1Enum`](../../doc/models/association-status-1-enum.md) | Required | The status of the association.<br><br>Possible values: **active** or **pendingApproval**. |

## Example

```python
from adyen.models.association import Association
from adyen.models.association_status_1_enum import AssociationStatus1Enum
from adyen.models.sca_entity_type_1_enum import ScaEntityType1Enum

association = Association(
    entity_id='entityId2',
    entity_type=ScaEntityType1Enum.ACCOUNTHOLDER,
    sca_device_id='BSDR11111111111A1AAA1AAAAA1AA1',
    status=AssociationStatus1Enum.PENDINGAPPROVAL
)
```

