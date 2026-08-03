
# Get Stores Under Account Request

*This model accepts additional fields of type Any.*

## Structure

`GetStoresUnderAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_account` | `str` | Required | The company account. If you only specify this parameter, the response includes the stores of all merchant accounts that are associated with the company account. |
| `merchant_account` | `str` | Optional | The merchant account. With this parameter, the response only includes the stores of the specified merchant account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.get_stores_under_account_request import GetStoresUnderAccountRequest

get_stores_under_account_request = GetStoresUnderAccountRequest(
    company_account='companyAccount6',
    merchant_account='merchantAccount6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

