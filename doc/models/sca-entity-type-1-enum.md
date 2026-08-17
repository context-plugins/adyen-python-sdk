
# Sca Entity Type 1 Enum

The type of entity you are associating the device with.

Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**.

## Enumeration

`ScaEntityType1Enum`

## Fields

| Name |
|  --- |
| `ACCOUNTHOLDER` |
| `LEGALENTITY` |
| `PAYMENTINSTRUMENT` |

## Example

```python
from adyen.models.sca_entity_type_1_enum import ScaEntityType1Enum

sca_entity_type_1 = ScaEntityType1Enum.LEGALENTITY
```

