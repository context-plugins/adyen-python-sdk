
# Wallet Purpose Enum

The purpose of a digital wallet transaction.

## Enumeration

`WalletPurposeEnum`

## Fields

| Name |
|  --- |
| `IDENTIFIEDBOLETO` |
| `TRANSFERDIFFERENTWALLET` |
| `TRANSFEROWNWALLET` |
| `TRANSFERSAMEWALLET` |
| `UNIDENTIFIEDBOLETO` |

## Example

```python
from adyen.models.wallet_purpose_enum import WalletPurposeEnum

wallet_purpose = WalletPurposeEnum.TRANSFEROWNWALLET
```

