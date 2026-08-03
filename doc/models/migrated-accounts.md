
# Migrated Accounts

*This model accepts additional fields of type Any.*

## Structure

`MigratedAccounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The unique identifier of the account of the migrated account holder in the classic integration. |
| `balance_account_id` | `str` | Optional | The unique identifier of the account of the migrated account holder in the balance platform. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.migrated_accounts import MigratedAccounts

migrated_accounts = MigratedAccounts(
    account_code='accountCode2',
    balance_account_id='balanceAccountId0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

