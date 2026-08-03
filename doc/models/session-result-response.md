
# Session Result Response

*This model accepts additional fields of type Any.*

## Structure

`SessionResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some fields are included only if you enable them. To enable these fields in your Customer Area, go to **Developers** > **Additional data**. |
| `id` | `str` | Optional | A unique identifier of the session. |
| `payments` | [`List[Payment]`](../../doc/models/payment.md) | Optional | A list of all authorised payments done for this session. |
| `reference` | `str` | Optional | The unique reference that you provided in the original `/sessions` request. This identifies the payment and is used in all communication with you about the payment status. |
| `status` | [`Status52`](../../doc/models/status-52.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.payment import Payment
from adyen.models.payment_response_8 import PaymentResponse8
from adyen.models.result_code_2 import ResultCode2
from adyen.models.session_result_response import SessionResultResponse
from adyen.models.status_52 import Status52

session_result_response = SessionResultResponse(
    additional_data={
        'key0': 'additionalData6',
        'key1': 'additionalData7'
    },
    id='id6',
    payments=[
        Payment(
            amount=Amount16(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            payment_method=PaymentResponse8(
                brand='brand6',
                mtype='type8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            psp_reference='pspReference6',
            result_code=ResultCode2.PENDING,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    reference='reference2',
    status=Status52.ACTIVE,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

