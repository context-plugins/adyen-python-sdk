
# Merchant Refund Reason 1 Enum

Your reason for the refund request.

## Enumeration

`MerchantRefundReason1Enum`

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
from adyen.models.merchant_refund_reason_1_enum import MerchantRefundReason1Enum

merchant_refund_reason_1 = MerchantRefundReason1Enum.ENUM_CUSTOMER_REQUEST
```

