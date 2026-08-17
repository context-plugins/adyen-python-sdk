
# Suspend Account Holder Request

## Structure

`SuspendAccountHolderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the account holder to be suspended. |

## Example

```python
from adyen.models.suspend_account_holder_request import SuspendAccountHolderRequest

suspend_account_holder_request = SuspendAccountHolderRequest(
    account_holder_code='accountHolderCode2'
)
```

