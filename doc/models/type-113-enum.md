
# Type 113 Enum

The type of transfer.

Possible values:

- **bankTransfer**: for push transfers to a transfer instrument or a bank account. The `category` must be **bank**.
- **internalTransfer**: for push transfers between balance accounts. The `category` must be **internal**.
- **internalDirectDebit**: for pull transfers (direct debits) between balance accounts. The `category` must be **internal**.

## Enumeration

`Type113Enum`

## Fields

| Name |
|  --- |
| `BANKTRANSFER` |
| `INTERNALTRANSFER` |
| `INTERNALDIRECTDEBIT` |

## Example

```python
from adyen.models.type_113_enum import Type113Enum

type_113 = Type113Enum.INTERNALDIRECTDEBIT
```

