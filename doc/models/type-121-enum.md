
# Type 121 Enum

The type of the cashout transfer.

Possible values:

- **cashoutRepayment**: Corresponds to the transfer created to deduct the cashout amount after settlement.
- **cashoutFee**: Corresponds to the transfer created to debit the cashout fee form the user's balance account.

## Enumeration

`Type121Enum`

## Fields

| Name |
|  --- |
| `CASHOUTREPAYMENT` |
| `CASHOUTFEE` |

## Example

```python
from adyen.models.type_121_enum import Type121Enum

type_121 = Type121Enum.CASHOUTREPAYMENT
```

