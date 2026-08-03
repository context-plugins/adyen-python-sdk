
# Mccs Restriction

*This model accepts additional fields of type Any.*

## Structure

`MccsRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | `str` | Required | Defines how the condition must be evaluated. |
| `value` | `List[str]` | Optional | List of merchant category codes (MCCs). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mccs_restriction import MccsRestriction

mccs_restriction = MccsRestriction(
    operation='operation6',
    value=[
        'value0',
        'value1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

