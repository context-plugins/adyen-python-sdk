
# Payment Instrument Data 1

Data related to the instrument of payment for the transaction.
If this type of payment card is configured to send information if the CardAcquisition response.

## Structure

`PaymentInstrumentData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_type` | [`PaymentInstrumentType11Enum`](../../doc/models/payment-instrument-type-11-enum.md) | Required | Type of payment instrument.<br>Possible values:<br><br>* **Card**<br>* **Cash**<br>* **Check**<br>* **Mobile**<br>* **StoredValue** |
| `protected_card_data` | `str` | Optional | Sensitive information related to the payment card, protected by CMS.<br>SensitiveCardData protected by CMS EnvelopedData. |
| `card_data` | [`CardData1`](../../doc/models/card-data-1.md) | Optional | Information related to the payment card used for the transaction.<br>If PaymentInstrumentType is Card. |
| `check_data` | [`CheckData1`](../../doc/models/check-data-1.md) | Optional | Information related to the paper check used for the transaction.<br>If PaymentInstrumentType is Check. |
| `mobile_data` | [`MobileData1`](../../doc/models/mobile-data-1.md) | Optional | Information related to the mobile for the payment transaction.<br>If PaymentInstrumentType is Mobile. |
| `stored_value_account_id` | [`StoredValueAccountID`](../../doc/models/stored-value-account-id.md) | Optional | Identification of the stored value account or the stored value card and the associated product sold by the Sale System for stored value requests. |

## Example

```python
from adyen.models.card_data_1 import CardData1
from adyen.models.check_data_1 import CheckData1
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.payment_instrument_data_1 import PaymentInstrumentData1
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.utm_coordinates import UTMCoordinates

payment_instrument_data_1 = PaymentInstrumentData1(
    payment_instrument_type=PaymentInstrumentType11Enum.CASH,
    protected_card_data='ProtectedCardData8',
    card_data=CardData1(
        payment_brand='PaymentBrand0',
        masked_pan='MaskedPan0',
        payment_account_ref='PaymentAccountRef8',
        entry_mode=[
            EntryModeEnum.MANUAL,
            EntryModeEnum.KEYED
        ],
        card_country_code=3
    ),
    check_data=CheckData1(
        bank_id='BankID0',
        account_number='AccountNumber6',
        check_number='CheckNumber2',
        track_data=TrackData1(
            track_value='TrackValue6',
            track_numb=3,
            track_format=TrackFormat1Enum.JISII
        ),
        check_card_number='CheckCardNumber6'
    ),
    mobile_data=MobileData1(
        mobile_country_code=3,
        mobile_network_code=3,
        masked_msisdn=22,
        geolocation=Geolocation1(
            geographic_coordinates=GeographicCoordinates(
                latitude='Latitude4',
                longitude='Longitude2'
            ),
            utm_coordinates=UTMCoordinates(
                utm_zone='UTMZone6',
                utm_eastward='UTMEastward0',
                utm_northward='UTMNorthward0'
            )
        ),
        protected_mobile_data='ProtectedMobileData0'
    ),
    stored_value_account_id=StoredValueAccountID(
        stored_value_account_type=StoredValueAccountType1Enum.PHONECARD,
        entry_mode=[
            EntryModeEnum.MAGSTRIPE,
            EntryModeEnum.SCANNED
        ],
        identification_type=IdentificationType11Enum.PHONENUMBER,
        stored_value_id='StoredValueID8',
        stored_value_provider='StoredValueProvider4',
        owner_name='OwnerName0',
        expiry_date=4
    )
)
```

