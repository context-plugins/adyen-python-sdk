
# Authorised Card Users

*This model accepts additional fields of type Any.*

## Structure

`AuthorisedCardUsers`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `legal_entity_ids` | `List[str]` | Optional | The legal entity IDs of the authorized card users linked to the specified payment instrument. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.authorised_card_users import AuthorisedCardUsers

authorised_card_users = AuthorisedCardUsers(
    legal_entity_ids=[
        'legalEntityIds4',
        'legalEntityIds5'
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

