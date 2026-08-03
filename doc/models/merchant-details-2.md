
# Merchant Details 2

Additional data for merchants who don't use Adyen as the payment authorisation gateway.

*This model accepts additional fields of type Any.*

## Structure

`MerchantDetails2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `country_code` | `str` | Optional | 2-letter ISO 3166 country code of the card acceptor location.<br><br>> This parameter is required for the merchants who don't use Adyen as the payment authorisation gateway.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `enrolled_in_3_d_secure` | `bool` | Optional | If true, indicates that the merchant is enrolled in 3D Secure for the card network. |
| `mcc` | `str` | Optional | The merchant category code (MCC) is a four-digit number which relates to a particular market segment. This code reflects the predominant activity that is conducted by the merchant.<br><br>The list of MCCs can be found [here](https://en.wikipedia.org/wiki/Merchant_category_code). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.merchant_details_2 import MerchantDetails2

merchant_details_2 = MerchantDetails2(
    country_code='countryCode2',
    enrolled_in_3_d_secure=False,
    mcc='mcc2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

