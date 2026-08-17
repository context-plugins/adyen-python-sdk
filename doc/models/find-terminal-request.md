
# Find Terminal Request

## Structure

`FindTerminalRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `terminal` | `str` | Required | The unique terminal ID in the format `[Device model]-[Serial number]`.<br><br>For example, **V400m-324689776**. |

## Example

```python
from adyen.models.find_terminal_request import FindTerminalRequest

find_terminal_request = FindTerminalRequest(
    terminal='terminal8'
)
```

