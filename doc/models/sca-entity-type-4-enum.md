
# Sca Entity Type 4 Enum

The type of the entity that you are associating with the SCA device.

Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**.

## Enumeration

`ScaEntityType4Enum`

## Fields

| Name |
|  --- |
| `ACCOUNTHOLDER` |
| `LEGALENTITY` |
| `PAYMENTINSTRUMENT` |

## Example

```python
from adyen.models.sca_entity_type_4_enum import ScaEntityType4Enum

sca_entity_type_4 = ScaEntityType4Enum.ACCOUNTHOLDER
```

