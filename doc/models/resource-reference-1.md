
# Resource Reference 1

Contains information about the balance account involved in the transfer.

*This model accepts additional fields of type Any.*

## Structure

`ResourceReference1`

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

from adyen.models.resource_reference_1 import ResourceReference1

resource_reference_1 = ResourceReference1(
    description='description8',
    id='id8',
    reference='reference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

