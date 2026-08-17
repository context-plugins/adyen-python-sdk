
# Submit Sca Association Request

## Structure

`SubmitScaAssociationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entities` | [`List[ScaEntity]`](../../doc/models/sca-entity.md) | Required | The list of entities to be associated.<br><br>**Constraints**: *Minimum Items*: `0`, *Maximum Items*: `5` |

## Example

```python
from adyen.models.sca_entity import ScaEntity
from adyen.models.sca_entity_type_4_enum import ScaEntityType4Enum
from adyen.models.submit_sca_association_request import SubmitScaAssociationRequest

submit_sca_association_request = SubmitScaAssociationRequest(
    entities=[
        ScaEntity(
            id='AH9999Z99Z999999ZZZZ9999Z',
            mtype=ScaEntityType4Enum.ACCOUNTHOLDER
        )
    ]
)
```

