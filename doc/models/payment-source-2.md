
# Payment Source 2

The source used to obtain the payload. Possible values: `qr`, `redirect`, and `pushNotification`.

## Enumeration

`PaymentSource2`

## Fields

| Name |
|  --- |
| `REDIRECT` |
| `QR` |
| `PUSHNOTIFICATION` |

## Example

```python
from adyen.models.payment_source_2 import PaymentSource2

payment_source_2 = PaymentSource2.QR
```

