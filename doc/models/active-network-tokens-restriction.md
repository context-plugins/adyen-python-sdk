
# Active Network Tokens Restriction

*This model accepts additional fields of type Any.*

## Structure

`ActiveNetworkTokensRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `int` | Optional | The number of tokens. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.active_network_tokens_restriction import ActiveNetworkTokensRestriction

active_network_tokens_restriction = ActiveNetworkTokensRestriction(
    operation='operation2',
    value=28,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

