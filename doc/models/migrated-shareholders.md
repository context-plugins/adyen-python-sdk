
# Migrated Shareholders

## Structure

`MigratedShareholders`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_entity_code` | `str` | Optional | The unique identifier of the legal entity of that shareholder in the balance platform. |
| `shareholder_code` | `str` | Optional | The unique identifier of the account of the migrated shareholder in the classic integration. |

## Example

```python
from adyen.models.migrated_shareholders import MigratedShareholders

migrated_shareholders = MigratedShareholders(
    legal_entity_code='legalEntityCode6',
    shareholder_code='shareholderCode0'
)
```

