
# Resource Reference 5

The account holder associated with the balance account involved in the transfer.

*This model accepts additional fields of type Any.*

## Structure

`ResourceReference5`

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

from adyen.models.resource_reference_5 import ResourceReference5

resource_reference_5 = ResourceReference5(
    description='description8',
    id='id8',
    reference='reference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

