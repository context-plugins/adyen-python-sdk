
# Wallet Provider Account Score Restriction 2

Checks the wallet account score.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

*This model accepts additional fields of type Any.*

## Structure

`WalletProviderAccountScoreRestriction2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.wallet_provider_account_score_restriction_2 import WalletProviderAccountScoreRestriction2

wallet_provider_account_score_restriction_2 = WalletProviderAccountScoreRestriction2(
    operation='operation6',
    value=86,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

