
# Test Webhook Response

*This model accepts additional fields of type Any.*

## Structure

`TestWebhookResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TestOutput]`](../../doc/models/test-output.md) | Optional | List with test results. Each test webhook we send has a list element with the result. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.test_output import TestOutput
from adyen.models.test_webhook_response import TestWebhookResponse

test_webhook_response = TestWebhookResponse(
    data=[
        TestOutput(
            status='status2',
            merchant_id='merchantId6',
            output='output8',
            request_sent='requestSent0',
            response_code='responseCode0',
            response_time='responseTime8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        TestOutput(
            status='status2',
            merchant_id='merchantId6',
            output='output8',
            request_sent='requestSent0',
            response_code='responseCode0',
            response_time='responseTime8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

