
# Merchant Refund Reason

The reason for the refund request.

Possible values:

* **FRAUD**

* **CUSTOMER REQUEST**

* **RETURN**

* **DUPLICATE**

* **OTHER**

## Enumeration

`MerchantRefundReason`

## Fields

| Name |
|  --- |
| `FRAUD` |
| `ENUM_CUSTOMER_REQUEST` |
| `RETURN` |
| `DUPLICATE` |
| `OTHER` |

## Example

```python
from adyen.models.merchant_refund_reason import MerchantRefundReason

merchant_refund_reason = MerchantRefundReason.OTHER
```

