
# Merchant Refund Reason 1

Your reason for the refund request.

## Enumeration

`MerchantRefundReason1`

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
from adyen.models.merchant_refund_reason_1 import MerchantRefundReason1

merchant_refund_reason_1 = MerchantRefundReason1.ENUM_CUSTOMER_REQUEST
```

