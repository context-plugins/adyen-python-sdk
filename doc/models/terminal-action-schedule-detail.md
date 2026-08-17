
# Terminal Action Schedule Detail

## Structure

`TerminalActionScheduleDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Optional | The ID of the action on the specified terminal. |
| `terminal_id` | `str` | Optional | The unique ID of the terminal that the action applies to. |

## Example

```python
from adyen.models.terminal_action_schedule_detail import TerminalActionScheduleDetail

terminal_action_schedule_detail = TerminalActionScheduleDetail(
    id='id4',
    terminal_id='terminalId2'
)
```

