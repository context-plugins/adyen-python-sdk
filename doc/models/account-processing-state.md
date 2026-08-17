
# Account Processing State

## Structure

`AccountProcessingState`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `disable_reason` | `str` | Optional | The reason why processing has been disabled. |
| `disabled` | `bool` | Optional | Indicates whether the processing of payments is allowed. |
| `processed_from` | [`Amount`](../../doc/models/amount.md) | Optional | The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier). |
| `processed_to` | [`Amount`](../../doc/models/amount.md) | Optional | The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier). |
| `tier_number` | `int` | Optional | The processing tier that the account holder occupies. |

## Example

```python
from adyen.models.account_processing_state import AccountProcessingState
from adyen.models.amount import Amount

account_processing_state = AccountProcessingState(
    disable_reason='disableReason4',
    disabled=False,
    processed_from=Amount(
        currency='currency4',
        value=148
    ),
    processed_to=Amount(
        currency='currency2',
        value=54
    ),
    tier_number=206
)
```

