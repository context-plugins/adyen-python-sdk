
# Patchable Top Up Amount

*This model accepts additional fields of type Any.*

## Structure

`PatchableTopUpAmount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fixed` | [PatchableAmountDTO](../../doc/models/patchable-amount-dto.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `target` | [PatchableAmountDTO](../../doc/models/patchable-amount-dto.md) \| Any \| None | Optional | This is a container for one-of cases. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_amount_dto import PatchableAmountDto
from adyen.models.patchable_top_up_amount import PatchableTopUpAmount

patchable_top_up_amount = PatchableTopUpAmount(
    fixed=PatchableAmountDto(
        currency='currency2',
        value=164,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    target=PatchableAmountDto(
        currency='currency2',
        value=164,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

