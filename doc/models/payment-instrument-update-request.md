
# Payment Instrument Update Request

## Structure

`PaymentInstrumentUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | The unique identifier of the balance account associated with this payment instrument.<br><br>> You can only change the balance account ID if the payment instrument has **inactive** status. |
| `card` | [`CardInfo2`](../../doc/models/card-info-2.md) | Optional | Object that contains information about the card payment instrument. |
| `status` | [`Status10Enum`](../../doc/models/status-10-enum.md) | Optional | The status of the payment instrument. If a status is not specified when creating a payment instrument, it is set to **active** by default. However, there can be exceptions for cards based on the `card.formFactor` and the `issuingCountryCode`. For example, when issuing physical cards in the US, the default status is **inactive**.<br><br>Possible values:<br><br>* **active**:  The payment instrument is active and can be used to make payments.<br><br>* **inactive**: The payment instrument is inactive and cannot be used to make payments.<br><br>* **suspended**: The payment instrument is suspended, either because it was stolen or lost.<br><br>* **closed**: The payment instrument is permanently closed. This action cannot be undone. |
| `status_comment` | `str` | Optional | Comment for the status of the payment instrument.<br><br>Required if `statusReason` is **other**. |
| `status_reason` | [`StatusReason2Enum`](../../doc/models/status-reason-2-enum.md) | Optional | The reason for updating the status of the payment instrument.<br><br>Possible values: **lost**, **stolen**, **damaged**, **suspectedFraud**, **expired**, **endOfLife**, **accountClosure**, **other**.<br>If the reason is **other**, you must also send the `statusComment` parameter describing the status change. |

## Example

```python
from adyen.models.authentication_1 import Authentication1
from adyen.models.bulk_address_1 import BulkAddress1
from adyen.models.card_configuration_2 import CardConfiguration2
from adyen.models.card_info_2 import CardInfo2
from adyen.models.delivery_contact_1 import DeliveryContact1
from adyen.models.form_factor_1_enum import FormFactor1Enum
from adyen.models.name import Name
from adyen.models.payment_instrument_update_request import PaymentInstrumentUpdateRequest
from adyen.models.phone_11 import Phone11
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.status_10_enum import Status10Enum
from adyen.models.status_reason_2_enum import StatusReason2Enum
from adyen.models.store_location import StoreLocation
from adyen.models.type_410_enum import Type410Enum
from adyen.models.vias_phone_number import ViasPhoneNumber

payment_instrument_update_request = PaymentInstrumentUpdateRequest(
    balance_account_id='balanceAccountId0',
    card=CardInfo2(
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
        three_d_secure='threeDSecure8',
        usage='usage4'
    ),
    status=Status10Enum.ACTIVE,
    status_comment='statusComment8',
    status_reason=StatusReason2Enum.SUSPECTEDFRAUD
)
```

