
# Delete Bank Account Request

## Structure

`DeleteBankAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder from which to delete the Bank Account(s). |
| `bank_account_uui_ds` | `List[str]` | Required | The code(s) of the Bank Accounts to be deleted. |

## Example

```python
from adyen.models.delete_bank_account_request import DeleteBankAccountRequest

delete_bank_account_request = DeleteBankAccountRequest(
    account_holder_code='accountHolderCode8',
    bank_account_uui_ds=[
        'bankAccountUUIDs1'
    ]
)
```

