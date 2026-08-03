
# Geographic Coordinates

*This model accepts additional fields of type Any.*

## Structure

`GeographicCoordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `str` | Required | Angular distance of a location on the earth south or north of the equator.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `longitude` | `str` | Required | Angular measurement of the distance of a location on the earth east or west of the Greenwich observatory.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.geographic_coordinates import GeographicCoordinates

geographic_coordinates = GeographicCoordinates(
    latitude='Latitude6',
    longitude='Longitude4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

