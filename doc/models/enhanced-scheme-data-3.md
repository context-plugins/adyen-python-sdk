
# Enhanced Scheme Data 3

[Enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/) that may be required for processing the payment and/or interchange savings can apply.

## Structure

`EnhancedSchemeData3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `airline` | [`Airline1`](../../doc/models/airline-1.md) | Optional | [Airline enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/airline/) that may be required for processing the transaction and/or for interchange savings. |
| `car_rental` | [`CarRental1`](../../doc/models/car-rental-1.md) | Optional | [Car rental enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/car-rental/) that may be required for processing the transaction and/or for interchange savings. |
| `healthcare` | [`Healthcare2`](../../doc/models/healthcare-2.md) | Optional | Healthcare auto-substantiation amounts for FSA/HSA card transactions. The amounts are used to qualify for reduced interchange rates on healthcare-eligible cards. |
| `level_two_three` | [`LevelTwoThree2`](../../doc/models/level-two-three-2.md) | Optional | [Level 2 and Level 3 enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3/) that may be required for processing the transaction and/or for interchange savings. |
| `lodging` | [`Lodging2`](../../doc/models/lodging-2.md) | Optional | [Lodging enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/lodging/) that may be required for processing the transaction and/or for interchange savings. |
| `temporary_services` | [`TemporaryServices2`](../../doc/models/temporary-services-2.md) | Optional | [Temporary services enhanced scheme data](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/temporary-services/) that may be required for processing the transaction and/or for interchange savings. |

## Example

```python
import dateutil.parser

from adyen.models.agency import Agency
from adyen.models.airline_1 import Airline1
from adyen.models.car_rental_1 import CarRental1
from adyen.models.destination_1 import Destination1
from adyen.models.enhanced_scheme_data_3 import EnhancedSchemeData3
from adyen.models.folio_2 import Folio2
from adyen.models.healthcare_2 import Healthcare2
from adyen.models.item_detail_line import ItemDetailLine
from adyen.models.level_two_three_2 import LevelTwoThree2
from adyen.models.lodging_2 import Lodging2
from adyen.models.pickup_info import PickupInfo
from adyen.models.rate_type_enum import RateTypeEnum

enhanced_scheme_data_3 = EnhancedSchemeData3(
    airline=Airline1(
        passenger_name='passengerName0',
        agency=Agency(
            invoice_number='invoiceNumber6',
            plan_name='planName6'
        ),
        boarding_fee=160,
        code='code0',
        computerized_reservation_system='computerizedReservationSystem4',
        customer_reference_number='customerReferenceNumber6'
    ),
    car_rental=CarRental1(
        renter_name='renterName2',
        customer_service_phone_number='customerServicePhoneNumber8',
        no_show=False,
        pickup_info=PickupInfo(
            city='city4',
            country_code='countryCode8',
            date=dateutil.parser.parse('2016-03-13').date(),
            state_or_province='stateOrProvince4'
        ),
        rate_type=RateTypeEnum.DAILY,
        rental_agreement_number='rentalAgreementNumber4'
    ),
    healthcare=Healthcare2(
        total_healthcare_value=16,
        dental_value=132,
        other_medical_value=150,
        prescription_value=116,
        vision_prescription_value=166
    ),
    level_two_three=LevelTwoThree2(
        customer_reference_number='customerReferenceNumber0',
        destination=Destination1(
            country_code='countryCode0',
            postal_code='postalCode6',
            state_or_province='stateOrProvince2'
        ),
        duty_amount=234,
        freight_amount=136,
        item_detail_lines=[
            ItemDetailLine(
                commodity_code='commodityCode4',
                description='description8',
                discount_amount=220,
                product_code='productCode0',
                quantity=184
            )
        ]
    ),
    lodging=Lodging2(
        check_in_date=dateutil.parser.parse('2016-03-13').date(),
        check_out_date=dateutil.parser.parse('2016-03-13').date(),
        customer_service_phone_number='customerServicePhoneNumber6',
        fire_safety_compliance=False,
        folio=Folio2(
            cash_advances=122,
            number='number8'
        )
    )
)
```

