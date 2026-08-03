
# Payment Instrument Info

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrumentInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Required | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id) associated with the payment instrument. |
| `bank_account` | [`BankAccountModel`](../../doc/models/bank-account-model.md) | Optional | - |
| `card` | [`CardInfo`](../../doc/models/card-info.md) | Optional | - |
| `description` | `str` | Optional | Your description for the payment instrument, maximum 300 characters.<br><br>**Constraints**: *Maximum Length*: `300` |
| `issuing_country_code` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**. |
| `payment_instrument_group_id` | `str` | Optional | The unique identifier of the [payment instrument group](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id) to which the payment instrument belongs. |
| `reference` | `str` | Optional | Your reference for the payment instrument, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `status` | [`Status10`](../../doc/models/status-10.md) | Optional | - |
| `status_comment` | `str` | Optional | The status comment provides additional information for the statusReason of the payment instrument. |
| `status_reason` | [`StatusReason`](../../doc/models/status-reason.md) | Optional | - |
| `mtype` | [`Type11`](../../doc/models/type-11.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_15 import Address15
from adyen.models.authentication import Authentication
from adyen.models.bank_account_model import BankAccountModel
from adyen.models.bulk_address import BulkAddress
from adyen.models.card_configuration import CardConfiguration
from adyen.models.card_info import CardInfo
from adyen.models.delivery_contact import DeliveryContact
from adyen.models.form_factor_1 import FormFactor1
from adyen.models.name_5 import Name5
from adyen.models.payment_instrument_info import PaymentInstrumentInfo
from adyen.models.phone import Phone
from adyen.models.phone_number_3 import PhoneNumber3
from adyen.models.phone_type import PhoneType
from adyen.models.type_11 import Type11
from adyen.models.type_4 import Type4

payment_instrument_info = PaymentInstrumentInfo(
    balance_account_id='balanceAccountId4',
    issuing_country_code='issuingCountryCode6',
    mtype=Type11.BANKACCOUNT,
    bank_account=BankAccountModel(
        form_factor=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
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
    description='description4',
    payment_instrument_group_id='paymentInstrumentGroupId4',
    reference='reference0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

