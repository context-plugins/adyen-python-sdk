
# Card Acquisition Response

It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered by the Customer.
Content of the Card Acquisition Response message.

*This model accepts additional fields of type Any.*

## Structure

`CardAcquisitionResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response` | [`Response3`](../../doc/models/response-3.md) | Required | - |
| `sale_data` | [`SaleData2`](../../doc/models/sale-data-2.md) | Required | - |
| `poi_data` | [`PoiData2`](../../doc/models/poi-data-2.md) | Required | - |
| `payment_brand` | `List[str]` | Optional | Type of payment card.<br>Brands available for payment by the card and not chosen by the Customer.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `payment_instrument_data` | [`PaymentInstrumentData2`](../../doc/models/payment-instrument-data-2.md) | Optional | - |
| `loyalty_account` | [`List[LoyaltyAccount]`](../../doc/models/loyalty-account.md) | Optional | Data related to the loyalty System. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.card_acquisition_response import CardAcquisitionResponse
from adyen.models.card_data_2 import CardData2
from adyen.models.check_data_2 import CheckData2
from adyen.models.entry_mode import EntryMode
from adyen.models.error_condition_1 import ErrorCondition1
from adyen.models.geographic_coordinates import GeographicCoordinates
from adyen.models.geolocation import Geolocation
from adyen.models.identification_support_1 import IdentificationSupport1
from adyen.models.identification_type_11 import IdentificationType11
from adyen.models.loyalty_account import LoyaltyAccount
from adyen.models.loyalty_account_id_3 import LoyaltyAccountId3
from adyen.models.mobile_data_2 import MobileData2
from adyen.models.payment_instrument_data_2 import PaymentInstrumentData2
from adyen.models.payment_instrument_type_11 import PaymentInstrumentType11
from adyen.models.poi_data_2 import PoiData2
from adyen.models.poi_transaction_id import PoiTransactionId
from adyen.models.response_3 import Response3
from adyen.models.result_11 import Result11
from adyen.models.sale_data_2 import SaleData2
from adyen.models.sale_terminal_data_3 import SaleTerminalData3
from adyen.models.sale_transaction_id import SaleTransactionId
from adyen.models.stored_value_account_id_2 import StoredValueAccountId2
from adyen.models.stored_value_account_type_1 import StoredValueAccountType1
from adyen.models.track_data_2 import TrackData2
from adyen.models.track_format_1 import TrackFormat1
from adyen.models.utm_coordinates import UtmCoordinates

card_acquisition_response = CardAcquisitionResponse(
    response=Response3(
        result=Result11.PARTIAL,
        error_condition=ErrorCondition1.PAYMENTRESTRICTION,
        additional_response='AdditionalResponse8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    sale_data=SaleData2(
        sale_transaction_id=SaleTransactionId(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        operator_id='OperatorID8',
        operator_language='OperatorLanguage2',
        shift_number='ShiftNumber0',
        sale_reference_id='SaleReferenceID8',
        sale_terminal_data=SaleTerminalData3(
            totals_group_id='TotalsGroupID4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    poi_data=PoiData2(
        poi_transaction_id=PoiTransactionId(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        poi_reconciliation_id=52,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_brand=[
        'PaymentBrand9',
        'PaymentBrand0'
    ],
    payment_instrument_data=PaymentInstrumentData2(
        payment_instrument_type=PaymentInstrumentType11.CASH,
        protected_card_data='ProtectedCardData8',
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
    ),
    loyalty_account=[
        LoyaltyAccount(
            loyalty_account_id=LoyaltyAccountId3(
                entry_mode=[
                    EntryMode.FILE
                ],
                identification_type=IdentificationType11.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1.HYBRIDCARD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            loyalty_brand='LoyaltyBrand0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LoyaltyAccount(
            loyalty_account_id=LoyaltyAccountId3(
                entry_mode=[
                    EntryMode.FILE
                ],
                identification_type=IdentificationType11.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1.HYBRIDCARD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            loyalty_brand='LoyaltyBrand0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        LoyaltyAccount(
            loyalty_account_id=LoyaltyAccountId3(
                entry_mode=[
                    EntryMode.FILE
                ],
                identification_type=IdentificationType11.ISOTRACK2,
                loyalty_id='LoyaltyID4',
                identification_support=IdentificationSupport1.HYBRIDCARD,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            loyalty_brand='LoyaltyBrand0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

