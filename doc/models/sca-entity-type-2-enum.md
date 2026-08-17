
# Sca Entity Type 2 Enum

The type of the entity.

Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**.

## Enumeration

`ScaEntityType2Enum`

## Fields

| Name |
|  --- |
| `ACCOUNTHOLDER` |
| `LEGALENTITY` |
| `PAYMENTINSTRUMENT` |

## Example

```python
from adyen.models.sca_entity_type_2_enum import ScaEntityType2Enum

sca_entity_type_2 = ScaEntityType2Enum.PAYMENTINSTRUMENT
```

