
# Payment Cancel Response

## Structure

`PaymentCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to cancel. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the cancel request. |
| `reference` | `str` | Optional | Your reference for the cancel request. |
| `status` | `str` | Required, Constant | The status of your request. This will always have the value **received**.<br><br>**Value**: `"received"` |

## Example

```python
from adyen.models.payment_cancel_response import PaymentCancelResponse

payment_cancel_response = PaymentCancelResponse(
    merchant_account='merchantAccount2',
    payment_psp_reference='paymentPspReference8',
    psp_reference='pspReference2',
    reference='reference4'
)
```

