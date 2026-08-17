
# Un Suspend Account Holder Request

## Structure

`UnSuspendAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder to be reinstated. |

## Example

```python
from adyen.models.un_suspend_account_holder_request import UnSuspendAccountHolderRequest

un_suspend_account_holder_request = UnSuspendAccountHolderRequest(
    account_holder_code='accountHolderCode2'
)
```

