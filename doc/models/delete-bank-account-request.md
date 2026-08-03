
# Delete Bank Account Request

*This model accepts additional fields of type Any.*

## Structure

`DeleteBankAccountRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_code` | `str` | Required | The code of the Account Holder from which to delete the Bank Account(s). |
| `bank_account_uui_ds` | `List[str]` | Required | The code(s) of the Bank Accounts to be deleted. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delete_bank_account_request import DeleteBankAccountRequest

delete_bank_account_request = DeleteBankAccountRequest(
    account_holder_code='accountHolderCode8',
    bank_account_uui_ds=[
        'bankAccountUUIDs1'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

