
# Mccs Restriction 1

List of merchant category codes (MCCs) and the operation.

Supported operations: **anyMatch**, **noneMatch**.

## Structure

`MccsRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of merchant category codes (MCCs). |

## Example

```python
from adyen.models.mccs_restriction_1 import MccsRestriction1

mccs_restriction_1 = MccsRestriction1(
    operation='operation2',
    value=[
        'value6'
    ]
)
```

