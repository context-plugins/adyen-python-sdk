
# Migration Data 2

Details of the account holder migrated to the balance platform.

## Structure

`MigrationData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_holder_id` | `str` | Optional | The unique identifier of the account holder in the balance platform. |
| `balance_platform` | `str` | Optional | The unique identifier of the balance platfrom to which the account holder was migrated. |
| `migrated` | `bool` | Optional | Set to **true** if the account holder has been migrated. |
| `migrated_accounts` | [`List[MigratedAccounts]`](../../doc/models/migrated-accounts.md) | Optional | Contains the mapping of virtual account codes (classic integration) to the balance account codes (balance platform) associated with the migrated account holder. |
| `migrated_shareholders` | [`List[MigratedShareholders]`](../../doc/models/migrated-shareholders.md) | Optional | Contains the mapping of shareholders associated with the migrated legal entities. |
| `migrated_stores` | [`List[MigratedStores]`](../../doc/models/migrated-stores.md) | Optional | Contains the mapping of business lines and stores associated with the migrated account holder. |
| `migration_date` | `datetime` | Optional | The date when account holder was migrated. |

## Example

```python
from adyen.models.migrated_accounts import MigratedAccounts
from adyen.models.migrated_shareholders import MigratedShareholders
from adyen.models.migration_data_2 import MigrationData2

migration_data_2 = MigrationData2(
    account_holder_id='accountHolderId2',
    balance_platform='balancePlatform8',
    migrated=False,
    migrated_accounts=[
        MigratedAccounts(
            account_code='accountCode6',
            balance_account_id='balanceAccountId2'
        )
    ],
    migrated_shareholders=[
        MigratedShareholders(
            legal_entity_code='legalEntityCode0',
            shareholder_code='shareholderCode4'
        )
    ]
)
```

