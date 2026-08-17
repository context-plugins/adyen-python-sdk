
# Party Role 2 Enum

Specifies a role or capacity of the party in relation to the bank account.

## Enumeration

`PartyRole2Enum`

## Fields

| Name |
|  --- |
| `HOLDER` |
| `AUTHORIZED_USER` |
| `OTHER` |
| `UNKNOWN` |

## Example

```python
from adyen.models.party_role_2_enum import PartyRole2Enum

party_role_2 = PartyRole2Enum.HOLDER
```

