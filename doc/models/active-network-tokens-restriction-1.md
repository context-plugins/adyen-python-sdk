
# Active Network Tokens Restriction 1

The total number of tokens that a card can have across different kinds of digital wallets on the user's phones, watches, or other wearables.

Supported operations: **equals**, **notEquals**, **greaterThanOrEqualTo**, **greaterThan**, **lessThanOrEqualTo**, **lessThan**.

## Structure

`ActiveNetworkTokensRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | The number of tokens. |

## Example

```python
from adyen.models.active_network_tokens_restriction_1 import ActiveNetworkTokensRestriction1

active_network_tokens_restriction_1 = ActiveNetworkTokensRestriction1(
    operation='operation0',
    value=244
)
```

