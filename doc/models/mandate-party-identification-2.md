
# Mandate Party Identification 2

Contains information about the owner of the counterparty bank account.

## Structure

`MandatePartyIdentification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_name` | `str` | Optional | The full name of the entity that owns the bank account.<br><br>Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space. |

## Example

```python
from adyen.models.mandate_party_identification_2 import MandatePartyIdentification2

mandate_party_identification_2 = MandatePartyIdentification2(
    full_name='fullName6'
)
```

