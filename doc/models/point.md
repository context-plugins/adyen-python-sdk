
# Point

*This model accepts additional fields of type Any.*

## Structure

`Point`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x` | `str` | Required | The hexadecimal value of the coordinates of a point on the abscissa. |
| `y` | `str` | Required | The hexadecimal value of the coordinates of a point on the ordinate. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.point import Point

point = Point(
    x='X6',
    y='Y0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

