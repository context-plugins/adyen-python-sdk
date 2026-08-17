
# Transfer Type Enum

The type of transfer to which the limit applies. Possible values:

* **instant**: the limit applies to transfers with an **instant** priority.
* **all**: the limit applies to all transfers, regardless of priority.

## Enumeration

`TransferTypeEnum`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `ALL` |

## Example

```python
from adyen.models.transfer_type_enum import TransferTypeEnum

transfer_type = TransferTypeEnum.INSTANT
```

