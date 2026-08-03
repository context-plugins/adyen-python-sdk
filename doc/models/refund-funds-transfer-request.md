
# Refund Funds Transfer Request

*This model accepts additional fields of type Any.*

## Structure

`RefundFundsTransferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Required | - |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user in order to link multiple transactions to one another. |
| `original_reference` | `str` | Required | A PSP reference of the original fund transfer. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.refund_funds_transfer_request import RefundFundsTransferRequest

refund_funds_transfer_request = RefundFundsTransferRequest(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    original_reference='originalReference4',
    merchant_reference='merchantReference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

