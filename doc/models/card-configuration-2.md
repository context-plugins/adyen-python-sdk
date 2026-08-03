
# Card Configuration 2

Contains information about the configuration profile for your cards. The configuration profile consists of settings required when creating a physical or a virtual card. You identify a configuration profile with its `configurationProfileId`.

When you provide this field in a request, you can override the settings of an existing configuration profile.

Reach out to your Adyen contact to get the values that you can send in this object.

*This model accepts additional fields of type Any.*

## Structure

`CardConfiguration2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `activation` | `str` | Optional | The activation label attached to the card that contains the activation instructions.<br><br>This field overrides the activation label design ID defined in the card configuration profile. |
| `activation_url` | `str` | Optional | Your app's URL, if you want to activate cards through your app. For example, **my-app://ref1236a7d**. A QR code is created based on this URL, and is included in the carrier. Before you use this field, reach out to your Adyen contact to set up the QR code process.<br><br>Maximum length: 255 characters.<br><br>**Constraints**: *Maximum Length*: `255` |
| `bulk_address` | [`BulkAddress`](../../doc/models/bulk-address.md) | Optional | - |
| `card_image_id` | `str` | Optional | The unique identifier of the card image. This image is printed on the full front of the card. |
| `carrier` | `str` | Optional | The letter or packaging to which the card is attached.<br><br>This field overrides the carrier design ID defined in the card configuration profile. |
| `carrier_image_id` | `str` | Optional | The unique identifier of the carrier image. This image is printed on the letter to which the card is attached. |
| `configuration_profile_id` | `str` | Required | The unique identifier of the card configuration profile that contains the settings that are applied to the card. For example, the envelope and PIN mailer designs or the logistics company handling the shipment.<br><br>You can override some of the existing settings in the configuration profile by providing the corresponding fields in the `configuration` object. For example, send the `shipmentMethod` to override the logistics company defined in the card configuration profile. |
| `currency` | `str` | Optional | The three-letter [ISO-4217](https://en.wikipedia.org/wiki/ISO_4217) currency code of the card. For example, **EUR**.<br><br>This field overrides the existing currency setting on the card configuration profile. |
| `envelope` | `str` | Optional | Overrides the envelope design ID defined in the card configuration profile. |
| `insert` | `str` | Optional | Any additional material, such as marketing material, that is shipped together with the card.<br><br>This field overrides the insert design ID defined in the card configuration profile. |
| `language` | `str` | Optional | The two-letter [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) language code of the card. For example, **en**. |
| `logo_image_id` | `str` | Optional | The unique identifier of the logo image. This image is printed on the partial front of the card, for example, a logo on the upper right corner. |
| `pin_mailer` | `str` | Optional | The letter on which the PIN of the card is printed.<br><br>This field overrides the PIN mailer design ID defined in the card configuration profile. |
| `print_line` | `str` | Optional | Print Line.<br><br>Text printed on the physical card below the cardholder name. You provide the value, which can be up to 26 characters. |
| `shipment_method` | `str` | Optional | The logistics company that ships the card.<br><br>This field overrides the logistics company defined in the card configuration profile. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bulk_address import BulkAddress
from adyen.models.card_configuration_2 import CardConfiguration2

card_configuration_2 = CardConfiguration2(
    configuration_profile_id='configurationProfileId8',
    activation='activation4',
    activation_url='activationUrl0',
    bulk_address=BulkAddress(
        country='country0',
        city='city6',
        company='company6',
        email='email0',
        house_number_or_name='houseNumberOrName4',
        line_1='line18',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card_image_id='cardImageId2',
    carrier='carrier0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

