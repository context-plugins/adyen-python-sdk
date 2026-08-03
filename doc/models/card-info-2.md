
# Card Info 2

Object that contains information about the card payment instrument.

*This model accepts additional fields of type Any.*

## Structure

`CardInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication` | [`Authentication`](../../doc/models/authentication.md) | Optional | - |
| `brand` | `str` | Required | The brand of the physical or the virtual card.<br>Possible values: **visa**, **mc**. |
| `brand_variant` | `str` | Required | The brand variant of the physical or the virtual card. For example, **visadebit** or **mcprepaid**.<br><br>> Reach out to your Adyen contact to get the values relevant for your integration. |
| `cardholder_name` | `str` | Required | The name of the cardholder.<br>Maximum length: 26 characters.<br><br>**Constraints**: *Maximum Length*: `26` |
| `configuration` | [`CardConfiguration`](../../doc/models/card-configuration.md) | Optional | - |
| `delivery_contact` | [`DeliveryContact`](../../doc/models/delivery-contact.md) | Optional | - |
| `form_factor` | [`FormFactor1`](../../doc/models/form-factor-1.md) | Required | - |
| `three_d_secure` | `str` | Optional | The 3DS configuration of the physical or the virtual card. Possible values: **fullySupported**, **secureCorporate**.<br><br>> Reach out to your Adyen contact to get the values relevant for your integration. |
| `usage` | `str` | Optional | Specifies how many times the card can be used. Possible values: **singleUse**, **multiUse**.<br><br>> Reach out to your Adyen contact to determine the value relevant for your integration. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_15 import Address15
from adyen.models.authentication import Authentication
from adyen.models.bulk_address import BulkAddress
from adyen.models.card_configuration import CardConfiguration
from adyen.models.card_info_2 import CardInfo2
from adyen.models.delivery_contact import DeliveryContact
from adyen.models.form_factor_1 import FormFactor1
from adyen.models.name_5 import Name5
from adyen.models.phone import Phone
from adyen.models.phone_number_3 import PhoneNumber3
from adyen.models.phone_type import PhoneType
from adyen.models.type_4 import Type4

card_info_2 = CardInfo2(
    brand='brand2',
    brand_variant='brandVariant0',
    cardholder_name='cardholderName6',
    form_factor=FormFactor1.PHYSICAL,
    authentication=Authentication(
        email='email8',
        password='password2',
        phone=Phone(
            number='number8',
            mtype=Type4.LANDLINE,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    configuration=CardConfiguration(
        configuration_profile_id='configurationProfileId6',
        activation='activation2',
        activation_url='activationUrl8',
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
        card_image_id='cardImageId0',
        carrier='carrier8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    delivery_contact=DeliveryContact(
        address=Address15(
            country='country0',
            city='city6',
            line_1='line18',
            line_2='line20',
            line_3='line38',
            postal_code='postalCode8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        name=Name5(
            first_name='firstName4',
            last_name='lastName4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        company='company4',
        email='email0',
        full_phone_number='fullPhoneNumber0',
        phone_number=PhoneNumber3(
            phone_country_code='phoneCountryCode8',
            phone_number='phoneNumber0',
            phone_type=PhoneType.FAX,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        web_address='webAddress4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    three_d_secure='threeDSecure6',
    usage='usage6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

