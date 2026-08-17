
# Payment Reversal Response

## Structure

`PaymentReversalResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_psp_reference` | `str` | Required | The [`pspReference`](https://docs.adyen.com/api-explorer/Checkout/latest/post/payments#responses-200-pspReference) of the payment to reverse. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the reversal request. |
| `reference` | `str` | Optional | Your reference for the reversal request. |
| `status` | `str` | Required, Constant | The status of your request. This will always have the value **received**.<br><br>**Value**: `"received"` |

## Example

```python
from adyen.models.payment_reversal_response import PaymentReversalResponse

payment_reversal_response = PaymentReversalResponse(
    merchant_account='merchantAccount6',
    payment_psp_reference='paymentPspReference0',
    psp_reference='pspReference6',
    reference='reference2'
)
```

