
# Terminal Instructions

*This model accepts additional fields of type Any.*

## Structure

`TerminalInstructions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adyen_app_restart` | `bool` | Optional | Indicates whether the Adyen app on the payment terminal restarts automatically when the configuration is updated. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.terminal_instructions import TerminalInstructions

terminal_instructions = TerminalInstructions(
    adyen_app_restart=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

