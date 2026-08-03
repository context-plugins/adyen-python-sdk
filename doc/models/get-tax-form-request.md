
# Get Tax Form Request

*This model accepts additional fields of type Any.*

## Structure

`GetTaxFormRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The account holder code you provided when you created the account holder. |
| `form_type` | `str` | Required | Type of the requested tax form. For example, 1099-K. |
| `year` | `int` | Required | Applicable tax year in the YYYY format. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_tax_form_request import GetTaxFormRequest

get_tax_form_request = GetTaxFormRequest(
    account_holder_code='accountHolderCode4',
    form_type='formType6',
    year=156,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

