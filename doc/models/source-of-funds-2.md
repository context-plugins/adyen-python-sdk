
# Source of Funds 2

Indicates where the funds used for the transfer originated. Possible values are:

- **DEBIT** for card-to-card transfers.
- **DEPOSIT_ACCOUNT** for wallet-to-card transfers.

## Enumeration

`SourceOfFunds2`

## Fields

| Name |
|  --- |
| `DEBIT` |
| `DEPOSIT_ACCOUNT` |

## Example

```python
from adyen.models.source_of_funds_2 import SourceOfFunds2

source_of_funds_2 = SourceOfFunds2.DEBIT
```

