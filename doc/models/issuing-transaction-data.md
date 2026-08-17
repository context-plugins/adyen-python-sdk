
# Issuing Transaction Data

## Structure

`IssuingTransactionData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `capture_cycle_id` | `str` | Optional | captureCycleId associated with transfer event. |
| `mtype` | `str` | Required, Constant | The type of events data.<br><br>Possible values:<br><br>- **issuingTransactionData**: issuing transaction data<br><br>**Value**: `"issuingTransactionData"` |

## Example

```python
from adyen.models.issuing_transaction_data import IssuingTransactionData

issuing_transaction_data = IssuingTransactionData(
    capture_cycle_id='captureCycleId6'
)
```

