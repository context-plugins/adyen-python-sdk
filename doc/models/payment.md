
# Payment

*This model accepts additional fields of type Any.*

## Structure

`Payment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `payment_method` | [`PaymentResponse8`](../../doc/models/payment-response-8.md) | Optional | - |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request. |
| `result_code` | [`ResultCode2`](../../doc/models/result-code-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.payment import Payment
from adyen.models.payment_response_8 import PaymentResponse8
from adyen.models.result_code_2 import ResultCode2

payment = Payment(
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
    psp_reference='pspReference2',
    result_code=ResultCode2.AUTHORISED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

