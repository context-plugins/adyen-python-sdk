
# Upi Intent

*This model accepts additional fields of type Any.*

## Structure

`UpiIntent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `app_id` | `str` | Optional | TPAP (Third Party Application) Id that is being used to make the UPI payment |
| `billing_sequence_number` | `str` | Optional | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_notification_reference` | `str` | Optional | The `shopperNotificationReference` returned in the response when you requested to notify the shopper. Used for recurring payment only. |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | [`Type79`](../../doc/models/type-79.md) | Required | **upi_intent** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.type_79 import Type79
from adyen.models.upi_intent import UpiIntent

upi_intent = UpiIntent(
    mtype=Type79.UPI_INTENT,
    app_id='appId8',
    billing_sequence_number='billingSequenceNumber2',
    checkout_attempt_id='checkoutAttemptId8',
    recurring_detail_reference='recurringDetailReference2',
    sdk_data='sdkData8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

