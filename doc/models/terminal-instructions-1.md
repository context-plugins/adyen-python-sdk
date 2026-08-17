
# Terminal Instructions 1

Settings to define the behaviour of the payment terminal.

## Structure

`TerminalInstructions1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_app_restart` | `bool` | Optional | Indicates whether the Adyen app on the payment terminal restarts automatically when the configuration is updated. |

## Example

```python
from adyen.models.terminal_instructions_1 import TerminalInstructions1

terminal_instructions_1 = TerminalInstructions1(
    adyen_app_restart=False
)
```

