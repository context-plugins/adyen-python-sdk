
# Get Terminal Details Request

## Structure

`GetTerminalDetailsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal` | `str` | Required | The unique terminal ID in the format `[Device model]-[Serial number]`.<br><br>For example, **V400m-324689776**. |

## Example

```python
from adyen.models.get_terminal_details_request import GetTerminalDetailsRequest

get_terminal_details_request = GetTerminalDetailsRequest(
    terminal='terminal2'
)
```

