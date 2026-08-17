
# Resource Reference 3

Contains information about the account holder associated with the `balanceAccount`.

## Structure

`ResourceReference3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |

## Example

```python
from adyen.models.resource_reference_3 import ResourceReference3

resource_reference_3 = ResourceReference3(
    description='description4',
    id='id6',
    reference='reference8'
)
```

