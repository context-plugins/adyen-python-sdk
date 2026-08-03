
# Area Size

*This model accepts additional fields of type Any.*

## Structure

`AreaSize`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x` | `str` | Required | Abscissa of a point coordinates. The hexadecimal value in text of the abscissa of the coordinates of a point. Leading zero can be removed (e.g. 3BC, 0, and 1287). |
| `y` | `str` | Required | Ordinate of a point coordinates. The hexadecimal value in text of the ordinate of the coordinates of a point. Leading zero can be removed (e.g. 3BC, 0, and 1287). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.area_size import AreaSize

area_size = AreaSize(
    x='X6',
    y='Y0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

