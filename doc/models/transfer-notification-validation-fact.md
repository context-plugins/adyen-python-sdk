
# Transfer Notification Validation Fact

## Structure

`TransferNotificationValidationFact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | `str` | Optional | The evaluation result of the validation fact. |
| `mtype` | `str` | Optional | The type of the validation fact. |

## Example

```python
from adyen.models.transfer_notification_validation_fact import TransferNotificationValidationFact

transfer_notification_validation_fact = TransferNotificationValidationFact(
    result='result4',
    mtype='type0'
)
```

