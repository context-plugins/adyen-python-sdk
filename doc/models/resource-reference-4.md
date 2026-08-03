
# Resource Reference 4

Contains information about the balance account involved in the transaction.

*This model accepts additional fields of type Any.*

## Structure

`ResourceReference4`

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

from adyen.models.resource_reference_4 import ResourceReference4

resource_reference_4 = ResourceReference4(
    description='description4',
    id='id4',
    reference='reference0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

