
# Payment Validations Name Result Response 2

Contains the scheme-agnostic match values returned by Adyen.

## Structure

`PaymentValidationsNameResultResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | Informs you if the first name your shopper provided matches the cardholder first name on file at the issuing bank. The first name is only validated for Visa. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `full_name` | `str` | Optional | Informs you if the full name your shopper provided matches the cardholder name on file at the issuing bank. The full name is the only field that is validated for Mastercard. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `last_name` | `str` | Optional | Informs you if the last name your shopper provided matches the cardholder last name on file at the issuing bank. The last name is only validated for Visa. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |
| `middle_name` | `str` | Optional | Informs you if the middle name your shopper provided matches the cardholder middle name on file at the issuing bank. The middle name is only validated for Visa. Possible values:<br><br>**match**, **partialMatch**, **noMatch** |

## Example

```python
from adyen.models.payment_validations_name_result_response_2 import PaymentValidationsNameResultResponse2

payment_validations_name_result_response_2 = PaymentValidationsNameResultResponse2(
    first_name='firstName2',
    full_name='fullName2',
    last_name='lastName6',
    middle_name='middleName0'
)
```

