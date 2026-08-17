
# Merchant Refund Reason Enum

The reason for the refund request.

Possible values:

* **FRAUD**

* **CUSTOMER REQUEST**

* **RETURN**

* **DUPLICATE**

* **OTHER**

## Enumeration

`MerchantRefundReasonEnum`

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
from adyen.models.merchant_refund_reason_enum import MerchantRefundReasonEnum

merchant_refund_reason = MerchantRefundReasonEnum.OTHER
```

