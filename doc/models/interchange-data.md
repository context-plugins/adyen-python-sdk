
# Interchange Data

## Structure

`InterchangeData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `interchange_amount` | [`Amount17`](../../doc/models/amount-17.md) | Optional | The currency and value of the adjusted interchange fee. |
| `interchange_rate_indicator` | `str` | Optional | A 3-character alphanumeric code assigned by Visa that identifies the specific interchange reimbursement program a transaction qualified for. The code is assigned based on the card type, entry mode, and security data provided. |
| `mtype` | `str` | Required, Constant | The type of events data.<br><br>Possible values:<br><br>- **interchangeData**: information about the interchange fee applied to a transaction.<br><br>**Value**: `"interchangeData"` |

## Example

```python
from adyen.models.amount_17 import Amount17
from adyen.models.interchange_data import InterchangeData

interchange_data = InterchangeData(
    interchange_amount=Amount17(
        currency='currency2',
        value=62
    ),
    interchange_rate_indicator='interchangeRateIndicator6'
)
```

