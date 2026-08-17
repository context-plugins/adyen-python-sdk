
# Geolocation 1

Geographic location specified by geographic or UTM coordinates.
If data available.

## Structure

`Geolocation1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `geographic_coordinates` | [`GeographicCoordinates`](../../doc/models/geographic-coordinates.md) | Optional | - |
| `utm_coordinates` | [`UTMCoordinates`](../../doc/models/utm-coordinates.md) | Optional | - |

## Example

```python
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.utm_coordinates import UTMCoordinates

geolocation_1 = Geolocation1(
    geographic_coordinates=GeographicCoordinates(
        latitude='Latitude4',
        longitude='Longitude2'
    ),
    utm_coordinates=UTMCoordinates(
        utm_zone='UTMZone6',
        utm_eastward='UTMEastward0',
        utm_northward='UTMNorthward0'
    )
)
```

