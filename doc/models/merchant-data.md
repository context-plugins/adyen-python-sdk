
# Merchant Data

## Structure

`MerchantData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acquirer_id` | `str` | Optional | The unique identifier of the merchant's acquirer. |
| `mcc` | `str` | Optional | The merchant category code. |
| `merchant_id` | `str` | Optional | The unique identifier of the merchant. |
| `name_location` | [`NameLocation2`](../../doc/models/name-location-2.md) | Optional | Contains the name and location of the merchant. |
| `postal_code` | `str` | Optional | The postal code of the merchant. |

## Example

```python
from adyen.models.merchant_data import MerchantData
from adyen.models.name_location_2 import NameLocation2

merchant_data = MerchantData(
    acquirer_id='acquirerId0',
    mcc='mcc8',
    merchant_id='merchantId4',
    name_location=NameLocation2(
        city='city6',
        country='country8',
        country_of_origin='countryOfOrigin0',
        name='name4',
        raw_data='rawData0'
    ),
    postal_code='postalCode0'
)
```

