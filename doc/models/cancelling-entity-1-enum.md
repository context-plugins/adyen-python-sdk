
# Cancelling Entity 1 Enum

The party that initiated the cancellation of the transaction.

Possible values: **merchant**, **cardholder**.

## Enumeration

`CancellingEntity1Enum`

## Fields

| Name |
|  --- |
| `MERCHANT` |
| `CARDHOLDER` |

## Example

```python
from adyen.models.cancelling_entity_1_enum import CancellingEntity1Enum

cancelling_entity_1 = CancellingEntity1Enum.MERCHANT
```

