
# Receipt Printing

## Structure

`ReceiptPrinting`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_approved` | `bool` | Optional | Print a merchant receipt when the payment is approved. |
| `merchant_cancelled` | `bool` | Optional | Print a merchant receipt when the transaction is cancelled. |
| `merchant_capture_approved` | `bool` | Optional | Print a merchant receipt when capturing the payment is approved. |
| `merchant_capture_refused` | `bool` | Optional | Print a merchant receipt when capturing the payment is refused. |
| `merchant_refund_approved` | `bool` | Optional | Print a merchant receipt when the refund is approved. |
| `merchant_refund_refused` | `bool` | Optional | Print a merchant receipt when the refund is refused. |
| `merchant_refused` | `bool` | Optional | Print a merchant receipt when the payment is refused. |
| `merchant_void` | `bool` | Optional | Print a merchant receipt when a previous transaction is voided. |
| `shopper_approved` | `bool` | Optional | Print a shopper receipt when the payment is approved. |
| `shopper_cancelled` | `bool` | Optional | Print a shopper receipt when the transaction is cancelled. |
| `shopper_capture_approved` | `bool` | Optional | Print a shopper receipt when capturing the payment is approved. |
| `shopper_capture_refused` | `bool` | Optional | Print a shopper receipt when capturing the payment is refused. |
| `shopper_refund_approved` | `bool` | Optional | Print a shopper receipt when the refund is approved. |
| `shopper_refund_refused` | `bool` | Optional | Print a shopper receipt when the refund is refused. |
| `shopper_refused` | `bool` | Optional | Print a shopper receipt when the payment is refused. |
| `shopper_void` | `bool` | Optional | Print a shopper receipt when a previous transaction is voided. |

## Example

```python
from adyen.models.receipt_printing import ReceiptPrinting

receipt_printing = ReceiptPrinting(
    merchant_approved=False,
    merchant_cancelled=False,
    merchant_capture_approved=False,
    merchant_capture_refused=False,
    merchant_refund_approved=False
)
```

