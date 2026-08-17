
# Payment Source 2 Enum

The source used to obtain the payload. Possible values: `qr`, `redirect`, and `pushNotification`.

## Enumeration

`PaymentSource2Enum`

## Fields

| Name |
|  --- |
| `REDIRECT` |
| `QR` |
| `PUSHNOTIFICATION` |

## Example

```python
from adyen.models.payment_source_2_enum import PaymentSource2Enum

payment_source_2 = PaymentSource2Enum.QR
```

