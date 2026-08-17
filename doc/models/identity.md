
# Identity

## Structure

`Identity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `full_legal_name` | `str` | Required | The complete legal name of the individual or entity. |
| `name` | `str` | Required | A commonly used or human-readable name for the individual or entity. |

## Example

```python
from adyen.models.identity import Identity

identity = Identity(
    full_legal_name='fullLegalName2',
    name='name4'
)
```

