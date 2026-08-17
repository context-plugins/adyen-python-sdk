
# Identity 2

Contains the identity details of the party.

## Structure

`Identity2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_legal_name` | `str` | Required | The complete legal name of the individual or entity. |
| `name` | `str` | Required | A commonly used or human-readable name for the individual or entity. |

## Example

```python
from adyen.models.identity_2 import Identity2

identity_2 = Identity2(
    full_legal_name='fullLegalName8',
    name='name0'
)
```

