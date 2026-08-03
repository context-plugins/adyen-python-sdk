
# Terminal Action Schedule Detail

*This model accepts additional fields of type Any.*

## Structure

`TerminalActionScheduleDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of the action on the specified terminal. |
| `terminal_id` | `str` | Optional | The unique ID of the terminal that the action applies to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_action_schedule_detail import TerminalActionScheduleDetail

terminal_action_schedule_detail = TerminalActionScheduleDetail(
    id='id4',
    terminal_id='terminalId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

