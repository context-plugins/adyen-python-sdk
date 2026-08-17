
# Wallet Provider Account Score Restriction 2

Checks the wallet account score.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

## Structure

`WalletProviderAccountScoreRestriction2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |

## Example

```python
from adyen.models.wallet_provider_account_score_restriction_2 import WalletProviderAccountScoreRestriction2

wallet_provider_account_score_restriction_2 = WalletProviderAccountScoreRestriction2(
    operation='operation6',
    value=86
)
```

