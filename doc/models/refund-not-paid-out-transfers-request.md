
# Refund Not Paid Out Transfers Request

## Structure

`RefundNotPaidOutTransfersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account from which to perform the refund(s). |
| `account_holder_code` | `str` | Required | The code of the Account Holder which owns the account from which to perform the refund(s). |

## Example

```python
from adyen.models.refund_not_paid_out_transfers_request import RefundNotPaidOutTransfersRequest

refund_not_paid_out_transfers_request = RefundNotPaidOutTransfersRequest(
    account_code='accountCode6',
    account_holder_code='accountHolderCode2'
)
```

