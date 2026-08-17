
# Migrated Accounts

## Structure

`MigratedAccounts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Optional | The unique identifier of the account of the migrated account holder in the classic integration. |
| `balance_account_id` | `str` | Optional | The unique identifier of the account of the migrated account holder in the balance platform. |

## Example

```python
from adyen.models.migrated_accounts import MigratedAccounts

migrated_accounts = MigratedAccounts(
    account_code='accountCode2',
    balance_account_id='balanceAccountId0'
)
```

