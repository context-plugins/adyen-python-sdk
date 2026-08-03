
# Referenced

*This model accepts additional fields of type Any.*

## Structure

`Referenced`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_standalone_refunds` | `bool` | Optional | Indicates whether referenced refunds are enabled on the standalone terminal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.referenced import Referenced

referenced = Referenced(
    enable_standalone_refunds=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

