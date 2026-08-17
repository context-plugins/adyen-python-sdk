
# Payment Account Status 2

Data related to the result of a Balance Inquiry request.
If BalanceInquiryRequest. PaymentAccount present.

## Structure

`PaymentAccountStatus2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_data` | [`PaymentInstrumentData`](../../doc/models/payment-instrument-data.md) | Optional | Data related to the instrument of payment for the transaction.<br>Sent in the result of the payment transaction. For a card, it could also be sent in the `CardAcquisition` response, to be processed by the Sale System. |
| `current_balance` | `float` | Optional | Balance of an account after processing of the transaction.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `currency` | `str` | Optional | Currency of a monetary amount.<br><br>**Constraints**: *Pattern*: `^[A-Z]{3,3}$` |
| `payment_acquirer_data` | [`PaymentAcquirerData`](../../doc/models/payment-acquirer-data.md) | Optional | Data related to the response from the payment Acquirer. |

## Example

```python
import dateutil.parser

from adyen.models.card_data_1 import CardData1
from adyen.models.check_data_1 import CheckData1
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.payment_account_status_2 import PaymentAccountStatus2
from adyen.models.payment_acquirer_data import PaymentAcquirerData
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type_6 import TransactionIDType6
from adyen.models.utm_coordinates import UTMCoordinates

payment_account_status_2 = PaymentAccountStatus2(
    payment_instrument_data=PaymentInstrumentData(
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
    ),
    current_balance=222.22,
    currency='Currency6',
    payment_acquirer_data=PaymentAcquirerData(
        merchant_id='MerchantID6',
        acquirer_poiid='AcquirerPOIID4',
        acquirer_id=238,
        acquirer_transaction_id=TransactionIDType6(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        approval_code='ApprovalCode8',
        host_reconciliation_id='HostReconciliationID8'
    )
)
```

