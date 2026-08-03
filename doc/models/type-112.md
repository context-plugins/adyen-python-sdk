
# Type 112

The type of transfer.

Possible values:

- **bankTransfer**: for push transfers to a transfer instrument or a bank account. The `category` must be **bank**.
- **internalTransfer**: for push transfers between balance accounts. The `category` must be **internal**.
- **internalDirectDebit**: for pull transfers (direct debits) between balance accounts. The `category` must be **internal**.

## Enumeration

`Type112`

## Fields

| Name |
|  --- |
| `BANKTRANSFER` |
| `INTERNALTRANSFER` |
| `INTERNALDIRECTDEBIT` |

## Example

```python
from adyen.models.type_112 import Type112

type_112 = Type112.INTERNALDIRECTDEBIT
```

