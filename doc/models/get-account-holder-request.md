
# Get Account Holder Request

## Structure

`GetAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The code of the account of which to retrieve the details.<br><br>> Required if no `accountHolderCode` is provided. |
| `account_holder_code` | `str` | Optional | The code of the account holder of which to retrieve the details.<br><br>> Required if no `accountCode` is provided. |
| `show_details` | `bool` | Optional | True if the request should return the account holder details |

## Example

```python
from adyen.models.get_account_holder_request import GetAccountHolderRequest

get_account_holder_request = GetAccountHolderRequest(
    account_code='accountCode0',
    account_holder_code='accountHolderCode4',
    show_details=False
)
```

