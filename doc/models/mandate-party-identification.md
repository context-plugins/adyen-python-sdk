
# Mandate Party Identification

## Structure

`MandatePartyIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_name` | `str` | Optional | The full name of the entity that owns the bank account.<br><br>Supported characters: [a-z] [A-Z] [0-9] , . ; : - — / \ + & ! ? @ ( ) " ' and space. |

## Example

```python
from adyen.models.mandate_party_identification import MandatePartyIdentification

mandate_party_identification = MandatePartyIdentification(
    full_name='fullName8'
)
```

