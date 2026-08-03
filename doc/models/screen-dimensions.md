
# Screen Dimensions

*This model accepts additional fields of type Any.*

## Structure

`ScreenDimensions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `height` | `int` | Optional | - |
| `width` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.screen_dimensions import ScreenDimensions

screen_dimensions = ScreenDimensions(
    height=70,
    width=78,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

