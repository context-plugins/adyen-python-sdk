
# Payment Capture Response

## Structure

`PaymentCaptureResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount33`](../../doc/models/amount-33.md) | Required | The captured amount. |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to capture. |
| `platform_chargeback_logic` | [`PlatformChargebackLogic`](../../doc/models/platform-chargeback-logic.md) | Optional | Defines how to book chargebacks when using [Adyen for Platforms](https://docs.adyen.com/adyen-for-platforms-model). |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the capture request. |
| `reference` | `str` | Optional | Your reference for the capture request. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
| `status` | `str` | Required, Constant | The status of your request. This will always have the value **received**.<br><br>**Value**: `"received"` |
| `sub_merchants` | [`List[SubMerchantInfo]`](../../doc/models/sub-merchant-info.md) | Optional | List of sub-merchants. |

## Example

```python
from adyen.models.amount_32 import Amount32
from adyen.models.amount_33 import Amount33
from adyen.models.behavior_enum import BehaviorEnum
from adyen.models.billing_address_4 import BillingAddress4
from adyen.models.line_item import LineItem
from adyen.models.payment_capture_response import PaymentCaptureResponse
from adyen.models.platform_chargeback_logic import PlatformChargebackLogic
from adyen.models.split import Split
from adyen.models.split_amount import SplitAmount
from adyen.models.sub_merchant_info import SubMerchantInfo
from adyen.models.type_11_enum import Type11Enum

payment_capture_response = PaymentCaptureResponse(
    amount=Amount33(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount4',
    payment_psp_reference='paymentPspReference0',
    psp_reference='pspReference4',
    line_items=[
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2'
        ),
        LineItem(
            amount_excluding_tax=38,
            amount_including_tax=148,
            brand='brand6',
            color='color6',
            description='description2'
        ),
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
    reference='reference2',
    splits=[
        Split(
            mtype=Type11Enum.DEFAULT,
            account='account2',
            amount=SplitAmount(
                value=110,
                currency='currency2'
            ),
            description='description2',
            reference='reference2'
        ),
        Split(
            mtype=Type11Enum.DEFAULT,
            account='account2',
            amount=SplitAmount(
                value=110,
                currency='currency2'
            ),
            description='description2',
            reference='reference2'
        ),
        Split(
            mtype=Type11Enum.DEFAULT,
            account='account2',
            amount=SplitAmount(
                value=110,
                currency='currency2'
            ),
            description='description2',
            reference='reference2'
        )
    ],
    sub_merchants=[
        SubMerchantInfo(
            address=BillingAddress4(
                city='city6',
                country='country0',
                house_number_or_name='houseNumberOrName4',
                postal_code='postalCode8',
                street='street6',
                state_or_province='stateOrProvince4'
            ),
            amount=Amount32(
                currency='currency2',
                value=110
            ),
            email='email6',
            id='id0',
            mcc='mcc0'
        )
    ]
)
```

