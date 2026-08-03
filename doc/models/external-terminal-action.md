
# External Terminal Action

*This model accepts additional fields of type Any.*

## Structure

`ExternalTerminalAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `action_type` | `str` | Optional | The type of terminal action: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, or **UninstallAndroidCertificate**. |
| `config` | `str` | Optional | Technical information about the terminal action. |
| `confirmed_at` | `datetime` | Optional | The date and time when the action was carried out. |
| `id` | `str` | Optional | The unique ID of the terminal action. |
| `result` | `str` | Optional | The result message for the action. |
| `scheduled_at` | `datetime` | Optional | The date and time when the action was scheduled to happen. |
| `status` | `str` | Optional | The status of the terminal action: **pending**, **successful**, **failed**, **cancelled**, or **tryLater**. |
| `terminal_id` | `str` | Optional | The unique ID of the terminal that the action applies to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.external_terminal_action import ExternalTerminalAction

external_terminal_action = ExternalTerminalAction(
    action_type='actionType8',
    config='config8',
    confirmed_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id2',
    result='result4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

