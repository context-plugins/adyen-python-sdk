
# Shopper Tax Info

*This model accepts additional fields of type Any.*

## Structure

`ShopperTaxInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tax_country_code` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code associated with the provided tax identification number.<br>Currently used only for Indian PA-CB tax verification, when applicable.<br><br>**Constraints**: *Maximum Length*: `2` |
| `tax_identification_number` | `str` | Required | The shopper’s tax identification number.<br><br>**Constraints**: *Maximum Length*: `20` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.shopper_tax_info import ShopperTaxInfo

shopper_tax_info = ShopperTaxInfo(
    tax_country_code='taxCountryCode0',
    tax_identification_number='taxIdentificationNumber8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

