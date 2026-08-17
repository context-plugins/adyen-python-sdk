
# Token Requestors Restriction

## Structure

`TokenRequestorsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | - |

## Example

```python
from adyen.models.token_requestors_restriction import TokenRequestorsRestriction

token_requestors_restriction = TokenRequestorsRestriction(
    operation='operation2',
    value=[
        'value6'
    ]
)
```

