
# Receipt Printing 1

Transaction outcomes that you want the terminal to print a merchant receipt or a shopper receipt for.

*This model accepts additional fields of type Any.*

## Structure

`ReceiptPrinting1`

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
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.receipt_printing_1 import ReceiptPrinting1

receipt_printing_1 = ReceiptPrinting1(
    merchant_approved=False,
    merchant_cancelled=False,
    merchant_capture_approved=False,
    merchant_capture_refused=False,
    merchant_refund_approved=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

