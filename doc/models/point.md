
# Point

## Structure

`Point`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x` | `str` | Required | The hexadecimal value of the coordinates of a point on the abscissa. |
| `y` | `str` | Required | The hexadecimal value of the coordinates of a point on the ordinate. |

## Example

```python
from adyen.models.point import Point

point = Point(
    x='X6',
    y='Y0'
)
```

