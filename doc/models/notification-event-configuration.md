
# Notification Event Configuration

## Structure

`NotificationEventConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventTypeEnum`](../../doc/models/event-type-enum.md) | Required | The type of event.<br><br>Possible values: **ACCOUNT_CLOSED**, **ACCOUNT_CREATED**, **ACCOUNT_FUNDS_BELOW_THRESHOLD**, **ACCOUNT_HOLDER_CREATED**, **ACCOUNT_HOLDER_LIMIT_REACHED**, **ACCOUNT_HOLDER_PAYOUT**, **ACCOUNT_HOLDER_STATUS_CHANGE**, **ACCOUNT_HOLDER_STORE_STATUS_CHANGE**, **ACCOUNT_HOLDER_UPCOMING_DEADLINE**, **ACCOUNT_HOLDER_UPDATED**, **ACCOUNT_HOLDER_VERIFICATION**, **ACCOUNT_UPDATED**, **BENEFICIARY_SETUP**, **COMPENSATE_NEGATIVE_BALANCE**, **DIRECT_DEBIT_INITIATED**, **PAYMENT_FAILURE**, **REFUND_FUNDS_TRANSFER**, **REPORT_AVAILABLE**, **SCHEDULED_REFUNDS**, **TRANSFER_FUNDS**. |
| `include_mode` | [`IncludeModeEnum`](../../doc/models/include-mode-enum.md) | Required | Indicates whether the specified `eventType` is sent to your webhook endpoint.<br>Possible values:<br><br>* **INCLUDE**: Send the specified `eventType`.<br>* **EXCLUDE**: Send all event types except the specified `eventType` and other event types with the `includeMode` set to **EXCLUDE**. |

## Example

```python
from adyen.models.event_type_enum import EventTypeEnum
from adyen.models.include_mode_enum import IncludeModeEnum
from adyen.models.notification_event_configuration import NotificationEventConfiguration

notification_event_configuration = NotificationEventConfiguration(
    event_type=EventTypeEnum.BENEFICIARY_SETUP,
    include_mode=IncludeModeEnum.EXCLUDE
)
```

