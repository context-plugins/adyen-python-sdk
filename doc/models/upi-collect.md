
# Upi Collect

*This model accepts additional fields of type Any.*

## Structure

`UpiCollect`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_sequence_number` | `str` | Optional | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_notification_reference` | `str` | Optional | The `shopperNotificationReference` returned in the response when you requested to notify the shopper. Used for recurring payment only. |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type78`](../../doc/models/type-78.md) | Required | **upi_collect** |
| `virtual_payment_address` | `str` | Optional | The virtual payment address for UPI. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_78 import Type78
from adyen.models.upi_collect import UpiCollect

upi_collect = UpiCollect(
    mtype=Type78.UPI_COLLECT,
    billing_sequence_number='billingSequenceNumber4',
    checkout_attempt_id='checkoutAttemptId0',
    recurring_detail_reference='recurringDetailReference4',
    sdk_data='sdkData6',
    shopper_notification_reference='shopperNotificationReference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

