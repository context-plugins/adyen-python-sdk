
# Balance Inquiry Request 2

Content of the Balance Inquiry Request message.

## Structure

`BalanceInquiryRequest2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_account_req` | [`PaymentAccountReq2`](../../doc/models/payment-account-req-2.md) | Optional | Data related to the account pointed by the payment card. |
| `loyalty_account_req` | [`LoyaltyAccountReq2`](../../doc/models/loyalty-account-req-2.md) | Optional | Data related to a requested Loyalty program or account. |

## Example

```python
import dateutil.parser

from adyen.models.account_type_12_enum import AccountType12Enum
from adyen.models.balance_inquiry_request_2 import BalanceInquiryRequest2
from adyen.models.card_data_1 import CardData1
from adyen.models.check_data_1 import CheckData1
from adyen.models.entry_mode_enum import EntryModeEnum
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation_1 import Geolocation1
from adyen.models.identification_support_1_enum import IdentificationSupport1Enum
from adyen.models.identification_type_11_enum import IdentificationType11Enum
from adyen.models.loyalty_account_id import LoyaltyAccountID
from adyen.models.loyalty_account_req_2 import LoyaltyAccountReq2
from adyen.models.mobile_data_1 import MobileData1
from adyen.models.payment_account_req_2 import PaymentAccountReq2
from adyen.models.payment_instrument_data import PaymentInstrumentData
from adyen.models.payment_instrument_type_11_enum import PaymentInstrumentType11Enum
from adyen.models.stored_value_account_id import StoredValueAccountID
from adyen.models.stored_value_account_type_1_enum import StoredValueAccountType1Enum
from adyen.models.track_data_1 import TrackData1
from adyen.models.track_format_1_enum import TrackFormat1Enum
from adyen.models.transaction_id_type import TransactionIDType
from adyen.models.utm_coordinates import UTMCoordinates

balance_inquiry_request_2 = BalanceInquiryRequest2(
    payment_account_req=PaymentAccountReq2(
        account_type=AccountType12Enum.CHECKING,
        card_acquisition_reference=TransactionIDType(
            transaction_id='TransactionID8',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
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
        )
    ),
    loyalty_account_req=LoyaltyAccountReq2(
        card_acquisition_reference=TransactionIDType(
            transaction_id='TransactionID8',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        ),
        loyalty_account_id=LoyaltyAccountID(
            entry_mode=[
                EntryModeEnum.FILE
            ],
            identification_type=IdentificationType11Enum.ISOTRACK2,
            loyalty_id='LoyaltyID4',
            identification_support=IdentificationSupport1Enum.HYBRIDCARD
        )
    )
)
```

