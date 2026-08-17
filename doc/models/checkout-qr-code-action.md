
# Checkout Qr Code Action

## Structure

`CheckoutQrCodeAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `str` | Optional | Expiry time of the QR code. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `qr_code_data` | `str` | Optional | The contents of the QR code as a UTF8 string. |
| `mtype` | `str` | Required, Constant | **qrCode**<br><br>**Value**: `"qrCode"` |
| `url` | `str` | Optional | Specifies the URL to redirect to. |

## Example

```python
from adyen.models.checkout_qr_code_action import CheckoutQrCodeAction

checkout_qr_code_action = CheckoutQrCodeAction(
    expires_at='expiresAt0',
    payment_data='paymentData6',
    payment_method_type='paymentMethodType6',
    qr_code_data='qrCodeData6',
    url='url8'
)
```

