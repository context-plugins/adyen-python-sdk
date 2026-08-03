
# Refund Not Paid Out Transfers Request

*This model accepts additional fields of type Any.*

## Structure

`RefundNotPaidOutTransfersRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_code` | `str` | Required | The code of the account from which to perform the refund(s). |
| `account_holder_code` | `str` | Required | The code of the Account Holder which owns the account from which to perform the refund(s). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.refund_not_paid_out_transfers_request import RefundNotPaidOutTransfersRequest

refund_not_paid_out_transfers_request = RefundNotPaidOutTransfersRequest(
    account_code='accountCode6',
    account_holder_code='accountHolderCode2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

