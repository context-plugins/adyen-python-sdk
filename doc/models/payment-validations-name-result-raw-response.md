
# Payment Validations Name Result Raw Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentValidationsNameResultRawResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `first_name` | `str` | Optional | The raw first name validation result that Adyen received from the scheme. First name validation result is only returned for Visa. |
| `full_name` | `str` | Optional | The raw full name validation result that Adyen received from the scheme. Full name is the only field that is validated for Mastercard |
| `last_name` | `str` | Optional | The raw last name validation result that Adyen received from the scheme. Last name validation result is only returned for Visa. |
| `middle_name` | `str` | Optional | The raw middle name validation result that Adyen received from the scheme. Middle name validation result is only returned for Visa. |
| `status` | `str` | Optional | The raw name validation status value that Adyen received from the scheme. Only returned for Visa. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_validations_name_result_raw_response import PaymentValidationsNameResultRawResponse

payment_validations_name_result_raw_response = PaymentValidationsNameResultRawResponse(
    first_name='firstName2',
    full_name='fullName2',
    last_name='lastName6',
    middle_name='middleName0',
    status='status6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

