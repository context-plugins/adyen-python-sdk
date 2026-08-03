
# Type 122

The type of the cashout transfer.

Possible values:

- **cashoutRepayment**: Corresponds to the transfer created to deduct the cashout amount after settlement.
- **cashoutFee**: Corresponds to the transfer created to debit the cashout fee form the user's balance account.

## Enumeration

`Type122`

## Fields

| Name |
|  --- |
| `CASHOUTREPAYMENT` |
| `CASHOUTFEE` |

## Example

```python
from adyen.models.type_122 import Type122

type_122 = Type122.CASHOUTREPAYMENT
```

