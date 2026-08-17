
# Payment Amount Update Response

## Structure

`PaymentAmountUpdateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `adjust_authorisation_data` | `str` | Optional | The data blob for subsequent synchronous adjust authorisation calls. Returned when the synchronous flow is used. |
| `amount` | [`Amount30`](../../doc/models/amount-30.md) | Required | The updated amount. |
| `industry_usage` | [`IndustryUsage1Enum`](../../doc/models/industry-usage-1-enum.md) | Optional | The reason for the amount update. Possible values:<br><br>* **delayedCharge**<br>* **noShow**<br>* **installment** |
| `line_items` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Price and product information of the refunded items, required for [partial refunds](https://docs.adyen.com/online-payments/refund#refund-a-payment).<br><br>> This field is required for partial refunds with 3x 4x Oney, Affirm, Afterpay, Atome, Clearpay, Klarna, Ratepay, Walley, and Zip. |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to update. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the amount update request. |
| `reference` | `str` | Required | Your reference for the amount update request. Maximum length: 80 characters. |
| `splits` | [`List[Split]`](../../doc/models/split.md) | Optional | An array of objects specifying how the amount should be split between accounts when using Adyen for Platforms. For more information, see how to process payments for [marketplaces](https://docs.adyen.com/marketplaces/process-payments) or [platforms](https://docs.adyen.com/platforms/process-payments). |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Required | The status of your request.<br><br>If you included `adjustAuthorisationData` in your request, possible values are the following:<br><br>* **authorised**<br><br>* **refused**<br><br>Otherwise, the value is **received**. |

## Example

```python
from adyen.models.amount_30 import Amount30
from adyen.models.industry_usage_1_enum import IndustryUsage1Enum
from adyen.models.line_item import LineItem
from adyen.models.payment_amount_update_response import PaymentAmountUpdateResponse
from adyen.models.split import Split
from adyen.models.split_amount import SplitAmount
from adyen.models.status_2_enum import Status2Enum
from adyen.models.type_11_enum import Type11Enum

payment_amount_update_response = PaymentAmountUpdateResponse(
    amount=Amount30(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount8',
    payment_psp_reference='paymentPspReference2',
    psp_reference='pspReference8',
    reference='reference4',
    status=Status2Enum.REFUSED,
    adjust_authorisation_data='adjustAuthorisationData8',
    industry_usage=IndustryUsage1Enum.NOSHOW,
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
        )
    ]
)
```

