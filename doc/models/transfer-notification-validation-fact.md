
# Transfer Notification Validation Fact

*This model accepts additional fields of type Any.*

## Structure

`TransferNotificationValidationFact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `result` | `str` | Optional | The evaluation result of the validation fact. |
| `mtype` | `str` | Optional | The type of the validation fact. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.transfer_notification_validation_fact import TransferNotificationValidationFact

transfer_notification_validation_fact = TransferNotificationValidationFact(
    result='result4',
    mtype='type0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

