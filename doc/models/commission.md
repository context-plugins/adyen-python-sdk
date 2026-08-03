
# Commission

*This model accepts additional fields of type Any.*

## Structure

`Commission`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed_amount` | `int` | Optional | A fixed commission fee, in minor units. |
| `variable_percentage` | `int` | Optional | A variable commission fee, in basis points. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.commission import Commission

commission = Commission(
    fixed_amount=112,
    variable_percentage=52,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

