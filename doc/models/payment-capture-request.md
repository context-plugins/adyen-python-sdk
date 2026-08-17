
# Payment Capture Request

## Structure

`PaymentCaptureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount31`](../../doc/models/amount-31.md) | Required | The amount that you want to capture. The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount. |
| `application_info` | [`ApplicationInfo`](../../doc/models/application-info.md) | Optional | Information about your application. For more details, see [Building Adyen solutions](https://docs.adyen.com/development-resources/building-adyen-solutions). |
| `enhanced_scheme_data` | [`EnhancedSchemeData1`](../../doc/models/enhanced-scheme-data-1.md) | Optional | Enhanced scheme data that may be required for processing the payment. For example, airline information. |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `reference` | `str` | Optional | Your reference for the capture request. Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
| `sub_merchants` | [`List[SubMerchantInfo]`](../../doc/models/sub-merchant-info.md) | Optional | A List of sub-merchants. |

## Example

```python
import dateutil.parser

from adyen.models.agency import Agency
from adyen.models.airline_1 import Airline1
from adyen.models.amount_31 import Amount31
from adyen.models.application_info import ApplicationInfo
from adyen.models.behavior_enum import BehaviorEnum
from adyen.models.car_rental_1 import CarRental1
from adyen.models.common_field_1 import CommonField1
from adyen.models.common_field_2 import CommonField2
from adyen.models.common_field_4 import CommonField4
from adyen.models.destination_1 import Destination1
from adyen.models.enhanced_scheme_data_1 import EnhancedSchemeData1
from adyen.models.external_platform import ExternalPlatform
from adyen.models.folio_2 import Folio2
from adyen.models.healthcare_2 import Healthcare2
from adyen.models.item_detail_line import ItemDetailLine
from adyen.models.level_two_three_2 import LevelTwoThree2
from adyen.models.line_item import LineItem
from adyen.models.lodging_2 import Lodging2
from adyen.models.merchant_device import MerchantDevice
from adyen.models.payment_capture_request import PaymentCaptureRequest
from adyen.models.pickup_info import PickupInfo
from adyen.models.platform_chargeback_logic import PlatformChargebackLogic
from adyen.models.rate_type_enum import RateTypeEnum

payment_capture_request = PaymentCaptureRequest(
    amount=Amount31(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount4',
    application_info=ApplicationInfo(
        adyen_library=CommonField4(
            name='name8',
            version='version4'
        ),
        adyen_payment_source=CommonField1(
            name='name2',
            version='version8'
        ),
        external_platform=ExternalPlatform(
            integrator='integrator0',
            name='name4',
            version='version0'
        ),
        merchant_application=CommonField2(
            name='name2',
            version='version8'
        ),
        merchant_device=MerchantDevice(
            os='os4',
            os_version='osVersion6',
            reference='reference8'
        )
    ),
    enhanced_scheme_data=EnhancedSchemeData1(
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
    ),
    line_items=[
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2'
        )
    ],
    platform_chargeback_logic=PlatformChargebackLogic(
        behavior=BehaviorEnum.DEDUCTFROMONEBALANCEACCOUNT,
        cost_allocation_account='costAllocationAccount8',
        target_account='targetAccount6'
    ),
    reference='reference8'
)
```

