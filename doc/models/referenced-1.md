
# Referenced 1

Settings for referenced refunds.

*This model accepts additional fields of type Any.*

## Structure

`Referenced1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_standalone_refunds` | `bool` | Optional | Indicates whether referenced refunds are enabled on the standalone terminal. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.referenced_1 import Referenced1

referenced_1 = Referenced1(
    enable_standalone_refunds=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

