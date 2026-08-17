
# Account Party

## Structure

`AccountParty`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `identity` | [`Identity2`](../../doc/models/identity-2.md) | Required | Contains the identity details of the party. |
| `role` | [`PartyRole2Enum`](../../doc/models/party-role-2-enum.md) | Required | Specifies a role or capacity of the party in relation to the bank account. |

## Example

```python
from adyen.models.account_party import AccountParty
from adyen.models.identity_2 import Identity2
from adyen.models.party_role_2_enum import PartyRole2Enum

account_party = AccountParty(
    identity=Identity2(
        full_legal_name='fullLegalName2',
        name='name4'
    ),
    role=PartyRole2Enum.HOLDER
)
```

