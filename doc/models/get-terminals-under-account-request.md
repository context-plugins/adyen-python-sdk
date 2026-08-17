
# Get Terminals Under Account Request

## Structure

`GetTerminalsUnderAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_account` | `str` | Required | Your company account. If you only specify this parameter, the response includes all terminals at all account levels. |
| `merchant_account` | `str` | Optional | The merchant account. This is required if you are retrieving the terminals assigned to a store.If you don't specify a `store` the response includes the terminals assigned to the specified merchant account and the terminals assigned to the stores under this merchant account. |
| `store` | `str` | Optional | The store code of the store. With this parameter, the response only includes the terminals assigned to the specified store. |

## Example

```python
from adyen.models.get_terminals_under_account_request import GetTerminalsUnderAccountRequest

get_terminals_under_account_request = GetTerminalsUnderAccountRequest(
    company_account='companyAccount6',
    merchant_account='merchantAccount4',
    store='store2'
)
```

