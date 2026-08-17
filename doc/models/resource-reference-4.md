
# Resource Reference 4

Contains information about the balance account involved in the transaction.

## Structure

`ResourceReference4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |

## Example

```python
from adyen.models.resource_reference_4 import ResourceReference4

resource_reference_4 = ResourceReference4(
    description='description4',
    id='id4',
    reference='reference0'
)
```

