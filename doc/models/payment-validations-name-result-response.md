
# Payment Validations Name Result Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentValidationsNameResultResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | Informs you if the first name your shopper provided matches the cardholder first name on file at the issuing bank. The first name is only validated for Visa. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `full_name` | `str` | Optional | Informs you if the full name your shopper provided matches the cardholder name on file at the issuing bank. The full name is the only field that is validated for Mastercard. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `last_name` | `str` | Optional | Informs you if the last name your shopper provided matches the cardholder last name on file at the issuing bank. The last name is only validated for Visa. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `middle_name` | `str` | Optional | Informs you if the middle name your shopper provided matches the cardholder middle name on file at the issuing bank. The middle name is only validated for Visa. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_validations_name_result_response import PaymentValidationsNameResultResponse

payment_validations_name_result_response = PaymentValidationsNameResultResponse(
    first_name='firstName2',
    full_name='fullName2',
    last_name='lastName6',
    middle_name='middleName0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

