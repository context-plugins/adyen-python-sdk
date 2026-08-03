
# Captured Signature 1

Numeric value of a handwritten signature. Contains the value of a handwritten signature, e.g. the signature of a cardholder on the merchant payment receipt. Only one format of the signature is allowed:

* The size of the pad area where the signature is written, given with the maximum abscissa and ordinate values.
* The sequence of coordinates where the pen changes direction or lift.

*This model accepts additional fields of type Any.*

## Structure

`CapturedSignature1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `area_size` | [`AreaSize`](../../doc/models/area-size.md) | Optional | - |
| `signature_point` | [`List[Point]`](../../doc/models/point.md) | Optional | Coordinates of a point where the pen changes direction or lift. Contain the Coordinates of a point of the written signature where the pen changes direction or lift where (X and Y). When the signer lifts the pen, both X and Y have the value FFFF. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.area_size import AreaSize
from adyen.models.captured_signature_1 import CapturedSignature1
from adyen.models.point import Point

captured_signature_1 = CapturedSignature1(
    area_size=AreaSize(
        x='X4',
        y='Y8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    signature_point=[
        Point(
            x='X0',
            y='Y6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Point(
            x='X0',
            y='Y6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Point(
            x='X0',
            y='Y6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

