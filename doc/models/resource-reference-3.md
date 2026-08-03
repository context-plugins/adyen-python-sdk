
# Resource Reference 3

Contains information about the account holder associated with the `balanceAccount`.

*This model accepts additional fields of type Any.*

## Structure

`ResourceReference3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | The description of the resource. |
| `id` | `str` | Optional | The unique identifier of the resource. |
| `reference` | `str` | Optional | The reference for the resource. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.resource_reference_3 import ResourceReference3

resource_reference_3 = ResourceReference3(
    description='description4',
    id='id6',
    reference='reference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

