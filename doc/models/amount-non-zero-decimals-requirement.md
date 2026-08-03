
# Amount Non Zero Decimals Requirement

*This model accepts additional fields of type Any.*

## Structure

`AmountNonZeroDecimalsRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies for which routes the amount in a transfer request must have no non-zero decimal places, so the transfer can only be processed if the amount consists of round numbers. |
| `mtype` | [`Type94`](../../doc/models/type-94.md) | Required | **amountNonZeroDecimalsRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_non_zero_decimals_requirement import AmountNonZeroDecimalsRequirement
from adyen.models.type_94 import Type94

amount_non_zero_decimals_requirement = AmountNonZeroDecimalsRequirement(
    mtype=Type94.AMOUNTNONZERODECIMALSREQUIREMENT,
    description='description8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

