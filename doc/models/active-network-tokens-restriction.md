
# Active Network Tokens Restriction

## Structure

`ActiveNetworkTokensRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | The number of tokens. |

## Example

```python
from adyen.models.active_network_tokens_restriction import ActiveNetworkTokensRestriction

active_network_tokens_restriction = ActiveNetworkTokensRestriction(
    operation='operation2',
    value=28
)
```

