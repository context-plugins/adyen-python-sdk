
# Payment Instrument 1

## Structure

`PaymentInstrument1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_bank_account_identifications` | List[[IbanAccountIdentification](../../doc/models/iban-account-identification.md)] \| None | Optional | This is List of a container for one-of cases. |
| `balance_account_id` | `str` | Required | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/balanceAccounts__resParam_id) associated with the payment instrument. |
| `bank_account` | [`BankAccountDetails1`](../../doc/models/bank-account-details-1.md) | Optional | Contains the business account details. Returned when you create a payment instrument with `type` **bankAccount**. |
| `card` | [`Card11`](../../doc/models/card-11.md) | Optional | Contains information about the card payment instrument. Returned when you create a payment instrument with `type` **card**. |
| `description` | `str` | Optional | Your description for the payment instrument, maximum 300 characters.<br><br>**Constraints**: *Maximum Length*: `300` |
| `id` | `str` | Required | The unique identifier of the payment instrument. |
| `issuing_country_code` | `str` | Required | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**. |
| `payment_instrument_group_id` | `str` | Optional | The unique identifier of the [payment instrument group](https://docs.adyen.com/api-explorer/#/balanceplatform/v1/post/paymentInstrumentGroups__resParam_id) to which the payment instrument belongs. |
| `reference` | `str` | Optional | Your reference for the payment instrument, maximum 150 characters.<br><br>**Constraints**: *Maximum Length*: `150` |
| `replaced_by_id` | `str` | Optional | The unique identifier of the payment instrument that replaced this payment instrument. |
| `replacement_of_id` | `str` | Optional | The unique identifier of the payment instrument that is replaced by this payment instrument. |
| `status` | [`Status10Enum`](../../doc/models/status-10-enum.md) | Optional | The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **active** by default. However, there can be exceptions for cards based on the `card.formFactor` and the `issuingCountryCode`. For example, when issuing physical cards in the US, the default status is **inactive**.<br><br>Possible values:<br><br>* **active**:  The payment instrument is active and can be used to make payments.<br><br>* **inactive**: The payment instrument is inactive and cannot be used to make payments.<br><br>* **suspended**: The payment instrument is suspended, either because it was stolen or lost.<br><br>* **closed**: The payment instrument is permanently closed. This action cannot be undone. |
| `status_comment` | `str` | Optional | The status comment provides additional information for the statusReason of the payment instrument. |
| `status_reason` | [`StatusReasonEnum`](../../doc/models/status-reason-enum.md) | Optional | The reason for the status of the payment instrument.<br><br>Possible values: **accountClosure**, **damaged**, **endOfLife**, **expired**, **lost**, **stolen**, **suspectedFraud**, **transactionRule**, **other**.<br>If the reason is **other**, you must also send the `statusComment` parameter describing the status change. |
| `mtype` | [`Type111Enum`](../../doc/models/type-111-enum.md) | Required | The type of payment instrument.<br><br>Possible values: **card**, **bankAccount**. |

## Example

```python
from adyen.models.authentication_1 import Authentication1
from adyen.models.bank_account_details_1 import BankAccountDetails1
from adyen.models.bulk_address_1 import BulkAddress1
from adyen.models.card_11 import Card11
from adyen.models.card_configuration_2 import CardConfiguration2
from adyen.models.delivery_contact_1 import DeliveryContact1
from adyen.models.form_factor_1_enum import FormFactor1Enum
from adyen.models.iban_account_identification import IbanAccountIdentification
from adyen.models.name import Name
from adyen.models.payment_instrument_1 import PaymentInstrument1
from adyen.models.phone_11 import Phone11
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.store_location import StoreLocation
from adyen.models.type_111_enum import Type111Enum
from adyen.models.type_410_enum import Type410Enum
from adyen.models.vias_phone_number import ViasPhoneNumber

payment_instrument_1 = PaymentInstrument1(
    balance_account_id='balanceAccountId4',
    id='id4',
    issuing_country_code='issuingCountryCode6',
    mtype=Type111Enum.BANKACCOUNT,
    additional_bank_account_identifications=[
        IbanAccountIdentification(
            iban='iban6',
            bic='bic4'
        ),
        IbanAccountIdentification(
            iban='iban6',
            bic='bic4'
        ),
        IbanAccountIdentification(
            iban='iban6',
            bic='bic4'
        )
    ],
    bank_account=BankAccountDetails1(
        mtype='type2',
        account_number='accountNumber4',
        account_type='accountType8',
        branch_number='branchNumber8',
        form_factor='formFactor2',
        iban='iban2'
    ),
    card=Card11(
        brand='brand0',
        brand_variant='brandVariant8',
        cardholder_name='cardholderName8',
        form_factor=FormFactor1Enum.PHYSICAL,
        authentication=Authentication1(
            email='email8',
            password='password2',
            phone=Phone11(
                number='number8',
                mtype=Type410Enum.LANDLINE
            )
        ),
        bin='bin6',
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
        cvc='cvc0',
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
        )
    ),
    description='description4',
    payment_instrument_group_id='paymentInstrumentGroupId4'
)
```

