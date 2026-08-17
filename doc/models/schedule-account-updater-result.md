
# Schedule Account Updater Result

## Structure

`ScheduleAccountUpdaterResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `psp_reference` | `str` | Required | Adyen's 16-character unique reference associated with the transaction. This value is globally unique; quote it when communicating with us about this request. |
| `result` | `str` | Required | The result of scheduling an Account Updater. If scheduling was successful, this field returns **Success**; otherwise it contains the error message. |

## Example

```python
from adyen.models.schedule_account_updater_result import ScheduleAccountUpdaterResult

schedule_account_updater_result = ScheduleAccountUpdaterResult(
    psp_reference='pspReference4',
    result='result2'
)
```

