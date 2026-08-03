
# Additional Commission 1

Defines whether to book an additional commission for payments to your user's balance account. The commission amount can be defined as a fixed amount (specified in minor units), a percentage (specified in basis points), or both.

*This model accepts additional fields of type Any.*

## Structure

`AdditionalCommission1`

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

from adyen.models.additional_commission_1 import AdditionalCommission1

additional_commission_1 = AdditionalCommission1(
    balance_account_id='balanceAccountId0',
    fixed_amount=126,
    variable_percentage=38,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

