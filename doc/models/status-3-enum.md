
# Status 3 Enum

Status of the payment link. Possible values:

* **active**: The link can be used to make payments.
* **expired**: The expiry date for the payment link has passed. Shoppers can no longer use the link to make payments.
* **completed**: The shopper completed the payment.
* **paymentPending**: The shopper is in the process of making the payment. Applies to payment methods with an asynchronous flow.

## Enumeration

`Status3Enum`

## Fields

| Name |
|  --- |
| `ACTIVE` |
| `COMPLETED` |
| `EXPIRED` |
| `PAID` |
| `PAYMENTPENDING` |

## Example

```python
from adyen.models.status_3_enum import Status3Enum

status_3 = Status3Enum.PAID
```

