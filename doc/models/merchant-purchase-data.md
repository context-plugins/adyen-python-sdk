
# Merchant Purchase Data

*This model accepts additional fields of type Any.*

## Structure

`MerchantPurchaseData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `airline` | [`Airline2`](../../doc/models/airline-2.md) | Optional | - |
| `lodging` | [`List[Lodging1]`](../../doc/models/lodging-1.md) | Optional | Lodging information. |
| `mtype` | [`Type87`](../../doc/models/type-87.md) | Required | The type of events data.<br><br>Possible values:<br><br>- **merchantPurchaseData**: merchant purchase data |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.airline_2 import Airline2
from adyen.models.leg_1 import Leg1
from adyen.models.lodging_1 import Lodging1
from adyen.models.merchant_purchase_data import MerchantPurchaseData
from adyen.models.type_87 import Type87

merchant_purchase_data = MerchantPurchaseData(
    mtype=Type87.MERCHANTPURCHASEDATA,
    airline=Airline2(
        legs=[
            Leg1(
                arrival_airport_code='arrivalAirportCode8',
                basic_fare_code='basicFareCode4',
                carrier_code='carrierCode6',
                departure_airport_code='departureAirportCode4',
                departure_date='departureDate8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Leg1(
                arrival_airport_code='arrivalAirportCode8',
                basic_fare_code='basicFareCode4',
                carrier_code='carrierCode6',
                departure_airport_code='departureAirportCode4',
                departure_date='departureDate8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            Leg1(
                arrival_airport_code='arrivalAirportCode8',
                basic_fare_code='basicFareCode4',
                carrier_code='carrierCode6',
                departure_airport_code='departureAirportCode4',
                departure_date='departureDate8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        ticket_number='ticketNumber4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    lodging=[
        Lodging1(
            check_in_date='checkInDate0',
            number_of_nights=50,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Lodging1(
            check_in_date='checkInDate0',
            number_of_nights=50,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Lodging1(
            check_in_date='checkInDate0',
            number_of_nights=50,
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

