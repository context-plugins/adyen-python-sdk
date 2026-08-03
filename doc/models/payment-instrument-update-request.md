
# Payment Instrument Update Request

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrumentUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the balance account associated with this payment instrument.<br><br>> You can only change the balance account ID if the payment instrument has **inactive** status. |
| `card` | [`CardInfo`](../../doc/models/card-info.md) | Optional | - |
| `status` | [`Status10`](../../doc/models/status-10.md) | Optional | - |
| `status_comment` | `str` | Optional | Comment for the status of the payment instrument.<br><br>Required if `statusReason` is **other**. |
| `status_reason` | [`StatusReason2`](../../doc/models/status-reason-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_15 import Address15
from adyen.models.authentication import Authentication
from adyen.models.bulk_address import BulkAddress
from adyen.models.card_configuration import CardConfiguration
from adyen.models.card_info import CardInfo
from adyen.models.delivery_contact import DeliveryContact
from adyen.models.form_factor_1 import FormFactor1
from adyen.models.name_5 import Name5
from adyen.models.payment_instrument_update_request import PaymentInstrumentUpdateRequest
from adyen.models.phone import Phone
from adyen.models.phone_number_3 import PhoneNumber3
from adyen.models.phone_type import PhoneType
from adyen.models.status_10 import Status10
from adyen.models.status_reason_2 import StatusReason2
from adyen.models.type_4 import Type4

payment_instrument_update_request = PaymentInstrumentUpdateRequest(
    balance_account_id='balanceAccountId0',
    card=CardInfo(
        brand='brand0',
        brand_variant='brandVariant8',
        cardholder_name='cardholderName8',
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
        three_d_secure='threeDSecure8',
        usage='usage4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    status=Status10.ACTIVE,
    status_comment='statusComment8',
    status_reason=StatusReason2.SUSPECTEDFRAUD,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

