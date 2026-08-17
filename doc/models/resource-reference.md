
# Resource Reference

## Structure

`ResourceReference`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |

## Example

```python
from adyen.models.resource_reference import ResourceReference

resource_reference = ResourceReference(
    description='description8',
    id='id8',
    reference='reference6'
)
```

