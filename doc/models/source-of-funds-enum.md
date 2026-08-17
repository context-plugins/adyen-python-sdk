
# Source of Funds Enum

Indicates where the funds used for the transfer originated. Possible values are:

- **DEBIT** for card-to-card transfers.
- **DEPOSIT_ACCOUNT** for wallet-to-card transfers.

## Enumeration

`SourceOfFundsEnum`

## Fields

| Name |
|  --- |
| `DEBIT` |
| `DEPOSIT_ACCOUNT` |

## Example

```python
from adyen.models.source_of_funds_enum import SourceOfFundsEnum

source_of_funds = SourceOfFundsEnum.DEBIT
```

