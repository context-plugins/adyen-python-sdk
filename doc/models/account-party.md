
# Account Party

*This model accepts additional fields of type Any.*

## Structure

`AccountParty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `identity` | [`Identity`](../../doc/models/identity.md) | Required | - |
| `role` | [`PartyRole2`](../../doc/models/party-role-2.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.account_party import AccountParty
from adyen.models.identity import Identity
from adyen.models.party_role_2 import PartyRole2

account_party = AccountParty(
    identity=Identity(
        full_legal_name='fullLegalName2',
        name='name4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    role=PartyRole2.HOLDER,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

