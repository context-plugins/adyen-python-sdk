
# Payment Capture Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentCaptureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to capture. |
| `platform_chargeback_logic` | [`PlatformChargebackLogic1`](../../doc/models/platform-chargeback-logic-1.md) | Optional | - |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the capture request. |
| `reference` | `str` | Optional | Your reference for the capture request. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
| `status` | [`Status20`](../../doc/models/status-20.md) | Required | The status of your request. This will always have the value **received**. |
| `sub_merchants` | [`List[SubMerchantInfo]`](../../doc/models/sub-merchant-info.md) | Optional | List of sub-merchants. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.amount_31 import Amount31
from adyen.models.behavior import Behavior
from adyen.models.billing_address import BillingAddress
from adyen.models.line_item import LineItem
from adyen.models.payment_capture_response import PaymentCaptureResponse
from adyen.models.platform_chargeback_logic_1 import PlatformChargebackLogic1
from adyen.models.split import Split
from adyen.models.status_20 import Status20
from adyen.models.sub_merchant_info import SubMerchantInfo
from adyen.models.type_111 import Type111

payment_capture_response = PaymentCaptureResponse(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount4',
    payment_psp_reference='paymentPspReference0',
    psp_reference='pspReference4',
    status=Status20.RECEIVED,
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
        ),
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
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
    reference='reference2',
    splits=[
        Split(
            mtype=Type111.DEFAULT,
            account='account2',
            amount=Amount31(
                value=110,
                currency='currency2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description2',
            reference='reference2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Split(
            mtype=Type111.DEFAULT,
            account='account2',
            amount=Amount31(
                value=110,
                currency='currency2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description2',
            reference='reference2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        Split(
            mtype=Type111.DEFAULT,
            account='account2',
            amount=Amount31(
                value=110,
                currency='currency2',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            description='description2',
            reference='reference2',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    sub_merchants=[
        SubMerchantInfo(
            address=BillingAddress(
                city='city6',
                country='country0',
                house_number_or_name='houseNumberOrName4',
                postal_code='postalCode8',
                street='street6',
                state_or_province='stateOrProvince4',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            amount=Amount16(
                currency='currency2',
                value=110,
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            email='email6',
            id='id0',
            mcc='mcc0',
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

