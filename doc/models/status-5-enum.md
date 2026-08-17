
# Status 5 Enum

The status of the session. The status included in the response doesn't get updated. Don't make the request again to check for payment status updates.

Possible values:

* **completed**: the shopper completed the payment, and the payment was authorized.
* **paymentPending**: the shopper is in the process of making the payment. This applies to payment methods with an asynchronous flow, like voucher payments where the shopper completes the payment in a physical shop.
* **refused**: the session has been refused, because of too many refused payment attempts. The shopper can no longer complete the payment with this session.
* **canceled**: the shopper canceled the payment.
* **expired**: the session expired. The shopper can no longer complete the payment with this session. By default, the session expires one hour after it is created.

## Enumeration

`Status5Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `CANCELED` |
| `COMPLETED` |
| `EXPIRED` |
| `PAYMENTPENDING` |
| `REFUSED` |

## Example

```python
from adyen.models.status_5_enum import Status5Enum

status_5 = Status5Enum.COMPLETED
```

