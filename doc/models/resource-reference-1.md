
# Resource Reference 1

Contains information about the balance account involved in the transfer.

## Structure

`ResourceReference1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |

## Example

```python
from adyen.models.resource_reference_1 import ResourceReference1

resource_reference_1 = ResourceReference1(
    description='description8',
    id='id8',
    reference='reference4'
)
```

