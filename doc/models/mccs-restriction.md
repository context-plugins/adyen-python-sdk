
# Mccs Restriction

## Structure

`MccsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of merchant category codes (MCCs). |

## Example

```python
from adyen.models.mccs_restriction import MccsRestriction

mccs_restriction = MccsRestriction(
    operation='operation6',
    value=[
        'value0',
        'value1'
    ]
)
```

