
# UTM Coordinates

## Structure

`UTMCoordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `utm_zone` | `str` | Required | UTM grid zone combination of the longitude zone (1 to 60) and the latitude band (C to X, excluding I and O).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `utm_eastward` | `str` | Required | X-coordinate of the Universal Transverse Mercator coordinate system.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `utm_northward` | `str` | Required | Y-coordinate of the Universal Transverse Mercator coordinate system.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.utm_coordinates import UTMCoordinates

utm_coordinates = UTMCoordinates(
    utm_zone='UTMZone2',
    utm_eastward='UTMEastward4',
    utm_northward='UTMNorthward4'
)
```

