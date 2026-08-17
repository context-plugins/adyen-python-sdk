
# Additional Commission

## Structure

`AdditionalCommission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | Unique identifier of the balance account to which the additional commission is booked. |
| `fixed_amount` | `int` | Optional | A fixed commission fee, in minor units. |
| `variable_percentage` | `int` | Optional | A variable commission fee, in basis points. |

## Example

```python
from adyen.models.additional_commission import AdditionalCommission

additional_commission = AdditionalCommission(
    balance_account_id='balanceAccountId6',
    fixed_amount=180,
    variable_percentage=88
)
```

