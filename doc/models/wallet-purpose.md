
# Wallet Purpose

The purpose of a digital wallet transaction.

## Enumeration

`WalletPurpose`

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
from adyen.models.wallet_purpose import WalletPurpose

wallet_purpose = WalletPurpose.TRANSFEROWNWALLET
```

