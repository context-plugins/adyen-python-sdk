
# Wallet Provider Account Score Restriction

## Structure

`WalletProviderAccountScoreRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |

## Example

```python
from adyen.models.wallet_provider_account_score_restriction import WalletProviderAccountScoreRestriction

wallet_provider_account_score_restriction = WalletProviderAccountScoreRestriction(
    operation='operation8',
    value=22
)
```

