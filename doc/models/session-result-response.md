
# Session Result Response

## Structure

`SessionResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | Contains additional information about the payment. Some fields are included only if you enable them. To enable these fields in your Customer Area, go to **Developers** > **Additional data**. |
| `id` | `str` | Optional | A unique identifier of the session. |
| `payments` | [`List[Payment]`](../../doc/models/payment.md) | Optional | A list of all authorised payments done for this session. |
| `reference` | `str` | Optional | The unique reference that you provided in the original `/sessions` request. This identifies the payment and is used in all communication with you about the payment status. |
| `status` | [`Status5Enum`](../../doc/models/status-5-enum.md) | Optional | The status of the session. The status included in the response doesn't get updated. Don't make the request again to check for payment status updates.<br><br>Possible values:<br><br>* **completed**: the shopper completed the payment, and the payment was authorized.<br>* **paymentPending**: the shopper is in the process of making the payment. This applies to payment methods with an asynchronous flow, like voucher payments where the shopper completes the payment in a physical shop.<br>* **refused**: the session has been refused, because of too many refused payment attempts. The shopper can no longer complete the payment with this session.<br>* **canceled**: the shopper canceled the payment.<br>* **expired**: the session expired. The shopper can no longer complete the payment with this session. By default, the session expires one hour after it is created. |

## Example

```python
from adyen.models.amount_26 import Amount26
from adyen.models.payment import Payment
from adyen.models.payment_response_3 import PaymentResponse3
from adyen.models.result_code_2_enum import ResultCode2Enum
from adyen.models.session_result_response import SessionResultResponse
from adyen.models.status_5_enum import Status5Enum

session_result_response = SessionResultResponse(
    additional_data={
        'key0': 'additionalData6',
        'key1': 'additionalData7'
    },
    id='id6',
    payments=[
        Payment(
            amount=Amount26(
                currency='currency2',
                value=110
            ),
            payment_method=PaymentResponse3(
                brand='brand6',
                mtype='type8'
            ),
            psp_reference='pspReference6',
            result_code=ResultCode2Enum.PENDING
        )
    ],
    reference='reference2',
    status=Status5Enum.ACTIVE
)
```

