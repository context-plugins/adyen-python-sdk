
# Geolocation

## Structure

`Geolocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `geographic_coordinates` | [`GeographicCoordinates`](../../doc/models/geographic-coordinates.md) | Optional | - |
| `utm_coordinates` | [`UTMCoordinates`](../../doc/models/utm-coordinates.md) | Optional | - |

## Example

```python
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.utm_coordinates import UTMCoordinates

geolocation = Geolocation(
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

