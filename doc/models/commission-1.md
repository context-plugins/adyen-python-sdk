
# Commission 1

Defines your platform's commission for the processed payments as a fixed amount (specified in minor units), a percentage (specified in basis points), or both. The commission is booked to your platform's liable balance account.

*This model accepts additional fields of type Any.*

## Structure

`Commission1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed_amount` | `int` | Optional | A fixed commission fee, in minor units. |
| `variable_percentage` | `int` | Optional | A variable commission fee, in basis points. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.commission_1 import Commission1

commission_1 = Commission1(
    fixed_amount=18,
    variable_percentage=182,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

