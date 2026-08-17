
# List External Terminal Actions Response

## Structure

`ListExternalTerminalActionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[ExternalTerminalAction]`](../../doc/models/external-terminal-action.md) | Optional | The list of terminal actions. |

## Example

```python
import dateutil.parser

from adyen.models.external_terminal_action import ExternalTerminalAction
from adyen.models.list_external_terminal_actions_response import ListExternalTerminalActionsResponse

list_external_terminal_actions_response = ListExternalTerminalActionsResponse(
    data=[
        ExternalTerminalAction(
            action_type='actionType0',
            config='config6',
            confirmed_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            result='result4'
        ),
        ExternalTerminalAction(
            action_type='actionType0',
            config='config6',
            confirmed_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            result='result4'
        ),
        ExternalTerminalAction(
            action_type='actionType0',
            config='config6',
            confirmed_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            id='id0',
            result='result4'
        )
    ]
)
```

