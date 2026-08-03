
# Update Payment Instrument

*This model accepts additional fields of type Any.*

## Structure

`UpdatePaymentInstrument`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_bank_account_identifications` | [`List[IbanAccountIdentification1]`](../../doc/models/iban-account-identification-1.md) | Optional | Contains optional, additional business account details. Returned when you create a payment instrument with `type` **bankAccount**. |
| `balance_account_id` | `str` | Required | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id) associated with the payment instrument. |
| `bank_account` | [`BankAccountDetails`](../../doc/models/bank-account-details.md) | Optional | - |
| `card` | [`Card`](../../doc/models/card.md) | Optional | - |
| `description` | `str` | Optional | Your description for the payment instrument, maximum 300 characters.<br><br>**Constraints**: *Maximum Length*: `300` |
| `id` | `str` | Required | The unique identifier of the payment instrument. |
| `issuing_country_code` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**. |
| `payment_instrument_group_id` | `str` | Optional | The unique identifier of the [payment instrument group](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id) to which the payment instrument belongs. |
| `reference` | `str` | Optional | Your reference for the payment instrument, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `replaced_by_id` | `str` | Optional | The unique identifier of the payment instrument that replaced this payment instrument. |
| `replacement_of_id` | `str` | Optional | The unique identifier of the payment instrument that is replaced by this payment instrument. |
| `status` | [`Status10`](../../doc/models/status-10.md) | Optional | - |
| `status_comment` | `str` | Optional | Comment for the status of the payment instrument.<br><br>Required if `statusReason` is **other**. |
| `status_reason` | [`StatusReason`](../../doc/models/status-reason.md) | Optional | - |
| `mtype` | [`Type11`](../../doc/models/type-11.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_15 import Address15
from adyen.models.authentication import Authentication
from adyen.models.bank_account_details import BankAccountDetails
from adyen.models.bulk_address import BulkAddress
from adyen.models.card import Card
from adyen.models.card_configuration import CardConfiguration
from adyen.models.delivery_contact import DeliveryContact
from adyen.models.form_factor_1 import FormFactor1
from adyen.models.iban_account_identification_1 import IbanAccountIdentification1
from adyen.models.name_5 import Name5
from adyen.models.phone import Phone
from adyen.models.phone_number_3 import PhoneNumber3
from adyen.models.phone_type import PhoneType
from adyen.models.type_11 import Type11
from adyen.models.type_203 import Type203
from adyen.models.type_4 import Type4
from adyen.models.update_payment_instrument import UpdatePaymentInstrument

update_payment_instrument = UpdatePaymentInstrument(
    balance_account_id='balanceAccountId4',
    id='id2',
    issuing_country_code='issuingCountryCode4',
    mtype=Type11.BANKACCOUNT,
    additional_bank_account_identifications=[
        IbanAccountIdentification1(
            iban='iban8',
            mtype=Type203.IBAN,
            bic='bic6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        IbanAccountIdentification1(
            iban='iban8',
            mtype=Type203.IBAN,
            bic='bic6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    bank_account=BankAccountDetails(
        mtype='type2',
        account_number='accountNumber4',
        account_type='accountType8',
        branch_number='branchNumber8',
        form_factor='formFactor2',
        iban='iban2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    card=Card(
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
        bin='bin6',
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
        cvc='cvc0',
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
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    description='description2',
    payment_instrument_group_id='paymentInstrumentGroupId2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

