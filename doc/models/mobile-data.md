
# Mobile Data

Mobile phone is used as a payment instrument for the transaction.
Information related to the mobile for the payment transaction.

*This model accepts additional fields of type Any.*

## Structure

`MobileData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mobile_country_code` | `int` | Optional | Identifies the country of a mobile phone operator.<br>If data available.<br><br>**Constraints**: `>= 3`, `<= 3` |
| `mobile_network_code` | `int` | Optional | Identifies the mobile phone operator inside a country.<br>If data available.<br><br>**Constraints**: `>= 2`, `<= 3` |
| `masked_msisdn` | `int` | Optional | Masked Mobile Subscriber Integrated Service Digital Network.<br>If data available. |
| `geolocation` | [`Geolocation`](../../doc/models/geolocation.md) | Optional | - |
| `protected_mobile_data` | `str` | Optional | Sensitive information related to the mobile phone, protected by CMS.<br>SensitiveMobileData. |
| `sensitive_mobile_data` | [`SensitiveMobileData`](../../doc/models/sensitive-mobile-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.mobile_data import MobileData
from adyen.models.utm_coordinates import UtmCoordinates

mobile_data = MobileData(
    mobile_country_code=3,
    mobile_network_code=3,
    masked_msisdn=22,
    geolocation=Geolocation(
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
    ),
    protected_mobile_data='ProtectedMobileData8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

