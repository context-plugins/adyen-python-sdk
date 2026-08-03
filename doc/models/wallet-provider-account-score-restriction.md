
# Wallet Provider Account Score Restriction

*This model accepts additional fields of type Any.*

## Structure

`WalletProviderAccountScoreRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.wallet_provider_account_score_restriction import WalletProviderAccountScoreRestriction

wallet_provider_account_score_restriction = WalletProviderAccountScoreRestriction(
    operation='operation8',
    value=22,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

