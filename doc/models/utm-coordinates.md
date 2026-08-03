
# Utm Coordinates

*This model accepts additional fields of type Any.*

## Structure

`UtmCoordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `utm_zone` | `str` | Required | UTM grid zone combination of the longitude zone (1 to 60) and the latitude band (C to X, excluding I and O).<br><br>**Constraints**: *Pattern*: `^.+$` |
| `utm_eastward` | `str` | Required | X-coordinate of the Universal Transverse Mercator coordinate system.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `utm_northward` | `str` | Required | Y-coordinate of the Universal Transverse Mercator coordinate system.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.utm_coordinates import UtmCoordinates

utm_coordinates = UtmCoordinates(
    utm_zone='UTMZone2',
    utm_eastward='UTMEastward4',
    utm_northward='UTMNorthward4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

