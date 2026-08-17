
# Payment Validations Name Response

## Structure

`PaymentValidationsNameResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `raw_response` | [`PaymentValidationsNameResultRawResponse2`](../../doc/models/payment-validations-name-result-raw-response-2.md) | Optional | Contains the raw response(s) returned by the scheme for the name validation. |
| `result` | [`PaymentValidationsNameResultResponse2`](../../doc/models/payment-validations-name-result-response-2.md) | Optional | Contains the scheme-agnostic match values returned by Adyen. |
| `status` | [`StatusEnum`](../../doc/models/status-enum.md) | Optional | Informs you if the name validation was performed. Possible values:<br><br>**performed**, **notPerformed**, **notSupported** |

## Example

```python
from adyen.models.payment_validations_name_response import PaymentValidationsNameResponse
from adyen.models.payment_validations_name_result_raw_response_2 import PaymentValidationsNameResultRawResponse2
from adyen.models.payment_validations_name_result_response_2 import PaymentValidationsNameResultResponse2
from adyen.models.status_enum import StatusEnum

payment_validations_name_response = PaymentValidationsNameResponse(
    raw_response=PaymentValidationsNameResultRawResponse2(
        first_name='firstName0',
        full_name='fullName4',
        last_name='lastName8',
        middle_name='middleName2',
        status='status6'
    ),
    result=PaymentValidationsNameResultResponse2(
        first_name='firstName8',
        full_name='fullName6',
        last_name='lastName0',
        middle_name='middleName4'
    ),
    status=StatusEnum.NOTPERFORMED
)
```

