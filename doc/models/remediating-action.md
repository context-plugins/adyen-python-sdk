
# Remediating Action

*This model accepts additional fields of type Any.*

## Structure

`RemediatingAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The remediating action code. |
| `message` | `str` | Optional | A description of how you can resolve the verification error. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.remediating_action import RemediatingAction

remediating_action = RemediatingAction(
    code='code0',
    message='message8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

