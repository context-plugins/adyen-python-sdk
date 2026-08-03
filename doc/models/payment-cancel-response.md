
# Payment Cancel Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to cancel. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the cancel request. |
| `reference` | `str` | Optional | Your reference for the cancel request. |
| `status` | [`Status20`](../../doc/models/status-20.md) | Required | The status of your request. This will always have the value **received**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_cancel_response import PaymentCancelResponse
from adyen.models.status_20 import Status20

payment_cancel_response = PaymentCancelResponse(
    merchant_account='merchantAccount2',
    payment_psp_reference='paymentPspReference8',
    psp_reference='pspReference2',
    status=Status20.RECEIVED,
    reference='reference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

