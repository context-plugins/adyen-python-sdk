
# Payment Instrument Data

Data related to the instrument of payment for the transaction.
Sent in the result of the payment transaction. For a card, it could also be sent in the `CardAcquisition` response, to be processed by the Sale System.

*This model accepts additional fields of type Any.*

## Structure

`PaymentInstrumentData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_type` | [`PaymentInstrumentType11`](../../doc/models/payment-instrument-type-11.md) | Required | - |
| `protected_card_data` | `str` | Optional | Sensitive information related to the payment card, protected by CMS.<br>SensitiveCardData protected by CMS EnvelopedData. |
| `card_data` | [`CardData2`](../../doc/models/card-data-2.md) | Optional | - |
| `check_data` | [`CheckData2`](../../doc/models/check-data-2.md) | Optional | - |
| `mobile_data` | [`MobileData2`](../../doc/models/mobile-data-2.md) | Optional | - |
| `stored_value_account_id` | [`StoredValueAccountId2`](../../doc/models/stored-value-account-id-2.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.card_data_2 import CardData2
from adyen.models.check_data_2 import CheckData2
from adyen.models.entry_mode import EntryMode
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.utm_coordinates import UtmCoordinates

payment_instrument_data = PaymentInstrumentData(
    payment_instrument_type=PaymentInstrumentType11.MOBILE,
    protected_card_data='ProtectedCardData0',
    card_data=CardData2(
        payment_brand='PaymentBrand0',
        masked_pan='MaskedPan0',
        payment_account_ref='PaymentAccountRef8',
        entry_mode=[
            EntryMode.MANUAL,
            EntryMode.KEYED
        ],
        card_country_code=3,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    check_data=CheckData2(
        bank_id='BankID0',
        account_number='AccountNumber6',
        check_number='CheckNumber2',
        track_data=TrackData2(
            track_value='TrackValue6',
            track_numb=3,
            track_format=TrackFormat1.JISII,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        check_card_number='CheckCardNumber6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    mobile_data=MobileData2(
        mobile_country_code=3,
        mobile_network_code=3,
        masked_msisdn=22,
        geolocation=Geolocation(
            geographic_coordinates=GeographicCoordinates(
                latitude='Latitude4',
                longitude='Longitude2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            utm_coordinates=UtmCoordinates(
                utm_zone='UTMZone6',
                utm_eastward='UTMEastward0',
                utm_northward='UTMNorthward0',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        protected_mobile_data='ProtectedMobileData0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    stored_value_account_id=StoredValueAccountId2(
        stored_value_account_type=StoredValueAccountType1.PHONECARD,
        entry_mode=[
            EntryMode.MAGSTRIPE,
            EntryMode.SCANNED
        ],
        identification_type=IdentificationType11.PHONENUMBER,
        stored_value_id='StoredValueID8',
        stored_value_provider='StoredValueProvider4',
        owner_name='OwnerName0',
        expiry_date=4,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

