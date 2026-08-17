
# Paginated Payment Instruments Response

## Structure

`PaginatedPaymentInstrumentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_next` | `bool` | Required | Indicates whether there are more items on the next page. |
| `has_previous` | `bool` | Required | Indicates whether there are more items on the previous page. |
| `payment_instruments` | [`List[PaymentInstrument1]`](../../doc/models/payment-instrument-1.md) | Required | List of payment instruments associated with the balance account. |

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
from adyen.models.paginated_payment_instruments_response import PaginatedPaymentInstrumentsResponse
from adyen.models.payment_instrument_1 import PaymentInstrument1
from adyen.models.phone_11 import Phone11
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.store_location import StoreLocation
from adyen.models.type_111_enum import Type111Enum
from adyen.models.type_410_enum import Type410Enum
from adyen.models.vias_phone_number import ViasPhoneNumber

paginated_payment_instruments_response = PaginatedPaymentInstrumentsResponse(
    has_next=False,
    has_previous=False,
    payment_instruments=[
        PaymentInstrument1(
            balance_account_id='balanceAccountId0',
            id='id8',
            issuing_country_code='issuingCountryCode0',
            mtype=Type111Enum.BANKACCOUNT,
            additional_bank_account_identifications=[
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
            description='description2',
            payment_instrument_group_id='paymentInstrumentGroupId2'
        )
    ]
)
```

