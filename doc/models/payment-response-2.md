
# Payment Response 2

The object that contains the validation outcomes.
Only returned if `resultCode` is **Authorised** and if you have requested a payment validation in the request.

*This model accepts additional fields of type Any.*

## Structure

`PaymentResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`PaymentValidationsNameResponse`](../../doc/models/payment-validations-name-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_response_2 import PaymentResponse2
from adyen.models.payment_validations_name_response import PaymentValidationsNameResponse
from adyen.models.payment_validations_name_result_raw_response import PaymentValidationsNameResultRawResponse
from adyen.models.payment_validations_name_result_response import PaymentValidationsNameResultResponse
from adyen.models.status_11 import Status11

payment_response_2 = PaymentResponse2(
    name=PaymentValidationsNameResponse(
        raw_response=PaymentValidationsNameResultRawResponse(
            first_name='firstName0',
            full_name='fullName4',
            last_name='lastName8',
            middle_name='middleName2',
            status='status6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        result=PaymentValidationsNameResultResponse(
            first_name='firstName8',
            full_name='fullName6',
            last_name='lastName0',
            middle_name='middleName4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        status=Status11.NOTPERFORMED,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

