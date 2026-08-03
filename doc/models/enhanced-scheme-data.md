
# Enhanced Scheme Data

*This model accepts additional fields of type Any.*

## Structure

`EnhancedSchemeData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `airline` | [`Airline`](../../doc/models/airline.md) | Optional | - |
| `car_rental` | [`CarRental`](../../doc/models/car-rental.md) | Optional | - |
| `healthcare` | [`Healthcare`](../../doc/models/healthcare.md) | Optional | - |
| `level_two_three` | [`LevelTwoThree`](../../doc/models/level-two-three.md) | Optional | - |
| `lodging` | [`Lodging`](../../doc/models/lodging.md) | Optional | - |
| `temporary_services` | [`TemporaryServices`](../../doc/models/temporary-services.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.agency import Agency
from adyen.models.airline import Airline
from adyen.models.car_rental import CarRental
from adyen.models.destination import Destination
from adyen.models.enhanced_scheme_data import EnhancedSchemeData
from adyen.models.folio import Folio
from adyen.models.healthcare import Healthcare
from adyen.models.item_detail_line import ItemDetailLine
from adyen.models.level_two_three import LevelTwoThree
from adyen.models.lodging import Lodging
from adyen.models.pickup_info import PickupInfo
from adyen.models.rate_type import RateType

enhanced_scheme_data = EnhancedSchemeData(
    airline=Airline(
        passenger_name='passengerName0',
        agency=Agency(
            invoice_number='invoiceNumber6',
            plan_name='planName6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        boarding_fee=160,
        code='code0',
        computerized_reservation_system='computerizedReservationSystem4',
        customer_reference_number='customerReferenceNumber6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    car_rental=CarRental(
        renter_name='renterName2',
        customer_service_phone_number='customerServicePhoneNumber8',
        no_show=False,
        pickup_info=PickupInfo(
            city='city4',
            country_code='countryCode8',
            date=dateutil.parser.parse('2016-03-13').date(),
            state_or_province='stateOrProvince4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        rate_type=RateType.DAILY,
        rental_agreement_number='rentalAgreementNumber4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    healthcare=Healthcare(
        total_healthcare_value=16,
        dental_value=132,
        other_medical_value=150,
        prescription_value=116,
        vision_prescription_value=166,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    level_two_three=LevelTwoThree(
        customer_reference_number='customerReferenceNumber0',
        destination=Destination(
            country_code='countryCode0',
            postal_code='postalCode6',
            state_or_province='stateOrProvince2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        duty_amount=234,
        freight_amount=136,
        item_detail_lines=[
            ItemDetailLine(
                commodity_code='commodityCode4',
                description='description8',
                discount_amount=220,
                product_code='productCode0',
                quantity=184,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    lodging=Lodging(
        check_in_date=dateutil.parser.parse('2016-03-13').date(),
        check_out_date=dateutil.parser.parse('2016-03-13').date(),
        customer_service_phone_number='customerServicePhoneNumber6',
        fire_safety_compliance=False,
        folio=Folio(
            cash_advances=122,
            number='number8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

