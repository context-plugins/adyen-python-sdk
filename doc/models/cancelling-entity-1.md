
# Cancelling Entity 1

The party that initiated the cancellation of the transaction.

Possible values: **merchant**, **cardholder**.

## Enumeration

`CancellingEntity1`

## Fields

| Name |
|  --- |
| `MERCHANT` |
| `CARDHOLDER` |

## Example

```python
from adyen.models.cancelling_entity_1 import CancellingEntity1

cancelling_entity_1 = CancellingEntity1.MERCHANT
```

