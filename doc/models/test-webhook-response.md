
# Test Webhook Response

## Structure

`TestWebhookResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `data` | [`List[TestOutput]`](../../doc/models/test-output.md) | Optional | List with test results. Each test webhook we send has a list element with the result. |

## Example

```python
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
            response_time='responseTime8'
        ),
        TestOutput(
            status='status2',
            merchant_id='merchantId6',
            output='output8',
            request_sent='requestSent0',
            response_code='responseCode0',
            response_time='responseTime8'
        )
    ]
)
```

