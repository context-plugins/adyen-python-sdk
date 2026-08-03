
# Payment Validations Name Response 2

Object that contains the status and outcomes of the [name validation](https://docs.adyen.com/payment-methods/cards/name-validation).

*This model accepts additional fields of type Any.*

## Structure

`PaymentValidationsNameResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `raw_response` | [`PaymentValidationsNameResultRawResponse`](../../doc/models/payment-validations-name-result-raw-response.md) | Optional | - |
| `result` | [`PaymentValidationsNameResultResponse`](../../doc/models/payment-validations-name-result-response.md) | Optional | - |
| `status` | [`Status11`](../../doc/models/status-11.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_validations_name_response_2 import PaymentValidationsNameResponse2
from adyen.models.payment_validations_name_result_raw_response import PaymentValidationsNameResultRawResponse
from adyen.models.payment_validations_name_result_response import PaymentValidationsNameResultResponse
from adyen.models.status_11 import Status11

payment_validations_name_response_2 = PaymentValidationsNameResponse2(
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
    status=Status11.PERFORMED,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

