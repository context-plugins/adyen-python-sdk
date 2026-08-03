
# Transfer Type

The type of transfer to which the limit applies. Possible values:

* **instant**: the limit applies to transfers with an **instant** priority.
* **all**: the limit applies to all transfers, regardless of priority.

## Enumeration

`TransferType`

## Fields

| Name |
|  --- |
| `INSTANT` |
| `ALL` |

## Example

```python
from adyen.models.transfer_type import TransferType

transfer_type = TransferType.INSTANT
```

