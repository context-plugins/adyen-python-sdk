
# Close Account Holder Request

## Structure

`CloseAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder to be closed. |

## Example

```python
from adyen.models.close_account_holder_request import CloseAccountHolderRequest

close_account_holder_request = CloseAccountHolderRequest(
    account_holder_code='accountHolderCode0'
)
```

