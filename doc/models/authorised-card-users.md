
# Authorised Card Users

## Structure

`AuthorisedCardUsers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_entity_ids` | `List[str]` | Optional | The legal entity IDs of the authorized card users linked to the specified payment instrument. |

## Example

```python
from adyen.models.authorised_card_users import AuthorisedCardUsers

authorised_card_users = AuthorisedCardUsers(
    legal_entity_ids=[
        'legalEntityIds4',
        'legalEntityIds5'
    ]
)
```

