
# Payment Response 7

## Structure

`PaymentResponse7`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`PaymentValidationsNameResponse2`](../../doc/models/payment-validations-name-response-2.md) | Optional | Object that contains the status and outcomes of the [name validation](https://docs.adyen.com/payment-methods/cards/name-validation). |

## Example

```python
from adyen.models.payment_response_7 import PaymentResponse7
from adyen.models.payment_validations_name_response_2 import PaymentValidationsNameResponse2
from adyen.models.payment_validations_name_result_raw_response_2 import PaymentValidationsNameResultRawResponse2
from adyen.models.payment_validations_name_result_response_2 import PaymentValidationsNameResultResponse2
from adyen.models.status_enum import StatusEnum

payment_response_7 = PaymentResponse7(
    name=PaymentValidationsNameResponse2(
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
)
```

