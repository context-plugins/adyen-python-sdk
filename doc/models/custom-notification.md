
# Custom Notification

*This model accepts additional fields of type Any.*

## Structure

`CustomNotification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `event_code` | `str` | Optional | The event that caused the notification to be sent.Currently supported values:<br><br>* **AUTHORISATION**<br>* **CANCELLATION**<br>* **REFUND**<br>* **CAPTURE**<br>* **REPORT_AVAILABLE**<br>* **CHARGEBACK**<br>* **REQUEST_FOR_INFORMATION**<br>* **NOTIFICATION_OF_CHARGEBACK**<br>* **NOTIFICATIONTEST**<br>* **ORDER_OPENED**<br>* **ORDER_CLOSED**<br>* **CHARGEBACK_REVERSED**<br>* **REFUNDED_REVERSED**<br>* **REFUND_WITH_DATA** |
| `event_date` | `datetime` | Optional | The time of the event. Format: [ISO 8601](http://www.w3.org/TR/NOTE-datetime), YYYY-MM-DDThh:mm:ssTZD. |
| `merchant_reference` | `str` | Optional | Your reference for the custom test notification. |
| `payment_method` | `str` | Optional | The payment method for the payment that the notification is about. Possible values:<br><br>* **amex**<br>* **visa**<br>* **mc**<br>* **maestro**<br>* **bcmc**<br>* **paypal**<br>* **sms**<br>* **bankTransfer_NL**<br>* **bankTransfer_DE**<br>* **bankTransfer_BE**<br>* **ideal**<br>* **elv**<br>* **sepadirectdebit** |
| `reason` | `str` | Optional | A description of what caused the notification. |
| `success` | `bool` | Optional | The outcome of the event which the notification is about. Set to either **true** or **false**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.custom_notification import CustomNotification

custom_notification = CustomNotification(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    event_code='eventCode0',
    event_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    merchant_reference='merchantReference6',
    payment_method='paymentMethod8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

