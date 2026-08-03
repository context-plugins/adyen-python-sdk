
# Payment Capture Request

*This model accepts additional fields of type Any.*

## Structure

`PaymentCaptureRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `application_info` | [`ApplicationInfo1`](../../doc/models/application-info-1.md) | Optional | - |
| `enhanced_scheme_data` | [`EnhancedSchemeData`](../../doc/models/enhanced-scheme-data.md) | Optional | - |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `platform_chargeback_logic` | [`PlatformChargebackLogic1`](../../doc/models/platform-chargeback-logic-1.md) | Optional | - |
| `reference` | `str` | Optional | Your reference for the capture request. Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
| `sub_merchants` | [`List[SubMerchantInfo]`](../../doc/models/sub-merchant-info.md) | Optional | A List of sub-merchants. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.adyen_library import AdyenLibrary
from adyen.models.adyen_payment_source import AdyenPaymentSource
from adyen.models.agency import Agency
from adyen.models.airline import Airline
from adyen.models.amount_16 import Amount16
from adyen.models.application_info_1 import ApplicationInfo1
from adyen.models.behavior import Behavior
from adyen.models.car_rental import CarRental
from adyen.models.destination import Destination
from adyen.models.enhanced_scheme_data import EnhancedSchemeData
from adyen.models.external_platform_2 import ExternalPlatform2
from adyen.models.folio import Folio
from adyen.models.healthcare import Healthcare
from adyen.models.item_detail_line import ItemDetailLine
from adyen.models.level_two_three import LevelTwoThree
from adyen.models.line_item import LineItem
from adyen.models.lodging import Lodging
from adyen.models.merchant_application import MerchantApplication
from adyen.models.merchant_device_2 import MerchantDevice2
from adyen.models.payment_capture_request import PaymentCaptureRequest
from adyen.models.pickup_info import PickupInfo
from adyen.models.platform_chargeback_logic_1 import PlatformChargebackLogic1
from adyen.models.rate_type import RateType

payment_capture_request = PaymentCaptureRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount4',
    application_info=ApplicationInfo1(
        adyen_library=AdyenLibrary(
            name='name8',
            version='version4',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        adyen_payment_source=AdyenPaymentSource(
            name='name2',
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        external_platform=ExternalPlatform2(
            integrator='integrator0',
            name='name4',
            version='version0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        merchant_application=MerchantApplication(
            name='name2',
            version='version8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        merchant_device=MerchantDevice2(
            os='os4',
            os_version='osVersion6',
            reference='reference8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    enhanced_scheme_data=EnhancedSchemeData(
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
    ),
    line_items=[
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    platform_chargeback_logic=PlatformChargebackLogic1(
        behavior=Behavior.DEDUCTFROMONEBALANCEACCOUNT,
        cost_allocation_account='costAllocationAccount8',
        target_account='targetAccount6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

