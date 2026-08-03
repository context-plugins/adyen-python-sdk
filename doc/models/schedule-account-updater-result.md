
# Schedule Account Updater Result

*This model accepts additional fields of type Any.*

## Structure

`ScheduleAccountUpdaterResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psp_reference` | `str` | Required | Adyen's 16-character unique reference associated with the transaction. This value is globally unique; quote it when communicating with us about this request. |
| `result` | `str` | Required | The result of scheduling an Account Updater. If scheduling was successful, this field returns **Success**; otherwise it contains the error message. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.schedule_account_updater_result import ScheduleAccountUpdaterResult

schedule_account_updater_result = ScheduleAccountUpdaterResult(
    psp_reference='pspReference4',
    result='result2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

