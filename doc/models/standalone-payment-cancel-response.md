
# Standalone Payment Cancel Response

*This model accepts additional fields of type Any.*

## Structure

`StandalonePaymentCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_reference` | `str` | Required | The [`reference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment to cancel. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the cancel request. |
| `reference` | `str` | Optional | Your reference for the cancel request. |
| `status` | [`Status20`](../../doc/models/status-20.md) | Required | The status of your request. This will always have the value **received**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.standalone_payment_cancel_response import StandalonePaymentCancelResponse
from adyen.models.status_20 import Status20

standalone_payment_cancel_response = StandalonePaymentCancelResponse(
    merchant_account='merchantAccount8',
    payment_reference='paymentReference6',
    psp_reference='pspReference8',
    status=Status20.RECEIVED,
    reference='reference2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

