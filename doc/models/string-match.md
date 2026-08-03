
# String Match

*This model accepts additional fields of type Any.*

## Structure

`StringMatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | [`Operation`](../../doc/models/operation.md) | Optional | - |
| `value` | `str` | Optional | The string to be matched. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.operation import Operation
from adyen.models.string_match import StringMatch

string_match = StringMatch(
    operation=Operation.ISEQUALTO,
    value='value4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

