
# Same Counterparty Restriction

## Structure

`SameCounterpartyRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `bool` | Optional | - |

## Example

```python
from adyen.models.same_counterparty_restriction import SameCounterpartyRestriction

same_counterparty_restriction = SameCounterpartyRestriction(
    operation='operation0',
    value=False
)
```

