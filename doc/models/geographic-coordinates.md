
# Geographic Coordinates

## Structure

`GeographicCoordinates`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `latitude` | `str` | Required | Angular distance of a location on the earth south or north of the equator.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `longitude` | `str` | Required | Angular measurement of the distance of a location on the earth east or west of the Greenwich observatory.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.geographic_coordinates import GeographicCoordinates

geographic_coordinates = GeographicCoordinates(
    latitude='Latitude6',
    longitude='Longitude4'
)
```

