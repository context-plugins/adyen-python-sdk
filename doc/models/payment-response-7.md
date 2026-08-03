
# Payment Response 7

*This model accepts additional fields of type Any.*

## Structure

`PaymentResponse7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`PaymentValidationsNameResponse`](../../doc/models/payment-validations-name-response.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_response_7 import PaymentResponse7
from adyen.models.payment_validations_name_response import PaymentValidationsNameResponse
from adyen.models.payment_validations_name_result_raw_response import PaymentValidationsNameResultRawResponse
from adyen.models.payment_validations_name_result_response import PaymentValidationsNameResultResponse
from adyen.models.status_11 import Status11

payment_response_7 = PaymentResponse7(
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

