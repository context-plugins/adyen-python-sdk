
# Show Pages 2

Contains indicators whether specific pages must be shown to the account holder.

*This model accepts additional fields of type Any.*

## Structure

`ShowPages2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_details_summary_page` | `bool` | Optional | Indicates whether the page with bank account details must be shown. Defaults to **true**. |
| `bank_verification_page` | `bool` | Optional | Indicates whether the bank check instant verification' details must be shown. Defaults to **true**. |
| `business_details_summary_page` | `bool` | Optional | Indicates whether the page with the company's or organization's details must be shown. Defaults to **true**. |
| `checks_overview_page` | `bool` | Optional | Indicates whether the checks overview page must be shown. Defaults to **false**. |
| `individual_details_summary_page` | `bool` | Optional | Indicates whether the page with the individual's details must be shown. Defaults to **true**. |
| `legal_arrangements_details_summary_page` | `bool` | Optional | Indicates whether the page with the legal arrangements' details must be shown. Defaults to **true**. |
| `manual_bank_account_page` | `bool` | Optional | Indicates whether the page to manually add bank account' details must be shown. Defaults to **true**. |
| `shareholder_details_summary_page` | `bool` | Optional | Indicates whether the page with the shareholders' details must be shown. Defaults to **true**. |
| `welcome_page` | `bool` | Optional | Indicates whether the welcome page must be shown. Defaults to **false**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.show_pages_2 import ShowPages2

show_pages_2 = ShowPages2(
    bank_details_summary_page=False,
    bank_verification_page=False,
    business_details_summary_page=False,
    checks_overview_page=False,
    individual_details_summary_page=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

