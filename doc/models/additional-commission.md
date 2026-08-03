
# Additional Commission

*This model accepts additional fields of type Any.*

## Structure

`AdditionalCommission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Optional | Unique identifier of the balance account to which the additional commission is booked. |
| `fixed_amount` | `int` | Optional | A fixed commission fee, in minor units. |
| `variable_percentage` | `int` | Optional | A variable commission fee, in basis points. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_commission import AdditionalCommission

additional_commission = AdditionalCommission(
    balance_account_id='balanceAccountId6',
    fixed_amount=180,
    variable_percentage=88,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

