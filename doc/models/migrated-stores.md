
# Migrated Stores

## Structure

`MigratedStores`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `business_line_id` | `str` | Optional | The unique identifier of the business line associated with the migrated account holder in the balance platform. |
| `store_code` | `str` | Optional | The unique identifier of the store associated with the migrated account holder in the classic integration. |
| `store_id` | `str` | Optional | The unique identifier of the store associated with the migrated account holder in the balance platform. |
| `store_reference` | `str` | Optional | Your reference for the store in the classic integration. The [Customer Area](https://ca-test.adyen.com/) uses this value for the store description. |

## Example

```python
from adyen.models.migrated_stores import MigratedStores

migrated_stores = MigratedStores(
    business_line_id='businessLineId2',
    store_code='storeCode0',
    store_id='storeId4',
    store_reference='storeReference0'
)
```

