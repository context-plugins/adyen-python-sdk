
# Sca Entity

## Structure

`ScaEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `100` |
| `mtype` | [`ScaEntityType4Enum`](../../doc/models/sca-entity-type-4-enum.md) | Required | The type of the entity that you are associating with the SCA device.<br><br>Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**. |

## Example

```python
from adyen.models.sca_entity import ScaEntity
from adyen.models.sca_entity_type_4_enum import ScaEntityType4Enum

sca_entity = ScaEntity(
    id='AH9999Z99Z999999ZZZZ9999Z',
    mtype=ScaEntityType4Enum.LEGALENTITY
)
```

