
# Patchable Amount Dto 1

The balance threshold that triggers the top-up. If the balance falls below this amount, a top-up is initiated.

*This model accepts additional fields of type Any.*

## Structure

`PatchableAmountDto1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). |
| `value` | `int` | Optional | The amount of the transaction, in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_amount_dto_1 import PatchableAmountDto1

patchable_amount_dto_1 = PatchableAmountDto1(
    currency='currency6',
    value=138,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

