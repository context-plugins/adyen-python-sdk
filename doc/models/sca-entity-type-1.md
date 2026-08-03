
# Sca Entity Type 1

The type of entity you are associating the device with.

Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**.

## Enumeration

`ScaEntityType1`

## Fields

| Name |
|  --- |
| `ACCOUNTHOLDER` |
| `LEGALENTITY` |
| `PAYMENTINSTRUMENT` |

## Example

```python
from adyen.models.sca_entity_type_1 import ScaEntityType1

sca_entity_type_1 = ScaEntityType1.LEGALENTITY
```

