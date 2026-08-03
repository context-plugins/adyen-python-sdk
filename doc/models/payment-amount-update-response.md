
# Payment Amount Update Response

*This model accepts additional fields of type Any.*

## Structure

`PaymentAmountUpdateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjust_authorisation_data` | `str` | Optional | The data blob for subsequent synchronous adjust authorisation calls. Returned when the synchronous flow is used. |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `industry_usage` | [`IndustryUsage1`](../../doc/models/industry-usage-1.md) | Optional | - |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to update. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the amount update request. |
| `reference` | `str` | Required | Your reference for the amount update request. Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/process-payments) or [platforms](https://docs.adyen.com/platforms/process-payments). |
| `status` | [`Status23`](../../doc/models/status-23.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.amount_31 import Amount31
from adyen.models.industry_usage_1 import IndustryUsage1
from adyen.models.line_item import LineItem
from adyen.models.payment_amount_update_response import PaymentAmountUpdateResponse
from adyen.models.split import Split
from adyen.models.status_23 import Status23
from adyen.models.type_111 import Type111

payment_amount_update_response = PaymentAmountUpdateResponse(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    merchant_account='merchantAccount8',
    payment_psp_reference='paymentPspReference2',
    psp_reference='pspReference8',
    reference='reference4',
    status=Status23.REFUSED,
    adjust_authorisation_data='adjustAuthorisationData8',
    industry_usage=IndustryUsage1.NOSHOW,
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
        )
    ],
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

