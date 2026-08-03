
# Merchant Data

*This model accepts additional fields of type Any.*

## Structure

`MerchantData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `str` | Optional | The unique identifier of the merchant's acquirer. |
| `mcc` | `str` | Optional | The merchant category code. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant. |
| `name_location` | [`NameLocation`](../../doc/models/name-location.md) | Optional | - |
| `postal_code` | `str` | Optional | The postal code of the merchant. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.merchant_data import MerchantData
from adyen.models.name_location import NameLocation

merchant_data = MerchantData(
    acquirer_id='acquirerId0',
    mcc='mcc8',
    merchant_id='merchantId4',
    name_location=NameLocation(
        city='city6',
        country='country8',
        country_of_origin='countryOfOrigin0',
        name='name4',
        raw_data='rawData0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    postal_code='postalCode0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

