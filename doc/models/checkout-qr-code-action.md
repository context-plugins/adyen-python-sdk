
# Checkout Qr Code Action

*This model accepts additional fields of type Any.*

## Structure

`CheckoutQrCodeAction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expires_at` | `str` | Optional | Expiry time of the QR code. |
| `payment_data` | `str` | Optional | Encoded payment data. |
| `payment_method_type` | `str` | Optional | Specifies the payment method. |
| `qr_code_data` | `str` | Optional | The contents of the QR code as a UTF8 string. |
| `mtype` | [`Type563`](../../doc/models/type-563.md) | Required | **qrCode** |
| `url` | `str` | Optional | Specifies the URL to redirect to. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.checkout_qr_code_action import CheckoutQrCodeAction
from adyen.models.type_563 import Type563

checkout_qr_code_action = CheckoutQrCodeAction(
    mtype=Type563.QRCODE,
    expires_at='expiresAt0',
    payment_data='paymentData6',
    payment_method_type='paymentMethodType6',
    qr_code_data='qrCodeData6',
    url='url8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

