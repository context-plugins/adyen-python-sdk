
# Area Size 1

Size of an area. Contain the size of the pad area where the signature is written, given with the maximum abscissa and ordinate values (X and Y). The maximum value is FFFF.

## Structure

`AreaSize1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x` | `str` | Required | Abscissa of a point coordinates. The hexadecimal value in text of the abscissa of the coordinates of a point. Leading zero can be removed (e.g. 3BC, 0, and 1287). |
| `y` | `str` | Required | Ordinate of a point coordinates. The hexadecimal value in text of the ordinate of the coordinates of a point. Leading zero can be removed (e.g. 3BC, 0, and 1287). |

## Example

```python
from adyen.models.area_size_1 import AreaSize1

area_size_1 = AreaSize1(
    x='X6',
    y='Y0'
)
```

