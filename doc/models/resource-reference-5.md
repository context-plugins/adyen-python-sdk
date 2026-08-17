
# Resource Reference 5

The account holder associated with the balance account involved in the transfer.

## Structure

`ResourceReference5`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |

## Example

```python
from adyen.models.resource_reference_5 import ResourceReference5

resource_reference_5 = ResourceReference5(
    description='description8',
    id='id8',
    reference='reference6'
)
```

