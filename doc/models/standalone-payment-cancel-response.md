
# Standalone Payment Cancel Response

## Structure

`StandalonePaymentCancelResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account that is used to process the payment. |
| `payment_reference` | `str` | Required | The [`reference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_reference) of the payment to cancel. |
| `psp_reference` | `str` | Required | Adyen's 16-character reference associated with the cancel request. |
| `reference` | `str` | Optional | Your reference for the cancel request. |
| `status` | `str` | Required, Constant | The status of your request. This will always have the value **received**.<br><br>**Value**: `"received"` |

## Example

```python
from adyen.models.standalone_payment_cancel_response import StandalonePaymentCancelResponse

standalone_payment_cancel_response = StandalonePaymentCancelResponse(
    merchant_account='merchantAccount8',
    payment_reference='paymentReference6',
    psp_reference='pspReference8',
    reference='reference2'
)
```

