
# Close Account Request

## Structure

`CloseAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of account to be closed. |

## Example

```python
from adyen.models.close_account_request import CloseAccountRequest

close_account_request = CloseAccountRequest(
    account_code='accountCode0'
)
```

