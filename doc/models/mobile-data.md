
# Mobile Data

Mobile phone is used as a payment instrument for the transaction.
Information related to the mobile for the payment transaction.

## Structure

`MobileData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mobile_country_code` | `int` | Optional | Identifies the country of a mobile phone operator.<br>If data available.<br><br>**Constraints**: `>= 3`, `<= 3` |
| `mobile_network_code` | `int` | Optional | Identifies the mobile phone operator inside a country.<br>If data available.<br><br>**Constraints**: `>= 2`, `<= 3` |
| `masked_msisdn` | `int` | Optional | Masked Mobile Subscriber Integrated Service Digital Network.<br>If data available. |
| `geolocation` | [`Geolocation1`](../../doc/models/geolocation-1.md) | Optional | Geographic location specified by geographic or UTM coordinates.<br>If data available. |
| `protected_mobile_data` | `str` | Optional | Sensitive information related to the mobile phone, protected by CMS.<br>SensitiveMobileData. |
| `sensitive_mobile_data` | [`SensitiveMobileData1`](../../doc/models/sensitive-mobile-data-1.md) | Optional | Sensitive information related to the mobile phone.<br>If unprotected mobile data. |

## Example

```python
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.mobile_data import MobileData
from adyen.models.utm_coordinates import UTMCoordinates

mobile_data = MobileData(
    mobile_country_code=3,
    mobile_network_code=3,
    masked_msisdn=22,
    geolocation=Geolocation1(
        geographic_coordinates=GeographicCoordinates(
            latitude='Latitude4',
            longitude='Longitude2'
        ),
        utm_coordinates=UTMCoordinates(
            utm_zone='UTMZone6',
            utm_eastward='UTMEastward0',
            utm_northward='UTMNorthward0'
        )
    ),
    protected_mobile_data='ProtectedMobileData8'
)
```

