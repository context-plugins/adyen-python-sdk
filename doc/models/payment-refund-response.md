
# Payment Refund Response

## Structure

`PaymentRefundResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount39`](../../doc/models/amount-39.md) | Required | The refund amount. |
| `capture_psp_reference` | `str` | Optional | This is only available for PayPal refunds. The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the specific capture to refund. |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `merchant_refund_reason` | [`MerchantRefundReason1Enum`](../../doc/models/merchant-refund-reason-1-enum.md) | Optional | Your reason for the refund request. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to refund. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the refund request. |
| `reference` | `str` | Optional | Your reference for the refund request. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/split-payments) or [platforms](https://docs.adyen.com/platforms/online-payments/split-payments/). |
| `status` | `str` | Required, Constant | The status of your request. This will always have the value **received**.<br><br>**Value**: `"received"` |
| `store` | `str` | Optional | The online store or [physical store](https://docs.adyen.com/point-of-sale/design-your-integration/determine-account-structure/#create-stores) that is processing the refund. This must be the same as the store name configured in your Customer Area.  Otherwise, you get an error and the refund fails. |

## Example

```python
from adyen.models.amount_39 import Amount39
from adyen.models.line_item import LineItem
from adyen.models.merchant_refund_reason_1_enum import MerchantRefundReason1Enum
from adyen.models.payment_refund_response import PaymentRefundResponse
from adyen.models.split import Split
from adyen.models.split_amount import SplitAmount
from adyen.models.type_11_enum import Type11Enum

payment_refund_response = PaymentRefundResponse(
    amount=Amount39(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount0',
    payment_psp_reference='paymentPspReference4',
    psp_reference='pspReference0',
    capture_psp_reference='capturePspReference6',
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
        )
    ],
    merchant_refund_reason=MerchantRefundReason1Enum.DUPLICATE,
    reference='reference6',
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
    ]
)
```

