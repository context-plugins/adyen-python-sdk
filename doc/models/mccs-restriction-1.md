
# Mccs Restriction 1

List of merchant category codes (MCCs) and the operation.

Supported operations: **anyMatch**, **noneMatch**.

*This model accepts additional fields of type Any.*

## Structure

`MccsRestriction1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of merchant category codes (MCCs). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mccs_restriction_1 import MccsRestriction1

mccs_restriction_1 = MccsRestriction1(
    operation='operation2',
    value=[
        'value6'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

