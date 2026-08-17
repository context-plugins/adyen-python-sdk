
# Delete Shareholder Request

## Structure

`DeleteShareholderRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder from which to delete the Shareholders. |
| `shareholder_codes` | `List[str]` | Required | The code(s) of the Shareholders to be deleted. |

## Example

```python
from adyen.models.delete_shareholder_request import DeleteShareholderRequest

delete_shareholder_request = DeleteShareholderRequest(
    account_holder_code='accountHolderCode8',
    shareholder_codes=[
        'shareholderCodes7',
        'shareholderCodes8'
    ]
)
```

