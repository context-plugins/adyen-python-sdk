
# Test Webhook Request

*This model accepts additional fields of type Any.*

## Structure

`TestWebhookRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification` | [`CustomNotification`](../../doc/models/custom-notification.md) | Optional | - |
| `types` | `List[str]` | Optional | List of event codes for which to send test notifications. Only the webhook types below are supported.<br><br>Possible values if webhook `type`: **standard**:<br><br>* **AUTHORISATION**<br>* **CHARGEBACK_REVERSED**<br>* **ORDER_CLOSED**<br>* **ORDER_OPENED**<br>* **PAIDOUT_REVERSED**<br>* **PAYOUT_THIRDPARTY**<br>* **REFUNDED_REVERSED**<br>* **REFUND_WITH_DATA**<br>* **REPORT_AVAILABLE**<br>* **CUSTOM** - set your custom notification fields in the [`notification`](https://docs.adyen.com/api-explorer/#/ManagementService/v1/post/companies/{companyId}/webhooks/{webhookId}/test__reqParam_notification) object.<br><br>Possible values if webhook `type`: **banktransfer-notification**:<br><br>* **PENDING**<br><br>Possible values if webhook `type`: **report-notification**:<br><br>* **REPORT_AVAILABLE**<br><br>Possible values if webhook `type`: **ideal-notification**:<br><br>* **AUTHORISATION**<br><br>Possible values if webhook `type`: **pending-notification**:<br><br>* **PENDING** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.custom_notification import CustomNotification
from adyen.models.test_webhook_request import TestWebhookRequest

test_webhook_request = TestWebhookRequest(
    notification=CustomNotification(
        amount=Amount16(
            currency='currency2',
            value=110,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        event_code='eventCode2',
        event_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        merchant_reference='merchantReference4',
        payment_method='paymentMethod0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    types=[
        'types3'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

