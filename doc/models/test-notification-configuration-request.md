
# Test Notification Configuration Request

*This model accepts additional fields of type Any.*

## Structure

`TestNotificationConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_types` | [`List[EventType1]`](../../doc/models/event-type-1.md) | Optional | The event types to test.  If left blank, then all of the configured event types will be tested.<br><br>> Permitted values: `ACCOUNT_HOLDER_CREATED`, `ACCOUNT_CREATED`, `ACCOUNT_UPDATED`, `ACCOUNT_HOLDER_UPDATED`, `ACCOUNT_HOLDER_STATUS_CHANGE`, `ACCOUNT_HOLDER_STORE_STATUS_CHANGE` `ACCOUNT_HOLDER_VERIFICATION`, `ACCOUNT_HOLDER_LIMIT_REACHED`, `ACCOUNT_HOLDER_PAYOUT`, `PAYMENT_FAILURE`, `SCHEDULED_REFUNDS`, `REPORT_AVAILABLE`, `TRANSFER_FUNDS`, `BENEFICIARY_SETUP`, `COMPENSATE_NEGATIVE_BALANCE`. |
| `notification_id` | `int` | Required | The ID of the notification subscription configuration to be tested. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.event_type_1 import EventType1
from adyen.models.test_notification_configuration_request import TestNotificationConfigurationRequest

test_notification_configuration_request = TestNotificationConfigurationRequest(
    notification_id=40,
    event_types=[
        EventType1.REFUND_FUNDS_TRANSFER
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

