
# Terminal Instructions

## Structure

`TerminalInstructions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_app_restart` | `bool` | Optional | Indicates whether the Adyen app on the payment terminal restarts automatically when the configuration is updated. |

## Example

```python
from adyen.models.terminal_instructions import TerminalInstructions

terminal_instructions = TerminalInstructions(
    adyen_app_restart=False
)
```

