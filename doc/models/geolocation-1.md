
# Geolocation 1

Geographic location specified by geographic or UTM coordinates.
If data available.

*This model accepts additional fields of type Any.*

## Structure

`Geolocation1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `geographic_coordinates` | [`GeographicCoordinates`](../../doc/models/geographic-coordinates.md) | Optional | - |
| `utm_coordinates` | [`UtmCoordinates`](../../doc/models/utm-coordinates.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.utm_coordinates import UtmCoordinates

geolocation_1 = Geolocation1(
    geographic_coordinates=GeographicCoordinates(
        latitude='Latitude4',
        longitude='Longitude2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    utm_coordinates=UtmCoordinates(
        utm_zone='UTMZone6',
        utm_eastward='UTMEastward0',
        utm_northward='UTMNorthward0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

