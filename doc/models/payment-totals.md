
# Payment Totals

Totals of the payment transaction during the reconciliation period.

*This model accepts additional fields of type Any.*

## Structure

`PaymentTotals`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`TransactionType11`](../../doc/models/transaction-type-11.md) | Required | - |
| `transaction_count` | `int` | Required | Number of processed transaction during the period. |
| `transaction_amount` | `float` | Required | Sum of amount of processed transaction during the period.<br><br>**Constraints**: `>= 0`, `<= 99999999.999999` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_totals import PaymentTotals
from adyen.models.transaction_type_11 import TransactionType11

payment_totals = PaymentTotals(
    transaction_type=TransactionType11.UPDATERESERVATION,
    transaction_count=220,
    transaction_amount=21.08,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

