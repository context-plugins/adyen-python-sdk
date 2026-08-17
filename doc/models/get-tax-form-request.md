
# Get Tax Form Request

## Structure

`GetTaxFormRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The account holder code you provided when you created the account holder. |
| `form_type` | `str` | Required | Type of the requested tax form. For example, 1099-K. |
| `year` | `int` | Required | Applicable tax year in the YYYY format. |

## Example

```python
from adyen.models.get_tax_form_request import GetTaxFormRequest

get_tax_form_request = GetTaxFormRequest(
    account_holder_code='accountHolderCode4',
    form_type='formType6',
    year=156
)
```

