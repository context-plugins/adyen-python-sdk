
# Delivery Address

The address of the store.

*This model accepts additional fields of type Any.*

## Structure

`DeliveryAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Optional | The name of the city. |
| `country` | `str` | Required | The two-character ISO-3166-1 alpha-2 country code. For example, **US**.<br><br>> If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`. |
| `line_1` | `str` | Optional | The name of the street. Do not include the number of the building.<br><br>For example, if the address is Simon Carmiggeltstraat 6-50, provide **Simon Carmiggeltstraat**. |
| `line_2` | `str` | Optional | The number of the building.<br><br>For example, if the address is Simon Carmiggeltstraat 6-50, provide **6-50**. |
| `line_3` | `str` | Optional | Additional information about the delivery address. |
| `postal_code` | `str` | Optional | The postal code.<br>Maximum length:<br><br>* 5 digits for an address in the US.<br>* 10 characters for an address in all other countries. |
| `state_or_province` | `str` | Optional | The state or province code, maximum 3 characters. For example, **CA** for California in the US or **ON** for Ontario in Canada.<br><br>> Required for the US and Canada. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.delivery_address import DeliveryAddress

delivery_address = DeliveryAddress(
    country='country8',
    city='city4',
    line_1='line16',
    line_2='line28',
    line_3='line36',
    postal_code='postalCode6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

