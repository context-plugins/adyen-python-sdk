
# Merchant Purchase Data

## Structure

`MerchantPurchaseData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `airline` | [`Airline11`](../../doc/models/airline-11.md) | Optional | Airline information. |
| `lodging` | [`List[Lodging1]`](../../doc/models/lodging-1.md) | Optional | Lodging information. |
| `mtype` | `str` | Required, Constant | The type of events data.<br><br>Possible values:<br><br>- **merchantPurchaseData**: merchant purchase data<br><br>**Value**: `"merchantPurchaseData"` |

## Example

```python
from adyen.models.airline_11 import Airline11
from adyen.models.leg_1 import Leg1
from adyen.models.lodging_1 import Lodging1
from adyen.models.merchant_purchase_data import MerchantPurchaseData

merchant_purchase_data = MerchantPurchaseData(
    airline=Airline11(
        legs=[
            Leg1(
                arrival_airport_code='arrivalAirportCode8',
                basic_fare_code='basicFareCode4',
                carrier_code='carrierCode6',
                departure_airport_code='departureAirportCode4',
                departure_date='departureDate8'
            ),
            Leg1(
                arrival_airport_code='arrivalAirportCode8',
                basic_fare_code='basicFareCode4',
                carrier_code='carrierCode6',
                departure_airport_code='departureAirportCode4',
                departure_date='departureDate8'
            ),
            Leg1(
                arrival_airport_code='arrivalAirportCode8',
                basic_fare_code='basicFareCode4',
                carrier_code='carrierCode6',
                departure_airport_code='departureAirportCode4',
                departure_date='departureDate8'
            )
        ],
        ticket_number='ticketNumber4'
    ),
    lodging=[
        Lodging1(
            check_in_date='checkInDate0',
            number_of_nights=50
        ),
        Lodging1(
            check_in_date='checkInDate0',
            number_of_nights=50
        ),
        Lodging1(
            check_in_date='checkInDate0',
            number_of_nights=50
        )
    ]
)
```

