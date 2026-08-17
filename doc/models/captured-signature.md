
# Captured Signature

## Structure

`CapturedSignature`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `area_size` | [`AreaSize1`](../../doc/models/area-size-1.md) | Optional | Size of an area. Contain the size of the pad area where the signature is written, given with the maximum abscissa and ordinate values (X and Y). The maximum value is FFFF. |
| `signature_point` | [`List[Point]`](../../doc/models/point.md) | Optional | Coordinates of a point where the pen changes direction or lift. Contain the Coordinates of a point of the written signature where the pen changes direction or lift where (X and Y). When the signer lifts the pen, both X and Y have the value FFFF. |

## Example

```python
from adyen.models.area_size_1 import AreaSize1
from adyen.models.captured_signature import CapturedSignature
from adyen.models.point import Point

captured_signature = CapturedSignature(
    area_size=AreaSize1(
        x='X4',
        y='Y8'
    ),
    signature_point=[
        Point(
            x='X0',
            y='Y6'
        ),
        Point(
            x='X0',
            y='Y6'
        ),
        Point(
            x='X0',
            y='Y6'
        )
    ]
)
```

