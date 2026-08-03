
# Get Terminal Details Request

*This model accepts additional fields of type Any.*

## Structure

`GetTerminalDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal` | `str` | Required | The unique terminal ID in the format `[Device model]-[Serial number]`.<br><br>For example, **V400m-324689776**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_terminal_details_request import GetTerminalDetailsRequest

get_terminal_details_request = GetTerminalDetailsRequest(
    terminal='terminal2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

