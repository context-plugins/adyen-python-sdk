
# Patchable Other Info

*This model accepts additional fields of type Any.*

## Structure

`PatchableOtherInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description_of_issue` | `str` | Optional | Your description of the issue for raising a dispute of `type` **other**.<br><br>**Constraints**: *Minimum Length*: `0`, *Maximum Length*: `2500` |
| `sub_type` | [`SubType11`](../../doc/models/sub-type-11.md) | Optional | - |
| `what_was_purchased` | [`ProductType1`](../../doc/models/product-type-1.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.patchable_other_info import PatchableOtherInfo
from adyen.models.product_type_1 import ProductType1
from adyen.models.sub_type_11 import SubType11

patchable_other_info = PatchableOtherInfo(
    description_of_issue='descriptionOfIssue0',
    sub_type=SubType11.CANCELLEDRECURRING,
    what_was_purchased=ProductType1.GOODS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

