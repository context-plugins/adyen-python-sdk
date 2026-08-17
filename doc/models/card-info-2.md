
# Card Info 2

Object that contains information about the card payment instrument.

## Structure

`CardInfo2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authentication` | [`Authentication1`](../../doc/models/authentication-1.md) | Optional | Contains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to [3D Secure and digital wallets](https://docs.adyen.com/issuing/3d-secure-and-wallets) for more information. |
| `brand` | `str` | Required | The brand of the physical or the virtual card.<br>Possible values: **visa**, **mc**. |
| `brand_variant` | `str` | Required | The brand variant of the physical or the virtual card. For example, **visadebit** or **mcprepaid**.<br><br>> Reach out to your Adyen contact to get the values relevant for your integration. |
| `cardholder_name` | `str` | Required | The name of the cardholder.<br>Maximum length: 26 characters.<br><br>**Constraints**: *Maximum Length*: `26` |
| `configuration` | [`CardConfiguration2`](../../doc/models/card-configuration-2.md) | Optional | Contains information about the configuration profile for your cards. The configuration profile consists of settings required when creating a physical or a virtual card. You identify a configuration profile with its `configurationProfileId`.<br><br>When you provide this field in a request, you can override the settings of an existing configuration profile.<br><br>Reach out to your Adyen contact to get the values that you can send in this object. |
| `delivery_contact` | [`DeliveryContact1`](../../doc/models/delivery-contact-1.md) | Optional | The delivery contact (name and address) for physical card delivery. |
| `form_factor` | [`FormFactor1Enum`](../../doc/models/form-factor-1-enum.md) | Required | The form factor of the card.<br>Possible values: **virtual**, **physical**. |
| `three_d_secure` | `str` | Optional | The 3DS configuration of the physical or the virtual card. Possible values: **fullySupported**, **secureCorporate**.<br><br>> Reach out to your Adyen contact to get the values relevant for your integration. |
| `usage` | `str` | Optional | Specifies how many times the card can be used. Possible values: **singleUse**, **multiUse**.<br><br>> Reach out to your Adyen contact to determine the value relevant for your integration. |

## Example

```python
from adyen.models.authentication_1 import Authentication1
from adyen.models.bulk_address_1 import BulkAddress1
from adyen.models.card_configuration_2 import CardConfiguration2
from adyen.models.card_info_2 import CardInfo2
from adyen.models.delivery_contact_1 import DeliveryContact1
from adyen.models.form_factor_1_enum import FormFactor1Enum
from adyen.models.name import Name
from adyen.models.phone_11 import Phone11
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.store_location import StoreLocation
from adyen.models.type_410_enum import Type410Enum
from adyen.models.vias_phone_number import ViasPhoneNumber

card_info_2 = CardInfo2(
    brand='brand2',
    brand_variant='brandVariant0',
    cardholder_name='cardholderName6',
    form_factor=FormFactor1Enum.PHYSICAL,
    authentication=Authentication1(
        email='email8',
        password='password2',
        phone=Phone11(
            number='number8',
            mtype=Type410Enum.LANDLINE
        )
    ),
    configuration=CardConfiguration2(
        configuration_profile_id='configurationProfileId6',
        activation='activation2',
        activation_url='activationUrl8',
        bulk_address=BulkAddress1(
            country='country0',
            city='city6',
            company='company6',
            email='email0',
            house_number_or_name='houseNumberOrName4',
            line_1='line18'
        ),
        card_image_id='cardImageId0',
        carrier='carrier8'
    ),
    delivery_contact=DeliveryContact1(
        address=StoreLocation(
            country='country0',
            city='city6',
            line_1='line18',
            line_2='line20',
            line_3='line38',
            postal_code='postalCode8'
        ),
        name=Name(
            first_name='firstName4',
            last_name='lastName4'
        ),
        company='company4',
        email='email0',
        full_phone_number='fullPhoneNumber0',
        phone_number=ViasPhoneNumber(
            phone_country_code='phoneCountryCode8',
            phone_number='phoneNumber0',
            phone_type=PhoneTypeEnum.FAX
        ),
        web_address='webAddress4'
    ),
    three_d_secure='threeDSecure6',
    usage='usage6'
)
```

