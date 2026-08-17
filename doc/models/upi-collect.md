
# UPI Collect

## Structure

`UPICollect`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billing_sequence_number` | `str` | Optional | The sequence number for the debit. For example, send **2** if this is the second debit for the subscription. The sequence number is included in the notification sent to the shopper. |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `shopper_notification_reference` | `str` | Optional | The `shopperNotificationReference` returned in the response when you requested to notify the shopper. Used for recurring payment only. |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `mtype` | `str` | Required, Constant | **upi_collect**<br><br>**Value**: `"upi_collect"` |
| `virtual_payment_address` | `str` | Optional | The virtual payment address for UPI. |

## Example

```python
from adyen.models.upi_collect import UPICollect

upi_collect = UPICollect(
    billing_sequence_number='billingSequenceNumber4',
    checkout_attempt_id='checkoutAttemptId0',
    recurring_detail_reference='recurringDetailReference4',
    sdk_data='sdkData6',
    shopper_notification_reference='shopperNotificationReference4'
)
```

